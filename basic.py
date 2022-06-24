import cv2, time

img = cv2.imread("galaxy.jpg",0)
print(type(img))
shape = img.shape
print(shape)
print(img.ndim)
print(img)
print(help(cv2.resize))

resized_img = cv2.resize(img, (shape[1]//2, shape[0]//2))
print(cv2.imshow("Test", resized_img))
cv2.waitKey(0)
cv2.destroyAllWindows()
