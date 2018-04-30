import cPickle as pickle
import numpy as np 
import matplotlib.pyplot as plt

np.set_printoptions(threshold=np.NaN) 
f1 = open('./faster/person_pr.pkl')
f2 = open('./faster+incep/person_pr.pkl')
f3 = open('./faster+lccnet/person_pr.pkl')
f4 = open('./faster+lccnet+incep/person_pr.pkl')

d1 = pickle.load(f1)
d2 = pickle.load(f2)
d3 = pickle.load(f3)
d4 = pickle.load(f4)

print d1['ap'], d2['ap'], d3['ap'], d4['ap']


plt.figure()

#plt.title('Precision/Recall Curve')

plt.xlabel("Recall")
plt.ylabel("Precision")

y1 = list(d1['prec'])
y2 = list(d2['prec'])
y3 = list(d3['prec'])
y4 = list(d4['prec'])


x1 = list(d1['rec'])
x2 = list(d2['rec'])
x3 = list(d3['rec'])
x4 = list(d4['rec'])

plt.plot(x1,y1, color ='blue', linewidth = 1.0, linestyle ='-',label="faster rcnn")  
plt.plot(x2,y2, color ='green',linewidth=1.0, linestyle='-', label='faster-rcnn+inception')  
plt.plot(x3,y3, color ='yellow', linewidth=1.0, linestyle='-',label='faster-rcnn+lccnet')  
plt.plot(x4,y4, color ='red', linewidth=1.0, linestyle='-',label='faster-rcnn+inception+lccnet')
'''
x = list(d1['rec'])
y = list(d1['prec'])
plt.plot(x, y,'g-')
'''
plt.legend(loc='upper right')
plt.savefig('compare-pr.jpg')



