import cv2
import os

CASCADE = 'faces.xml'
COLOR = (255, 255, 255)
WIDTH = 4
SCALE = 1.1
NEIGHBORS = 4

def has_face(image_path):
    image = cv2.imread(image_path, 1)
    face_cascade = cv2.CascadeClassifier(CASCADE)

    faces = face_cascade.detectMultiScale(image, SCALE, NEIGHBORS)
    # Loop through face values
    for (x, y, w, h) in faces:
        # Draw rectangle around detected face, 255s for white colored rectangles, width set to 4
        cv2.rectangle(image, (x, y), (x+w, y+h), COLOR, WIDTH)
    return image

images = os.listdir('faces')
for image in images:
    face_image = has_face(f'faces/{image}')
    if face_image is not None:
        cv2.imwrite(f'faces/{image}-analyzed.jpeg', face_image)
