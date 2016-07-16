#!/usr/bin/env python
# -*- coding: utf-8 -*-
import cv2
cascade_path = "./haarcascade_frontalface_alt.xml"
image_path = "face-2.jpg"

color = (255, 255, 255) # color of rectangle for face detection

cam = cv2.VideoCapture(0)
count=0

while True:
    ret, capture = cam.read()
    if not ret:
        print('error')
        break
    count += 1
    if count > 1:
        image = capture.copy()
        image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        cascade = cv2.CascadeClassifier(cascade_path)
        facerect = cascade.detectMultiScale(image_gray, scaleFactor=1.1, minNeighbors=1, minSize=(1, 1))

        if len(facerect) > 0:
            for rect in facerect:
                cv2.rectangle(image, tuple(rect[0:2]),tuple(rect[0:2]+rect[2:4]), color, thickness=2)

        count=0
        cv2.imshow('face detector', image)

cam.release()
cv2.destroyAllWindows()

