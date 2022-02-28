# An-automatic-plant-leaf-stoma-detection-method-based-on-YOLOv4
In this project, users can train the network to detect the number and location of the stomata with the help of your labeled stomatal data or obtain the required stomatal test results with the help of existing weight files
# Requirements for Linux
The environment and packages that need to be downloaded are visible in https://github.com/AlexeyAB/darknet
# our data 
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.6302925.svg)](https://doi.org/10.5281/zenodo.6302925)
# An-automatic-plant-leaf-stoma-detection-method-based-on-YOLOv4
In this project, users can train the network to detect the number and location of the stomata with the help of your labeled stomatal data or obtain the required stomatal test results with the help of existing weight files
# Requirements for Linux
The environment and packages that need to be downloaded are visible in https://github.com/AlexeyAB/darknet
# data preparation 
After labeling with labelme software, use jsontotxt.py to convert the json file into a txt file

You can use the train.py and test.py to devide data to train set and test set and the address will in the train.txt and test.txt
# test the best weights trained in this study with your image
./darknet detector test data/obj.data cfg/yolov4-obj.cfg yolov4-obj_best.weights(detect one image)

./darknet detector map data/obj.data cfg/yolov4-obj.cfg backup/yolov4-obj_best.weights(detect and count the number of stomata)

./darknet detector map data/obj.data cfg/yolov4-obj.cfg backup/yolov4-obj_best.weights -thresh 0.65(detect in different thresh)

./darknet detector map data/obj.data cfg/yolov4-obj.cfg backup/yolov4-obj_best.weights -thresh -iou_thresh(detect in different iou)

./darknet detector test data/obj.data cfg/yolov4-obj.cfg backup/yolov4-obj_best.weights -i 0,1,2(detect in different GPU)
# Train the network with your data and the best weights trained in this study  
1.Create the obj folder under the data folder,Modify the number of detection categories in obj.data, the location of the folder where the train set, the test set, the category name, and the weights are saved 

2.The obj folder stores the dataset images and the label information of each image

3.The train weights will both in backup folder.

4.change the parameters in obj.cfg[based on your gpu,you can change the batch and subdivisions;based on your detection number,you can change the classes parameter;also,you should change the filter number based on the 3*(5+class number)]

5.change the Makefile,based on your GPU.

./darknet detector [train the location of the folder where the data is located(data/obj.data)]  [the location of the folder where the weights are located(cfg/yolov4-obj.cfg)] yolov4-obj_best.weights -map

6.test in your own trained weights

At the end of the training, you can use the best weights obtained from the above training for stomata detection and counting .

./darknet detector map data/obj.data cfg/yourobj.cfg backup/yourbest.weights(detect and count the number of stomata)

./darknet detector map ata/obj.data cfg/yourobj.cfg backup/yourbest.weights -thresh 0.65(detect in different thresh)

./darknet detector map data/obj.data cfg/yourobj.cfg backup/yourbest.weights -iou_thresh(detect in different iou)

./darknet detector test data/obj.data data/obj.data cfg/yourobj.cfg backup/yourbest.weights -i 0,1,2(detect in different GPU)
# data preparation 
After labeling with labelme software, use jsontotxt.py to convert the json file into a txt file

You can use the train.py and test.py to devide data to train set and test set and the address will in the train.txt and test.txt
# test the best weights trained in this study with your image
./darknet detector test data/obj.data cfg/yolov4-obj.cfg yolov4-obj_best.weights(detect one image)

./darknet detector map data/obj.data cfg/yolov4-obj.cfg backup/yolov4-obj_best.weights(detect and count the number of stomata)

./darknet detector map data/obj.data cfg/yolov4-obj.cfg backup/yolov4-obj_best.weights -thresh 0.65(detect in different thresh)

./darknet detector map data/obj.data cfg/yolov4-obj.cfg backup/yolov4-obj_best.weights -thresh -iou_thresh(detect in different iou)

./darknet detector test data/obj.data cfg/yolov4-obj.cfg backup/yolov4-obj_best.weights -i 0,1,2(detect in different GPU)
# Train the network with your data and the best weights trained in this study  
1.Create the obj folder under the data folder,Modify the number of detection categories in obj.data, the location of the folder where the train set, the test set, the category name, and the weights are saved 

2.The obj folder stores the dataset images and the label information of each image

3.The train weights will both in backup folder.

4.change the parameters in obj.cfg[based on your gpu,you can change the batch and subdivisions;based on your detection number,you can change the classes parameter;also,you should change the filter number based on the 3*(5+class number)]

5.change the Makefile,based on your GPU.

./darknet detector [train the location of the folder where the data is located(data/obj.data)]  [the location of the folder where the weights are located(cfg/yolov4-obj.cfg)] yolov4-obj_best.weights -map

6.test in your own trained weights

At the end of the training, you can use the best weights obtained from the above training for stomata detection and counting .

./darknet detector map data/obj.data cfg/yourobj.cfg backup/yourbest.weights(detect and count the number of stomata)

./darknet detector map ata/obj.data cfg/yourobj.cfg backup/yourbest.weights -thresh 0.65(detect in different thresh)

./darknet detector map data/obj.data cfg/yourobj.cfg backup/yourbest.weights -iou_thresh(detect in different iou)

./darknet detector test data/obj.data data/obj.data cfg/yourobj.cfg backup/yourbest.weights -i 0,1,2(detect in different GPU)
