import sys
import os
import numpy as np 
import glob as gb

def makeDirlist(input_dir, out_file):
  root_path = os.getcwd() + '/'
  all_file = gb.glob(root_path + input_dir+'/*.txt')
  all_file.sort()
  num = 0
  if os.path.exists(root_path + out_file):
    with open(out_file, 'w') as f:
      f.truncate()
    print 1
  for afile in all_file:
    s = afile + '\n'
    with open(out_file, 'a+') as f:
      f.write(s)
    num = num + 1
    print num
if __name__ == '__main__':
  dir_in = sys.argv[1]
  file_out = sys.argv[2]
  if len(sys.argv) == 3:
    makeDirlist(dir_in, file_out)
#usage: python makelist.py label_3balanced label_3balanced.txt
#fast!!
