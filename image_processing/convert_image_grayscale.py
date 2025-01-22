import cv2
import os
import numpy as np


# Read in image in color
color = cv2.imread('galaxy.jpeg', 1)
print(color)

# Read in image in Grayscale
image = cv2.imread('images/galaxy.jpeg', 0)
cv2.imwrite('grayscale_images/galaxy-gray.jpeg', image)

# Convert image to Grayscale
gray_image = cv2.cvtColor(color, cv2.COLOR_BGR2GRAY)
cv2.imwrite('galaxy-gray.jpeg', gray_image)

# Convert multiple images to grayscale
images = os.listdir('images')
print(images)
for image in images:
    gray = cv2.imread(f'images/{image}', 0)
    cv2.imwrite(f'grayscale_images/Gray-{image}', gray)





