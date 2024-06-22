import csv
import pymongo

# Connect to MongoDB
client = pymongo.MongoClient("mongodb+srv://gangadharjami:Xyd11TsTf0GfkNLu@cluster0.egjdqci.mongodb.net/cluster0?retryWrites=true&w=majority")
db = client["cluster0"]
collection = db["students_datas"]

# Function to clean and encode data
def clean_and_encode(text):
    try:
        # Attempt to encode the text as UTF-8
        cleaned_text = text.encode('utf-8', 'ignore').decode('utf-8')
        return cleaned_text
    except Exception as e:
        print(f"Error cleaning text: {e}")
        return None

# Read CSV file and insert data into MongoDB
def upload_csv_to_mongodb(filename):
    try:
        with open(filename, newline='', encoding='utf-8',errors='ignore') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                # Cleanse and encode each field in the row
                cleaned_row = {key: clean_and_encode(value) for key, value in row.items()}
                # Insert the cleaned row into MongoDB
                collection.insert_one(cleaned_row)
        print("Data uploaded successfully to MongoDB")
    except Exception as e:
        print(f"Error uploading data to MongoDB: {e}")

# Example usage
upload_csv_to_mongodb('2023_acoe.csv')
