import sys
import glob as gb
import os

def run(path):
  files = os.listdir(path)
  pre = '/ssd/guan/tiny-cls/train/'
  for x in files:
    path = pre + x
    if x[:3] == 'dog':
      cls = 0
    else:
      cls = 1
    with open('train_list.txt', 'a+') as f:
      f.write(path + ' ' + str(cls) + '\n')

if __name__ == '__main__':
  path = sys.argv[1]
  num = 0
  run(path) # gen mu lu
  print num
