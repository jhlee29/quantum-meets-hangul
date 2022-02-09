import os
import numpy as np
import pandas as pd
from PIL import Image

###path to images
image_path = "./hangulcharacters"

###filtering only jpg files
img_list = os.listdir(image_path)
img_list_jpg = [img for img in img_list if img.endswith(".jpg")]

#print("img_list_jpg: {}".format(img_list_jpg))

target = []
for i in range(len(img_list_jpg)):
    target.append(img_list_jpg[i].split("_")[0])

DF = pd.DataFrame(target)
DF.to_csv("data_target.csv")

#print(target)

###make an empty list
img_list_np = []

###image to array
for i in img_list_jpg:
    img = Image.open(image_path + "/" + i).convert("L") ###grayscale
    img_array = np.array(img)

    DF = pd.DataFrame(img_array)
    DF.to_csv("./data_sample/"+i.split(".")[0] + ".csv")
    
    #img_list_np.append(img_array)
    #print(i, "Done - Structure:", img_array.shape)
    #print(img_array.T.shape)

###save as npy
#np.save("dataset", img_np)
#np.savetxt("dataset_2D.csv", img_np, %d, delimiter=",")
#np.savetxt("./dataset_2D.txt", img_np)

print("Done")
