# -*- coding: utf-8 -*-
import cv2
import sys
import numpy as np
# from matplotlib import pyplot as plt

def watershed(src):
    # Change color to gray scale
    gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)

    # Use the Otsu's binarization
    thresh,bin_img = cv2.threshold(gray,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
    # print(thresh)  # print threshold

    # Noise removal
    kernel = np.ones((3,3), np.uint8)
    opening = cv2.morphologyEx(bin_img,cv2.MORPH_OPEN,kernel,iterations = 2)

    # Sure background area
    sure_bg = cv2.dilate(opening,kernel,iterations=3)

    # Finding sure foreground area
    dist_transform = cv2.distanceTransform(opening,cv2.DIST_L2,5)
    ret, sure_fg = cv2.threshold(dist_transform,0.7*dist_transform.max(),255,0)

    # Finding unknown region
    sure_fg = np.uint8(sure_fg)
    unknown = cv2.subtract(sure_bg,sure_fg)

    # Marker labelling
    ret, markers = cv2.connectedComponents(sure_fg)

    # Add one to all labels so that sure background is not 0, but 1
    markers = markers+1

    # Now, mark the region of unknown with zero
    markers[unknown==255] = 0

    # Apply watershed
    markers = cv2.watershed(src,markers)
    src[markers == -1] = [255,0,0]

    # Check marker (If check markers, please import matplotlib)
    # plt.imshow(markers)
    # plt.show()

    # Check markers data
    # print(np.unique(markers,return_counts=True))

    return markers, src

if __name__ == '__main__':
    param = sys.argv
    if (len(param) != 2):
       print ("Usage: $ python " + param[0] + " sample.jpg")
       quit()

    # open image file
    try:
        input_img = cv2.imread(param[1])
    except:
        print ('faild to load %s' % param[1])
        quit()

    if input_img is None:
        print ('faild to load %s' % param[1])
        quit()

    markers, img = watershed(input_img)
    cv2.imwrite("watershed_markers_" + param[1], markers)
    cv2.imwrite("watershed_image_" + param[1], img)
