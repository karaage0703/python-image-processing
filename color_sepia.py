# -*- coding: utf-8 -*-
import cv2
import sys

# extract color function
def color_sepia(src):
    img_bgr = cv2.split(src)
    # R=A, G=0.8xA, B=0.55xA
    dst = cv2.merge((img_bgr[0] * 0.55 , img_bgr[1] * 0.8, img_bgr[2] * 1.0))

    return dst

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

    # making mask using by extract color function
    output_img = color_sepia(input_img)

    cv2.imwrite("sepia_" + param[1], output_img)
