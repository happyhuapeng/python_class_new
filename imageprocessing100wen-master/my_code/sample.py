# _*_ encoding: utf-8 _*_

__author__ = 'nzb'
__date__ = '2020/6/6 16:39'

import cv2

img = cv2.imread("../assets/imori.jpg")
cv2.imshow("imori", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

img3 = img.copy()
H, W, C = img3.shape
img3[:H//2, :W//2] = img3[:H//2, :W//2, (2, 1, 0)]
cv2.imshow('', img3); cv2.waitKey(0)
