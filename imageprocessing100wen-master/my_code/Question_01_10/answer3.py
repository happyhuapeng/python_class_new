# _*_ encoding: utf-8 _*_
__author__ = 'nzb'
__date__ = '2020/6/6 17:47'
__doc__ = "二值化（Thresholding）"
import cv2
import numpy as np
# 计算： y={0 (if y<128 ) 255 (else)


def Grayscale(img):
    b = img[:,:,0].copy()
    g = img[:,:,1].copy()
    r = img[:,:,2].copy()

    ret = 0.2126 * r + 0.7152 * g + 0.0722 * b

    return ret.astype(np.uint8)


def Thresholding(img, th=128):
    img[img < th] = 0
    img[img >= th] = 250
    return img


img = cv2.imread("../../assets/imori.jpg").astype(np.float)
img2 = Grayscale(img)
img2 = Thresholding(img2)

# cv2.imshow("img", img)
cv2.imshow("ret", img2)

cv2.waitKey(0)
cv2.destroyAllWindows()
