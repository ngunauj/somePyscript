import sys
import numpy as np 
import glob as gb
import os
import shutil
import cv2

def run(path):
  global num
  files = os.listdir(path)
  tmp = ''
  for file in files:
  	file_n = os.path.join(path, file)
  	if os.path.isdir(file_n):
  	  run(file_n)
  	else:
  	  name, ext = os.path.splitext(file_n)
  	  if ext == '.jpg':
  	  	List = name.split('_')
  	  	x, y, w, h = int(List[-5]), int(List[-4]), int(List[-3]), int(List[-2])
  	  	frame = cv2.imread(file_n, 1)
  	  	print x,y,w,h
  	  	#cv2.rectangle(frame, (x,y), (x+w, y+h), (0,0,255), 2)
  	  	cv2.rectangle(frame,(x,y),(x+w,y+h),(255,255,0),2)
  	  	frame = cv2.resize(frame, (800, 800))
  	  	cv2.imshow('frame',frame)
  	  	cv2.waitKey(0)
  	    #tmp = tmp + file_n + '\n'
  	    #print file_n
  	    #num = num + 1

'''
  f = open('pic_list.txt', 'a')
  f.write(tmp)
  f.close()
'''

if __name__ == '__main__':
  path = 'imposter_cad/'
  num = 0
  run(path) # gen mu lu
  print num