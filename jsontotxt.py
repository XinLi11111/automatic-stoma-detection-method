# coding: utf-8
from os import getcwd
import numpy as np
import os
import json
import glob
wd = getcwd()
classes = ["stoma"]  #Detection target name 
image_ids = glob.glob(r"[your image path]/*.jpg")           #jpg and json need to both in obj folder
print(image_ids)
def convert_annotation(image_id):
    jsonfile=open('%s.json' % (image_id))
    in_file = json.load(jsonfile)
    #print(in_file)
    width=in_file["imageWidth"]
    height=in_file["imageHeight"]
    size=[width,height]
    list_file = open('%s.txt'%(image_id.split('.')[0]), 'w')
    for i in range(0,len(in_file["shapes"])):
        object=in_file["shapes"][i]
        cls=object["label"]
        points=object["points"]
        dw = 1./(size[0])
        dh = 1./(size[1])
        min_x=min_y= np.inf
        max_x = max_y = 0
        for x, y in points:
            min_x = min(min_x, x)
            min_y = min(min_y, y)
            max_x = max(max_x, x)
            max_y = max(max_y, y)
        x=(min_x+max_x)/2.0
        print(x)
        y=(min_y+max_y)/2.0
        print(y)
        w=max_x-min_x
        h=max_y-min_y
        x = x*dw
        w = w*dw
        y = y*dh
        h = h*dh
        if cls not in classes:
            print("class not in classes")
            continue
        cls_id = classes.index(cls)
        b = (x, y, w, h)
        list_file.write(str(cls_id)+" "+" ".join([str(a) for a in b]) )
        list_file.write('\n')
    list_file.close()
    jsonfile.close()
for image_id in image_ids:
   # list_file.write('%s.jpg' % (image_id.split('.')[0]))
    convert_annotation(image_id.split('.')[0])
