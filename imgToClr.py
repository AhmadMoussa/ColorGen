import cv2
import numpy as np
from collector import kmeans

def getClrs(path):
    #load image
    img = cv2.imread(path)
    img = kmeans(img)
    data = img.reshape(-1,3)
    print(data.shape)
    diff_clrs = []
    init = 0
    for color in data:
        if init == 0:
            diff_clrs = np.asarray([color])
            init = 1
        else:
            if color not in diff_clrs:
                print("adding color")
                print(color.shape)
                print(diff_clrs.shape)
                diff_clrs = np.concatenate((diff_clrs, np.asarray([color])), axis = 0)

    return diff_clrs

path = "palette4.jpg"
clrs = getClrs(path)
print(clrs)

def checkClrs(clrs):
    height = 64
    width = 32
    init = 0
    for color in clrs:
        for i in range(width):
            if init == 0:
                data = np.array([color])
                print(data.shape)
                init = 1
            else:
                data = np.concatenate((data,np.array([color])), axis = 0)

    data = data.reshape(1,len(data),3)
    data2 = data
    for i in range(height):
        data = np.concatenate((data,data2), axis = 0)

    return(data)

check = checkClrs(clrs)
cv2.imshow("check",check)
cv2.waitKey(0); cv2.destroyAllWindows(); cv2.waitKey(1)
