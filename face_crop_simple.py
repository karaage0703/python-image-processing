# -*- coding: utf-8 -*-
import cv2
import sys
from os import path
import math
from math import sin, cos

cascades_dir = path.normpath(path.join(cv2.__file__, '..', '..', '..', '..', 'share', 'OpenCV', 'haarcascades'))

color = (255, 255, 255) # color of rectangle for face detection

def face_detect(file):
    image = cv2.imread(file)
    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cascade_f = cv2.CascadeClassifier(path.join(cascades_dir, 'haarcascade_frontalface_alt2.xml'))
    cascade_e = cv2.CascadeClassifier(path.join(cascades_dir, 'haarcascade_eye.xml'))

    facerect = cascade_f.detectMultiScale(image_gray, scaleFactor=1.08, minNeighbors=1, minSize=(50, 50))

    print "face rectangle"
    print facerect

    if len(facerect) > 0:
        # filename numbering
        numb = 0
        for rect in facerect:
            x, y, w, h = rect
            # eyes in face?
            y_offset = int(h * 0.1)
            eye_area = image_gray[y + y_offset: y + h, x: x + w]
            eyes = cascade_e.detectMultiScale(eye_area, 1.05)
            eyes = filter(lambda e: (e[0] > w / 2 or e[0] + e[2] < w / 2) and e[1] + e[3] < h / 2, eyes)
            print(len(eyes))
            if len(eyes) > 0:
                image_face = image[y:y+h, x:x+h]
                cv2.imwrite(str("{0:02d}".format(numb)) + "_face_" + file, image_face)
                numb += 1

if __name__ == '__main__':
    param = sys.argv
    if (len(param) != 2):
        print ("Usage: $ python " + param[0] + " sample.jpg")
        quit()

    face_detect(param[1])
