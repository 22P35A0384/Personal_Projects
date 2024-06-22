import os
import requests
import csv

def download_image(url, folder, filename):
    """Downloads an image from the given URL and saves it to the specified folder with the provided filename.

    Args:
        url: The URL of the image to download.
        folder: The folder path where the image should be saved.
        filename: The desired filename for the downloaded image.
    """
    # Create the full path for the image
    full_path = os.path.join(folder, filename)

    # Send a GET request to the URL
    response = requests.get(url, stream=True)
    x = []
    # Check for successful response
    if response.status_code == 200:
        # Create the folder if it doesn't exist
        os.makedirs(folder, exist_ok=True)

        # Open the file in binary write mode
        with open(full_path, 'wb') as file:
            for chunk in response.iter_content(1024):
                file.write(chunk)
        # print(f"Image downloaded successfully: {full_path}")
        return True
    else:
        # print(f"Failed to download image. Status code: {response.status_code}")
        # x.append(roll)
        # print(x)
        return False

# Example usage
# image_url = "https://info.aec.edu.in/ACET/StudentPhotos/22p35a0384.jpg"
# download_folder = "acet_2021_1"
# download_filename = "my_image2.jpg"

# status = download_image(image_url, download_folder, download_filename)

# with open('log.csv', 'w', newline='') as csvfile:
#     writer = csv.writer(csvfile)
#     writer.writerow('sucess')
#     print(status)


# with open('testdata.csv', newline='', encoding='utf-8') as f1 :
#     data = list(csv.reader(f1))
#     data = data[1:]

# tc = 0
# fc = 0
# sc = 0
# fc_list = []
# for d in data:
#     if d[8]=='AEC':
#         image_url = "https://info.aec.edu.in/AEC/StudentPhotos/"+d[3]+".jpg"
#     elif d[8]=='ACET':
#         image_url = "https://info.aec.edu.in/ACET/StudentPhotos/"+d[3]+".jpg"
#     elif d[8]=='ACOE':
#         image_url = "https://info.aec.edu.in/ACOE/StudentPhotos/"+d[3]+".jpg"
#     download_folder = "main_images"
#     download_filename = d[3]+".jpg"

#     status = download_image(image_url, download_folder, download_filename)
    
#     if status==True:
#         tc+=1
#         sc+=1
#         print(str(tc)+', '+str(sc)+'. '+d[3]+' success')
#     else:
#         tc+=1
#         fc+=1
#         fc_list.append(d[3])
#         print(str(tc)+', '+str(fc)+'. '+d[3]+' failed')
#         print(fc_list)
#     with open('log3.csv', 'w', newline='') as csvfile:
#         writer = csv.writer(csvfile)
#         writer.writerow([d[3],str(status),tc,sc,fc,fc_list])
#         # print(status)
# print(str(tc)+', '+str(sc)+', '+str(fc)+', ')
# print(fc_list)

with open('2020_acet.csv') as f1 :
    data = list(csv.reader(f1))
    data = data[1:]
# print(data[0])

with open('2020_acet_log.csv', 'w', newline='') as log:
    c = 0
    sc = 0
    fc = 0
    writer = csv.writer(log)
    for d in data:
        image_url = "https://info.aec.edu.in/ACET/StudentPhotos/"+d[1]+".jpg"
        download_folder = "acet_2020"
        download_filename = d[1]+".jpg"

        x =  download_image(image_url, download_folder, download_filename)
        c+=1
        if x==True:
            sc+=1
            writer.writerow([sc,d[1],'success'])
            print(str(c)+' '+d[1]+'.jpg - success')
        else:
            fc+=1
            writer.writerow([fc,d[1],'failed'])
            print(str(c)+' '+d[1]+' - failed')
