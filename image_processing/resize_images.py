import cv2
import os


def calculate_size(scale_percentage, width, height):
    new_width = int(width * scale_percentage / 100)
    new_height = int(height * scale_percentage / 100)
    return new_width, new_height


def resize(image_path, scale_percentage, resized_path):
    original_image = cv2.imread(image_path)
    new_dim = calculate_size(scale_percentage, original_image.shape[1], original_image.shape[0])
    resized_image = cv2.resize(original_image, new_dim)
    cv2.imwrite(resized_path, resized_image)


images = os.listdir('images')
print(images)

for image in images:
    resize(f'images/{image}', 10, f'images/resized_{image}')
