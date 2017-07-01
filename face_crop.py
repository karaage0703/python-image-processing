# -*- coding: utf-8 -*-
import cv2
import numpy as np
import sys
import math
from math import sin, cos
from os import path

cascades_dir = path.normpath(path.join(cv2.__file__, '..', '..', '..', '..', 'share', 'OpenCV', 'haarcascades'))
max_size = 720

def detect(img, filename):
    cascade_f = cv2.CascadeClassifier(path.join(cascades_dir, 'haarcascade_frontalface_alt2.xml'))
    cascade_e = cv2.CascadeClassifier(path.join(cascades_dir, 'haarcascade_eye.xml'))
    # resize if learch image
    rows, cols, _ = img.shape
    if max(rows, cols) > max_size:
        l = max(rows, cols)
        img = cv2.resize(img, (cols * max_size / l, rows * max_size / l))
    rows, cols, _ = img.shape
    # create gray image for rotate
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    hypot = int(math.ceil(math.hypot(rows, cols)))
    frame = np.zeros((hypot, hypot), np.uint8)
    frame[(hypot - rows) * 0.5:(hypot + rows) * 0.5, (hypot - cols) * 0.5:(hypot + cols) * 0.5] = gray

    def translate(coord, deg):
        x, y = coord
        rad = math.radians(deg)
        return {
            'x': (  cos(rad) * x + sin(rad) * y - hypot * 0.5 * cos(rad) - hypot * 0.5 * sin(rad) + hypot * 0.5 - (hypot - cols) * 0.5) / float(cols) * 100.0,
            'y': (- sin(rad) * x + cos(rad) * y + hypot * 0.5 * sin(rad) - hypot * 0.5 * cos(rad) + hypot * 0.5 - (hypot - rows) * 0.5) / float(rows) * 100.0,
        }

    # filename numbering
    numb = 0
    for deg in range(-48, 49, 6):
        M = cv2.getRotationMatrix2D((hypot * 0.5, hypot * 0.5), deg, 1.0)
        rotated = cv2.warpAffine(frame, M, (hypot, hypot))
        faces = cascade_f.detectMultiScale(rotated, 1.08, 2)
        print deg, len(faces)
        for face in faces:
            x, y, w, h = face
            # eyes in face?
            y_offset = int(h * 0.1)
            roi = rotated[y + y_offset: y + h, x: x + w]
            eyes = cascade_e.detectMultiScale(roi, 1.05)
            eyes = filter(lambda e: (e[0] > w / 2 or e[0] + e[2] < w / 2) and e[1] + e[3] < h / 2, eyes)
            if len(eyes) == 2 and abs(eyes[0][0] - eyes[1][0]) > w / 4:
                score = math.atan2(abs(eyes[1][1] - eyes[0][1]), abs(eyes[1][0] - eyes[0][0]))
                if eyes[0][1] == eyes[1][1]:
                    score = 0.0
                if score < 0.15:
                    print("face_pos=" + str(face))
                    print("score=" + str(score))
                    print("numb=" + str(numb))
                    # cv2.rectangle(rotated, (x ,y), (x+w, x+h), (255,255,255), thickness=2)
                    # crop image
                    output_img = rotated[y:y+h, x:x+h]
                    # output file
                    cv2.imwrite(str("{0:02d}".format(numb)) + "_face_" + filename, output_img)
                    numb += 1


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

    output_img = detect(input_img, param[1])
