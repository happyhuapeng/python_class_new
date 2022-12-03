# _*_ encoding: utf-8 _*_
__author__ = 'nzb'
__date__ = '2020/6/6 18:37'
__doc__ = "大津二值化算法（Otsu's Method）"

# 计算： y={0 (if y<128 ) 255 (else)

import cv2
import numpy as np



def Grayscale(img):
    b = img[:,:,0].copy()
    g = img[:,:,1].copy()
    r = img[:,:,2].copy()

    ret = 0.2126 * r + 0.7152 * g + 0.0722 * b

    return ret.astype(np.uint8)


def otsu_binarization(img):
    max_sigma = 0
    max_t = 0
    H,W = img.shape

    for t in range(1, 256):
        # 类1
        v0 = ret[np.where(ret < t)]
        # 平均数
        m0 = np.mean(v0) if len(v0) > 0 else 0
        # 占比
        w0 = len(v0) / (H * W)

        v1 = ret[np.where(ret >= t)]
        m1 = np.mean(v1) if len(v1) > 0 else 0
        w1 = len(v1) / (H * W)

        sigma = w0 * w1 * ((m0 - m1) ** 2)

        if sigma > max_sigma:
            max_sigma = sigma
            max_t = t

    print("max_t", max_t)
    th = max_t
    ret[ret < th] = 0
    ret[ret >= th] = 255

    return ret


img = cv2.imread("../../assets/imori.jpg").astype(np.float)
ret = Grayscale(img)
ret = otsu_binarization(ret)

# cv2.imshow("img", img)
cv2.imshow("ret", ret)

cv2.waitKey(0)
cv2.destroyAllWindows()