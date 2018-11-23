import sys
import numpy as np 
import glob as gb
import shutil
with open('f_lidar.txt', 'r') as f:
	y = [x.strip() for x in f.readlines()]
for i in y:
	shutil.copy(i, '/media/mmt/data/dataset/mmt_lidar/100lidar')
