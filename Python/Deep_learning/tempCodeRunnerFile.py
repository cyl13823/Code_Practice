import torch
import torch.nn as nn
import requests
import zipfile
from pathlib import Path
import random
import matplotlib.pyplot as plt

random.seed(42)

# Set path to data folder
data_path = Path("data/")
image_path = data_path / "images"

# If the image folder doesn't exist, download it and prepare it
if image_path.is_dir():
    print(f"{image_path} directory exists.")
else:
    print(f"Directory doesn't exist, creating one...")
    image_path.mkdir(parents=True, exist_ok=True)

    # Download images
    with open(data_path / "images.zip", "wb") as f:
        request = requests.get("https://github.com/mrdbourke/pytorch-deep-learning/raw/main/data/pizza_steak_sushi.zip")
        print("Downloading images")
        f.write(request.content)
    
    # Unzip images
    with zipfile.ZipFile(data_path / "images.zip", "r") as zip_ref:
        print("Unzipping images...")
        zip_ref.extractall(image_path)

# Check numbers of the images in the directories
import os
def walk_through_dir(dir_path):
  for dirpath, dirnames, filenames in os.walk(dir_path):
    print(f"There are {len(dirnames)} directories and {len(filenames)} images in '{dirpath}'.")

walk_through_dir(image_path)

# Setup training and testing paths
train_dir = image_path / "train"
test_dir = image_path / "test"

# Visualize an image
from PIL import Image  # Python Image Library

# 1. Get all image paths (* means "any combination")
image_path_list = list(image_path.glob("*/*/*.jpg"))

# 2. Get random image path
random_image_path = random.choice(image_path_list)

# 3. Get image class from path name (the image class is the name of the directory where the image is stored)
image_class = random_image_path.parent.stem

# 4. Open image
img = Image.open(random_image_path)

# 5. Print metadata
print(f"Random image path: {random_image_path}")
print(f"Image class: {image_class}")
print(f"Image height: {img.height}") 
print(f"Image width: {img.width}")
plt.imshow(img)
plt.axis('off')
plt.show()