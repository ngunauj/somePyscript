import cv2
import sys
import numpy as np

def run(path):
	imagelist = open(path).readlines()
	for oneline in imagelist:
		m_items = oneline.rstrip().split("\t")
		frame = cv2.imread(m_items[0], 1)
		#img = frame.copy()
		bags = list()
		bags.append([int(m_items[1]), int(m_items[2]), int(m_items[3]), int(m_items[4])])

		if len(bags) > 0:
			x, y, w, h = bags[0]
			cv2.rectangle(frame, (x,y), (x+w,y+h), (0, 255, 255), 2)
			frame = cv2.resize(frame, (frame.shape[1]/2, frame.shape[0]/2))
			print oneline
			cv2.imshow('1', frame)
			cv2.waitKey(0)

if __name__ == '__main__':
	path = sys.argv[1]
	run(path)
