# -*- coding: utf-8 -*-
import cv2

img1 = cv2.imread('image-1.jpg')
img2 = cv2.imread('image-2.jpg')
img3 = cv2.imread('image-3.jpg')
img4 = cv2.imread('image-4.jpg')

img5 = cv2.vconcat([img1, img2])
img6 = cv2.vconcat([img3, img4])
img7 = cv2.hconcat([img5, img6])
cv2.imwrite('output.jpg', img7)
