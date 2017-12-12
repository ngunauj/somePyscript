import sys
import numpy as np
import glob as gb
import shutil
import os

def run(pathin, pathout):
  f = open(pathin, 'r')
  tmp = ''
  num = 0
  while True:
    line = f.readline().strip()
    if not line:
      break
    num = num + 1
    List = line.split('\t')
    if os.path.isfile(List[0]):
      tmp = tmp + line + '\n'
    else:
      print line
    if num % 1000 == 0:
       print num
  f.close()
  f = open(pathout, 'w')
  f.write(tmp)
  f.close()

if __name__ == '__main__':
  pathin = sys.argv[1]
  pathout = sys.argv[2]
  run(pathin, pathout)
