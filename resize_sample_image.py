import cv2
import os
path_file = r"\ComputerVision\sample_images"
for file in os.listdir(path_file):
    img = cv2.imread(f"{path_file}\{file}", 0)
    shape = img.shape

    resized = cv2.resize(img, (shape[1]//2, shape[0]//2))
    cv2.imwrite(fr"{path_file}\resized_{file}", resized)
