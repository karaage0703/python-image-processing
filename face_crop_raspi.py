# -*- coding: utf-8 -*-
import cv2
import sys
from os import path
import math
from math import sin, cos

# cascades_dir = path.normpath(path.join(cv2.__file__, '..', '..', '..', '..', 'share', 'OpenCV', 'haarcascades'))
cascades_dir ='/usr/share/opencv/haarcascades'

color = (255, 255, 255) # color of rectangle for face detection

def face_detect(file):
    image = cv2.imread(file)
    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cascade_f = cv2.CascadeClassifier(path.join(cascades_dir, 'haarcascade_frontalface_alt2.xml'))
    cascade_e = cv2.CascadeClassifier(path.join(cascades_dir, 'haarcascade_eye.xml'))

    # facerect = cascade_f.detectMultiScale(image_gray, scaleFactor=1.08, minNeighbors=1, minSize=(50, 50))
    facerect = cascade_f.detectMultiScale(image_gray, scaleFactor=1.08, minNeighbors=1, minSize=(200, 200))

    print "face rectangle"
    print facerect

    # test_image = image

    if len(facerect) > 0:
        # filename numbering
        numb = 0
        for rect in facerect:
            x, y, w, h = rect
            # eyes in face?
            roi = image_gray[y: y + h, x: x + w]
            # cv2.rectangle(test_image,(x,y),(x+w,y+h),(255,255,255),2)
            eyes = cascade_e.detectMultiScale(roi, scaleFactor=1.05, minSize=(20,20))
            # eyes = filter(lambda e: (e[0] > w / 2 or e[0] + e[2] < w / 2) and e[1] + e[3] < h / 2, eyes)
            # for (ex,ey,ew,eh) in eyes:
            #     print("rectangle")
            #     cv2.rectangle(test_image,(x+ex,y+ey),(x+ex+ew,y+ey+eh),(0,255,0),2)
            if len(eyes) > 1:
            # if len(eyes) == 2 and abs(eyes[0][0] - eyes[1][0]) > w / 4:
                image_face = image[y:y+h, x:x+h]
                cv2.imwrite(str("{0:02d}".format(numb)) + "_face_" + file, image_face)
                numb += 1

            # cv2.imwrite("00debug_"+file, test_image)

if __name__ == '__main__':
    param = sys.argv
    if (len(param) != 2):
        print ("Usage: $ python " + param[0] + " sample.jpg")
        quit()

    face_detect(param[1])
