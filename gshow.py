# coding=utf-8
import os
import os.path
import xml.dom.minidom
import cv2
import shutil
path = "/home/guan/dataSet/vehicle/Annotations/"
# new_path = "/home/guan/dataSet/vehicle/Annotations2/"
# for xml in open("trainval.txt"):
#     name = xml.strip()
#     shutil.copy(path+name+'.xml', new_path)

files = os.listdir(path)
s = []
h = {
    "vehicle":(255, 255, 0),
    "car":(255, 0, 255),
    "van":(255, 255, 255),
    "bus": (0, 0, 255),
}
usefulClass = ['car', 'van', 'bus', 'vehicle']
for xmlFile in files:
    if not os.path.isdir(path + xmlFile):
        dom = xml.dom.minidom.parse(os.path.join(path, path + xmlFile))
        pretty_xml_as_string = dom.toprettyxml()
        root = dom.documentElement
        name = root.getElementsByTagName('filename')
        objs = root.getElementsByTagName('object')
        pjpg = '/home/guan/dataSet/vehicle/JPEGImages/' + name[0].firstChild.data
        print(pjpg)
        img = cv2.imread(pjpg)
        for obj in objs:
            class_name = obj.getElementsByTagName('name')[0].firstChild.data
            bndbox = obj.getElementsByTagName('bndbox')
            id = 0
            for box in bndbox:
                x1_list = box.getElementsByTagName('xmin') 
                x1 = int(float(x1_list[0].childNodes[0].data))
                y1_list = box.getElementsByTagName('ymin')
                y1 = int(float(y1_list[0].childNodes[0].data))
                x2_list = box.getElementsByTagName('xmax')
                x2 = int(float(x2_list[0].childNodes[0].data))
                y2_list = box.getElementsByTagName('ymax')
                y2 = int(float(y2_list[0].childNodes[0].data))
                s.append([x1, y1, x2, y2])
                cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
                print(class_name)
                if class_name in usefulClass:
                    obj.getElementsByTagName('name')[0].firstChild.data = 'vehicle'
                    # cv2.putText(img, class_name, (x1, y1), cv2.FONT_HERSHEY_TRIPLEX,1, h[class_name], 1)
                else:
                    obj.getElementsByTagName('name')[0].firstChild.data = 'others'
                    # cv2.putText(img, class_name, (x1, y1), cv2.FONT_HERSHEY_TRIPLEX,1, (0, 100, 100), 1)

        with open(os.path.join('/home/guan/dataSet/vehicle/Annotations_vehicle/', xmlFile), 'w') as fh:
            dom.writexml(fh)
            print('OK!')     

