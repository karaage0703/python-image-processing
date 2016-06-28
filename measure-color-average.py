# -*- coding: utf-8 -*-
import cv2
import sys
import numpy as np

if __name__ == '__main__':
    param = sys.argv
    if (len(param) != 2):
        print ("Usage: $ python " + param[0] + " sample.jpg")
        quit()  
    # open image file
    input_img = cv2.imread(param[1])
    average_color = [0,0,0]
    # measure average of color
    for i in range(3):
        extract_img = input_img[:,:,i]
        extract_img = extract_img[extract_img>0]
        average_color[i] = np.average(extract_img)

    print(str(average_color[0]) + " " + str(average_color[1]) + " " + str(average_color[2]))
