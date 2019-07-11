import cv2
import numpy as np
import os
from collector import kmeans, getColors, createPalette

def concatenateImages(path, filename, newFilename):
    #load image
    img = cv2.imread(path + "\\" + filename)

    # create reduced color image
    reduced = kmeans(img)


    # extract colors from reduced color image
    colors = createPalette(getColors(reduced))

    # resize original image
    dim = (256,256)
    resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)

    # concatenate resized image and color palette
    cnct = np.concatenate((colors, resized), axis=1)

    #save image
    cv2.imwrite("img_" + filename, cnct)

def globber(path):
    count = 0
    print( os.listdir(path))
    for file in os.listdir(path):
        try:
            print(count)
            concatenateImages(path, file, str(count))
        except:
            print("didn't work")

        count = count + 1


path = "un-processed images 2"
globber(path)
