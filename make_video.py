# encoding: UTF-8
import glob as gb
import cv2

img_path = gb.glob("out2.4/*.jpg")
 
videoWriter = cv2.VideoWriter('/home/guan/Desktop/out.mp4', cv2.VideoWriter_fourcc(*'MJPG'), 25, (640, 480))

for path in img_path:
    img  = cv2.imread(path) 
    img = cv2.resize(img, (640, 480))
    videoWriter.write(img)
videoWriter.release()
