import cv2
import numpy as np
from math import ceil

from collector import kmeans, getColors, createPalette

path = "gogh.jpg"
img = cv2.imread(path)
reduced = kmeans(img)
cv2.imshow("Reduced",reduced)
cv2.waitKey(0); cv2.destroyAllWindows(); cv2.waitKey(1)
colors = getColors(reduced)
for key in colors.getKeys():
    print("Color:", key, "Percentage", colors.getValue(key))

cv2.imwrite("palette4.jpg",createPalette(colors))
