# coding: utf-8
import os

paths = "/home/b/darknet/data/obj"
f = open('test.txt', 'w')   #
filenames = os.listdir(paths)
files=[]
for file in filenames:
    if file.split('.')[-1]=='txt':
        continue
    else:
        files.append(file)
cnt=0
st=[1,2,3,4,5,6,7,8,9]
for filename in files:
        cnt+=1
        cnt=cnt%10
        if cnt in st:
                continue
        #print(cnt)
        out_path = "data/obj/" + filename  
        print(out_path)
        f.write(out_path + '\n')
        cnt=0
f.close()

