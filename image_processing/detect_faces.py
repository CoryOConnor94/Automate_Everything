import cv2

image = cv2.imread('humans.jpeg', 1)
face_cascade = cv2.CascadeClassifier('faces.xml')

faces = face_cascade.detectMultiScale(image, 1.1, 4)

# Loop through face values
for (x, y, w, h) in faces:
    # Draw rectangle around detected face, 255s for white colored rectangles, width set to 4
    cv2.rectangle(image, (x, y), (x+w, y+h), (255, 255, 255), 4)

cv2.imwrite('human_faces.jpeg', image)