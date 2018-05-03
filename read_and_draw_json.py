import numpy as np
import matplotlib.pyplot as plt
import json

f = open("E:\\5.1\\valid_video_00_gt.json", encoding='utf-8')
arr = json.load(f)
dic = arr['frame_data']
X = []
VX = []
Box = []
for x in dic:
    X.append(x['x'])
    VX.append(x['vx'])
    xmin,ymin,xmax,ymax = x['ref_bbox']['left'],x['ref_bbox']['top'],x['ref_bbox']['right'],x['ref_bbox']['bot']
    Box.append([xmin,ymin,xmax,ymax])
                      
plt.plot(range(len(X)), X, '-')
print ((X[110]), (X[111]), (X[109]))

for i in Box:
    print (i)
