# _*_ encoding: utf-8 _*_
__author__ = 'nzb'
__date__ = '2020/6/7 11:59'
__doc__ = 'HSV 变换'

import cv2
import numpy as np


def BGR2HSV(img):
    new_img = img.copy() / 255.

    # 返回一个与给定类型,形状相似的,全零的矩阵
    hsv = np.zeros_like(new_img, dtype=np.float32)

    max_v = np.max(new_img, axis=2).copy()


def HSV2BGR(img, hsv):
    pass


img = cv2.imread("../../assets/imori.jpg").astype(np.float32)

ret = BGR2HSV(img)
ret = otsu_binarization(ret)

# cv2.imshow("img", img)
cv2.imshow("ret", ret)

cv2.waitKey(0)
cv2.destroyAllWindows()