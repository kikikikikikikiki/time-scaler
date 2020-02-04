import numpy as np
from PIL import Image

#Takes a set of image frames from a video
#Creates an image showing of how each vertical line of pixel changes over time
#Time becomes the x axis...

#number of frames
tpx = 240

xpx = 160
ypx = 120

tf = np.zeros((ypx,tpx,3), dtype="uint8")

for x in range(160):
    for t in range(tpx):
        print(t)
        for y in range(ypx):
            for z in range(3):
                str_num = "00" + str(t+200)
                file_name = str("image-") + str_num[-3:] + ".png"
                img = Image.open(file_name)
                img = np.array(img)
                tf[y][t][z] = img[y][x][z]

    result = Image.fromarray(tf.astype(np.uint8)).convert('RGB')
    im1 = result.save("segment"+str(x)+".png") 

