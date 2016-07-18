# -*- coding: utf-8 -*-
import cv2
import sys
cascade_path = "./haarcascade_frontalface_alt.xml"

color = (255, 255, 255) # color of rectangle for face detection

def face_detect(file):
    image = cv2.imread(file)
    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cascade = cv2.CascadeClassifier(cascade_path)
    facerect = cascade.detectMultiScale(image_gray, scaleFactor=1.1, minNeighbors=1, minSize=(1, 1))

    print "face rectangle"
    print facerect

    if len(facerect) > 0:
        for rect in facerect:
            cv2.rectangle(image, tuple(rect[0:2]),tuple(rect[0:2]+rect[2:4]), color, thickness=2)

    return image

if __name__ == '__main__':
    param = sys.argv
    if (len(param) != 2):
        print ("Usage: $ python " + param[0] + " sample.jpg")
        quit()  

    output_img = face_detect(param[1])
    cv2.imwrite('facedetect_' + param[1], output_img)
