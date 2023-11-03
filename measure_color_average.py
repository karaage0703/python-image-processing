# -*- coding: utf-8 -*-
import cv2
import sys
import numpy as np

if __name__ == '__main__':
    param = sys.argv
    if (len(param) != 3):
        print("Usage: $ python " + param[0] + " sample.jpg" "rgb or hsv")
        quit()

    # open image file
    bgr_img = cv2.imread(param[1])
    hsv_img = cv2.cvtColor(bgr_img, cv2.COLOR_BGR2HSV)

    average_bgr = [0,0,0]
    average_hsv = [0,0,0]

    # measure average of RGB color
    for i in range(3):
        extract_img = bgr_img[:,:,i]
        extract_img = extract_img[extract_img>0]
        average_bgr[i] = np.average(extract_img)

    for i in range(3):
        extract_img = hsv_img[:,:,i]
        extract_img = extract_img[extract_img>0]
        average_hsv[i] = np.average(extract_img)

    if param[2] == "rgb":
        # save RGB format(from BGR)
        print(str(average_bgr[2])+","+str(average_bgr[1])+","+str(average_bgr[0]))
    elif param[2] == "hsv":
        # save HSV format
        print(str(average_hsv[0])+","+str(average_hsv[1])+","+str(average_hsv[2]))
    else:
        print("Option is wrong. please select rgb or hsv")
