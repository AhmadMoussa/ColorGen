import cv2
import numpy as np

def checkDimensions():
    img = cv2.imread("test1.jpg")
    rows = img.shape[1]
    cols = img.shape[0]
    print("Rows: ", rows, "Cols: ", cols)

    scale_percent = 60 # percent of original size
    width = int(img.shape[1] * scale_percent / 100)
    height = int(img.shape[0] * scale_percent / 100)
    dim = (64,64)
    # resize image
    resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
    print('Resized Dimensions : ',resized.shape)

    cv2.imshow("Resized image", resized)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    cv2.imwrite("testresized1.jpg",resized)

checkDimensions()
