import cv2
import os

path = "Images"
images = []
for i in os.listdir(path):
    name, ext = os.path.splitext(i)
    #print(ext)
    if ext in [".png", ".jpeg", ".jpg", ".jfif", ".gif"]:
        file_name = path + "/" + i
        #print(file_name)
        images.append(file_name)
count = len(images)
#print(count)
frame = cv2.imread(images[0])
height, width, channels = frame.shape
size = (width, height)
print(size)
out = cv2.VideoWriter("Project.avi", cv2.VideoWriter_fourcc(*"DIVX"), 0.8, size)

for i in range(0, count - 1):
    frame = cv2.imread(images[i])
    out.write(frame)
out.release()
print("It is done")