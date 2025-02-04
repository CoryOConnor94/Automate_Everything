import cv2
import numpy as np


background = cv2.imread('safari.jpeg')
foreground = cv2.imread('giraffe.jpeg')

print(foreground[40, 40])
width = foreground.shape[1]
height = foreground.shape[0]

background_resized = cv2.resize(background, (width, height))

for i in range(width):
    for j in range(height):
        pixel = foreground[j, i]
        if np.any(pixel == [1, 255, 0]):
            foreground[j, i] = background_resized[j, i]

cv2.imwrite('output.jpeg', foreground)