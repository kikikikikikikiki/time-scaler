import numpy as np
from PIL import Image

#Takes the enhanced t/y images and converts them back into video frames

out_frames = 240
xpx = 160
ypx = 120

final = np.zeros((ypx,xpx,3), dtype="uint8")

for frame in range(240):
    for x in range(135):
        for y in range(120):
            for z in range(3):
                file_name = str("ennhancedRGBtimeframe") + str(x) + ".png"
                img = Image.open(file_name)
                img = np.array(img)
                final[y][x][z] = img[y][frame][z]

    result = Image.fromarray(final.astype(np.uint8)).convert('RGB')
    im1 = result.save("final"+str(frame)+".png") 


    

