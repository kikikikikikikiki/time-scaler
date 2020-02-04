from scipy import ndimage
import numpy as np
from skimage import measure
from PIL import Image
import math

#Separates the RGB channels from the time/y image
#sets a reference zero point at the start of the video(the first y line)
#finds the difference between zero and the rest of the image
#increases the difference value and applies it to the original image, wihint bounds of 0-255
#combines rgb channels together and exports enhanced image


tpx = 240
ypx = 120
frames = 160
tfr = np.zeros((ypx,tpx))
tfg = np.zeros((ypx,tpx))
tfb = np.zeros((ypx,tpx))

zeror = np.zeros((ypx))
zerog = np.zeros((ypx))
zerob = np.zeros((ypx))

diffr = np.zeros((ypx,tpx))
diffg = np.zeros((ypx,tpx))
diffb = np.zeros((ypx,tpx))

mixedr = np.zeros((ypx,tpx))
mixedg = np.zeros((ypx,tpx))
mixedb = np.zeros((ypx,tpx))

outputrgb = np.zeros((ypx,tpx, 3))

for frame in range(frames):
    for x in range(tpx):
        for y in range(ypx):
            for z in range(3):
                file_name = str("segment") + str(frame+137) + ".png"
                img = Image.open(file_name)
                img = np.array(img)
                
                if z == 0:
                    tfr[y][x] = img[y][x][0]
                    if x == 0:
                        zeror[y] = img[y][0][0]
                        
                if z == 1:
                    tfg[y][x] = img[y][x][1]
                    if x == 0:
                        zerog[y] = img[y][0][1]
                        
                if z == 2:
                    tfb[y][x] = img[y][x][2]
                    if x == 0:
                        zerob[y] = img[y][0][2]
    output = Image.fromarray(tfr.astype(np.uint8))
    im1 = output.save("tfr"+str(x)+".png")
    output = Image.fromarray(tfg.astype(np.uint8))
    im1 = output.save("tfg"+str(x)+".png")
    output = Image.fromarray(tfb.astype(np.uint8))
    im1 = output.save("tfb"+str(x)+".png")
    
    for x in range(tpx):
        for y in range(ypx):
            pre1r = tfr[y][x]
            pre2r = zeror[y]
            pre1g = tfg[y][x]
            pre2g = zerog[y]
            pre1b = tfb[y][x]
            pre2b = zerob[y]
            diffr[y][x] = pre1r - pre2r
            diffg[y][x] = pre1g - pre2g
            diffb[y][x] = pre1b - pre2b
    print(diffr)
    ##enhancer = diffr*2
    #enhanceg = diffg*2
    #enhanceb = diffb*2
    mixedr = diffr*2 + tfr
    mixedg = diffg*2 + tfg
    mixedb = diffb*2 + tfb
    """
    for x in range(tpx):
        for y in range(ypx):
            premixr = enhancer[y][x]+tfr[y][x]
            premixg = enhanceg[y][x]+tfg[y][x]
            premixb = enhanceb[y][x]+tfb[y][x]

            if premixr <= 255 and premixr >= 0:
                mixedr[y][x] = premixr
            if premixg <= 255 and premixg >= 0:
                mixedg[y][x] = premixg
            if premixb <= 255 and premixb >= 0:
                mixedb[y][x] = premixb
    """
    """print or just calculate?"""
    for x in range(tpx):
        for y in range(ypx):
            for z in range(3):
                if z == 0 and mixedr[y][x] <= 255 and mixedr[y][x] >= 0:
                    outputrgb[y][x][0] = mixedr[y][x]
                    
                    if mixedr[y][x] > 255:
                        outputrgb[y][x][0] = 255
                    elif mixedr[y][x] < 0:
                        outputrgb[y][x][0] = 0
                    
                if z == 1 and mixedg[y][x] <= 255 and mixedg[y][x] >= 0:
                    outputrgb[y][x][1] = mixedg[y][x]
                    
                    if mixedg[y][x] > 255:
                        outputrgb[y][x][1] = 255
                    elif mixedg[y][x] < 0:
                        outputrgb[y][x][1] = 0
                    
                if z == 2 and mixedb[y][x] <= 255 and mixedb[y][x] >= 0:
                    outputrgb[y][x][2] = mixedb[y][x]
                    
                    if mixedb[y][x] > 255:
                        outputrgb[y][x][2] = 255
                    elif mixedb[y][x] < 0:
                        outputrgb[y][x][2] = 0

    output = Image.fromarray(outputrgb.astype(np.uint8)).convert('RGB')
    im1 = output.save("ennhancedRGBtimeframe"+str(frame+137)+".png")



    

