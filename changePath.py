import sys
import numpy as np 
import glob as gb
import shutil
import os

def change(path):
  f = open(path, 'r')
  tmp = ''
  num = 0
  while True:
    line = f.readline().strip()
    if not line:
      print 'done'
      break
    prefix = '/media/guan/guan'
    num = num + 1
    subStr = line[13:]
    prefix = prefix + subStr
    prefix = prefix + '\n'

    tmp = tmp + prefix
  print num
  f.close()
  f = open('new_' + path, 'w')
  f.write(tmp)
  f.close()
if __name__ == '__main__':
  path = sys.argv[1]
  change(path)
