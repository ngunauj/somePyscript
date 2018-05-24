#coding=utf-8
import os
import os.path
import xml.dom.minidom
import cv2


path = "/home/m7/Day0/train/train_images/"
files = os.listdir(path) 
s = []
h = {
    "others":(255, 255, 0),
    "unknown":(255, 0, 255),
    "none":(255, 255, 255),
    "xiaoxingche": (0, 0, 255),
}
for xmlFile in files:
    #print xmlFile
    continue_flag = False
    if not os.path.isdir(path + xmlFile):

        dom = xml.dom.minidom.parse(os.path.join(path, path + xmlFile))
        pretty_xml_as_string = dom.toprettyxml()
        root = dom.documentElement
        name = root.getElementsByTagName('filename')
        objs = root.getElementsByTagName('object')
        p = path + name[0].firstChild.data
        #for i in range(len(objs)):
        #    print objs[i].getElementsByTagName('name')[0].firstChild.data 
        img = cv2.imread(p)
        #print img
        bndbox = root.getElementsByTagName('bndbox')
        id = 0
        for box in bndbox:
            class_name = objs[id].getElementsByTagName('name')[0].firstChild.data
            x1_list = box.getElementsByTagName('xmin') 
            x1 = int(x1_list[0].childNodes[0].data)
            y1_list = box.getElementsByTagName('ymin')
            y1 = int(y1_list[0].childNodes[0].data)
            x2_list = box.getElementsByTagName('xmax')
            x2 = int(x2_list[0].childNodes[0].data)
            y2_list = box.getElementsByTagName('ymax')
            y2 = int(y2_list[0].childNodes[0].data)
            s.append([x1, y1, x2, y2])
            cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
            if class_name in h:
                cv2.putText(img, class_name, (x1, y1), cv2.FONT_HERSHEY_TRIPLEX,1, h[class_name], 1)
            else:
                cv2.putText(img, class_name, (x1, y1), cv2.FONT_HERSHEY_TRIPLEX,1, (0, 100, 100), 1)
            id += 1
        width, height = img.shape[:2]
        #cv2.imshow('figure ' + str(xmlFile), cv2.resize(img, (height // 2, width // 2)))
        if class_name == 'others':
            print xmlFile[:-4]
        #if class_name == 'others':
        cv2.imwrite("train_image_preprocessed/" + xmlFile[:-4] + ".jpg", img)
        #if cv2.waitKey(1) & 0xFF == ord('c'): continue_flag = True
        #if continue_flag == True : continue
        #cv2.waitKey(0)
        #if cv2.waitKey(1) & 0xFF == ord('q'): break
    #if cv2.waitKey(1) & 0xFF == ord('q'): break

        #保存修改到xml文件中
        #with open(os.path.join(path,xmlFile),'w') as fh:
        #    dom.writexml(fh)
        #    print('OK!')
for i in s:
    print i

