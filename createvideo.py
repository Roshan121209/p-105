import os
import cv2

path = "C:/Users/rosha/OneDrive/Desktop/roshan/random things/codes/p-105/images"
images = []

for i in os.listdir(path):
    name, extension = os.path.splitext(i)
    if extension.lower() in ['.jpg', '.jpeg', '.png', '.gif', '.jfif']:
        file_name = path + "/" + i
        images.append(file_name)
        print(file_name)

count = len(images)

frame = cv2.imread(images[0])
height, width, channels = frame.shape
size = (width, height)

print(size)
out = cv2.VideoWriter('project.avi', cv2.VideoWriter_fourcc(*'DIVX'), 0.8, size)

for i in range(0, count - 1):
    img = cv2.imread(images[i])
    out.write(img)

out.release()

print("Done")


