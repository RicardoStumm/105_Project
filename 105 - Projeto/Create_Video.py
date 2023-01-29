import os
import cv2


path = "Imagens"

imagens = []

for file in os.listdir(path):
    name, ext = os.path.splitext(file)

    if ext in ['.gif', '.png', '.jpg', '.jpeg', '.jfif']:
        file_name = path+"/"+file

        # print(file_name)

        imagens.append(file_name)

count = len(imagens)

frame = cv2.imread(imagens[0])

height, width, channels = frame.shape

size = (width, height)

out = cv2.VideoWriter('video.mp4', cv2.VideoWriter_fourcc(*'DIVX'), 0.8, size)

for i in range(0, count-1):
    frame = cv2.imread(imagens[i])
    out.write(frame)
out.release()
print('concluido')
