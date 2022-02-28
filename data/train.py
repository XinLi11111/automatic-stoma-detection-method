# coding: utf-8
import os

paths = "/home/b/darknet/data/obj"    # the path of train set
f = open('train.txt', 'w')   # txt file to save the image path
filenames = os.listdir(paths)
files=[]
for file in filenames:
    if file.split('.')[-1]=='txt':
        continue
    else:
        files.append(file)
# 生成集
cnt=0
st=[1,2,3,4,5,6,7,8,9]
for filename in files:
        cnt+=1
        cnt=cnt%10
        if cnt not in st:
                cnt=0
                continue
        #print(cnt)
        out_path = "data/obj/" + filename  # The path to the test image folder is enclosed in quotation marks
        print(out_path)
        f.write(out_path + '\n')
f.close()

