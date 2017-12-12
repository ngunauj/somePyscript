import sys
import numpy as np 
import glob as gb
import os

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
  	    tmp = tmp + file_n + '\n'
  	    print file_n
  	    num = num + 1
      
  f = open('pic_list.txt', 'a')
  f.write(tmp)
  f.close()

if __name__ == '__main__':
  path = sys.argv[1]
  num = 0
  run(path) # gen mu lu
  print num