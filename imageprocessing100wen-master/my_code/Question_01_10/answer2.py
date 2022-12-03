# _*_ encoding: utf-8 _*_
__author__ = 'nzb'
__date__ = '2020/6/6 17:32'
__doc__ = "灰度化"

import cv2
import numpy as np
# 计算： Y = 0.2126\ R + 0.7152\ G + 0.0722\ B


def Grayscale(img):
    b = img[:,:,0].copy()
    g = img[:,:,1].copy()
    r = img[:,:,2].copy()

    ret = 0.2126 * r + 0.7152 * g + 0.0722 * b

    return ret.astype(np.uint8)


img = cv2.imread("../../assets/imori.jpg").astype(np.float)
img2 = Grayscale(img)

# cv2.imshow("img", img)
cv2.imshow("ret", img2)

cv2.waitKey(0)
cv2.destroyAllWindows()