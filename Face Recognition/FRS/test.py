# import cv2
# import numpy as np
# import joblib

# # Load the trained model
# model = joblib.load("trained_model.pkl")  # Replace "trained_model.pkl" with the path to your trained model file

# # Function to recognize a person in a new image
# def recognize_person(image_path, model):
#     # Load the new image
#     new_img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
#     new_img_vector = new_img.flatten()

#     # Predict the person in the new image
#     predicted_person = model.predict([new_img_vector])
#     return predicted_person[0]

# # Path to the new image
# new_image_path = "./images/22P35A0384.jpg"

# # Recognize the person in the new image
# predicted_person = recognize_person(new_image_path, model)
# print("Predicted person:", predicted_person)

import cv2
import joblib

# Load the trained model
model = joblib.load("trained_model.pkl")

# Function to recognize a person in a new image
def recognize_person(image_path, model):
    # Load and preprocess the new image
    new_img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    new_img = cv2.resize(new_img, (100, 100))  # Resize the image to the same size used during training
    new_img_vector = new_img.flatten()

    # Predict the person using the trained model
    predicted_person = model.predict([new_img_vector])

    return predicted_person

# Path to the new image
new_image_path = './images/peddakka.jpg'

# Recognize the person in the new image
predicted_person = recognize_person(new_image_path, model)

print("Predicted person:", predicted_person)

