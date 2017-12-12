import sys
import numpy as np 
import glob as gb

def getPicPath(path):
  img_path = gb.glob(path+'/*.jpg')
  f = open('train2.txt', 'w')
  num = 0
  s = ""
  for path in img_path:
    s = s + path + '\n'
    num = num + 1
    #if num == 794:
    #  break
  f.write(s)
  f.close()
  print len(img_path)
  #print num
if __name__ == '__main__':
  path = sys.argv[1]
  getPicPath(path)
