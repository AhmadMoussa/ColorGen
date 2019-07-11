#source == https://stackoverflow.com/questions/34734379/is-there-a-formula-to-determine-overall-color-given-bgr-values-opencv-and-c/34734939#34734939
import cv2
import numpy as np
from math import ceil

def kmeans(img):
    K = 5
    rows = img.shape[1]
    cols = img.shape[0]
    n = img.shape[0] * img.shape[1]
    data = img.reshape(-1,3)
    data = np.float32(data)

    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
    center,labels,colors = cv2.kmeans(data, K, None, criteria,  10, cv2.KMEANS_PP_CENTERS)

    for i in range(0,n):
        data[i][0] = colors[labels[i], 0]
        data[i][1] = colors[labels[i], 1]
        data[i][2] = colors[labels[i], 2]

    reduced = data.reshape(cols, rows, 3)
    reduced = np.uint8(reduced)

    return reduced


class ColorDict():
    def __init__(self):
        self.colors = dict()

    def add(self, key, value):
        self.colors[key] = value

    def getKey(color):
        return self.colors[color]

    def updateKey(self, key, value):
        self.colors[key] = self.colors[key] + value

    def getValue(self, key):
        return self.colors[key]

    def getKeys(self):
        return self.colors.keys()

def getPercentage(count, total):
    return count/(total)*100

def getColors(img):
    data = img.reshape(-1,3)
    percentage = 1/len(data)
    colors = ColorDict()
    for color in enumerate(data):
        color = list(color[1])
        color = tuple(color)
        if color not in colors.getKeys():
            colors.add(color, percentage)
        else:
            colors.updateKey(color, percentage)

    return colors

def createPalette(colors):
    data = []
    init = 0
    height = 256
    fix_width = 256
    for color in colors.getKeys():
        width = ceil(colors.getValue(color) * fix_width)

        for i in range(width):
            if init == 0:
                data = np.array([color])
                init = 1
            else:
                data = np.concatenate((data,np.array([color])), axis = 0)

    data = data.reshape(1,len(data),3)
    data2 = data
    for i in range(height - 1):
        data = np.concatenate((data,data2), axis = 0)

    return(data)

'''
path = "3.jpg"
img = cv2.imread(path)
reduced = kmeans(img)
cv2.imshow("Reduced",reduced)
cv2.waitKey(0); cv2.destroyAllWindows(); cv2.waitKey(1)
colors = getColors(reduced)
for key in colors.getKeys():
    print("Color:", key, "Percentage", colors.getValue(key))

cv2.imwrite("palette4.jpg",createPalette(colors))
'''
