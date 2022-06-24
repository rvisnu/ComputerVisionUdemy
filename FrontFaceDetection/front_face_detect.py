import cv2

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
picture = "picture.jpg"
color_image = cv2.imread(picture)
grey_image = cv2.imread(picture, 0)

faces = face_cascade.detectMultiScale(grey_image, scaleFactor=1.05, minNeighbors=5)
for x,y,w,h in faces:
    color_image = cv2.rectangle(color_image, (x,y), (x+w, y+h), (255,0,0), 3)

cv2.imshow("updated", color_image)
cv2.waitKey(0)
cv2.destroyAllWindows()