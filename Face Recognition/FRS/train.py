import os
import numpy as np
import cv2
from sklearn.svm import SVC
from sklearn.decomposition import PCA
from sklearn.pipeline import make_pipeline
import joblib

# Function to load face images and labels
def load_data(image_paths):
    images = []
    labels = []
    for path in image_paths:
        img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
        if img is not None:  # Check if the image was loaded successfully
            # Resize image to a common size (e.g., 100x100)
            img = cv2.resize(img, (100, 100))
            images.append(img.flatten())
            person_name = os.path.basename(path).split('.')[0]  # Extract person's name from the file name
            labels.append(person_name)
        else:
            print(f"Failed to load image: {path}")
    return np.array(images), np.array(labels)

# Path to the directory containing face images
image_dir = './images'

# List all image paths (provide two images of the same person)
image_paths = ['./images/21P31A0225.jpg', './images/21P31A0472.jpg']

# Load data
X, y = load_data(image_paths)

# Preprocess data: PCA for dimensionality reduction
pca = PCA(n_components=1, whiten=True, random_state=42)
svc = SVC(kernel='rbf', class_weight='balanced')
model = make_pipeline(pca, svc)

# Train the model
model.fit(X, y)

# Save the trained model
joblib.dump(model, "trained_model.pkl")  # Save the trained model to a file named "trained_model.pkl"
