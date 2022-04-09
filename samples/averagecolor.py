import cv2
import numpy as np

import pandas as pd
src_img = cv2.imread('C:\\Users\\farha\\OneDrive\\Pictures\\fruits.png')
average_color_row = np.average(src_img, axis=0)
average_color = np.average(average_color_row, axis=0)
print(average_color)

d_img = np.ones((312,312,3), dtype=np.uint8)
d_img[:,:] = average_color

cv2.imshow('C:\\Users\\farha\\OneDrive\\Pictures\\fruits.png',src_img)
cv2.imshow('Average Color',d_img)
cv2.waitKey(0)

name_dict = {
     'Colors': ['red','green','blue'],
     'RGB values': [average_color[0], average_color[1], average_color[2]],
 }


df = pd.DataFrame(name_dict)

df.to_csv('average color.csv')

