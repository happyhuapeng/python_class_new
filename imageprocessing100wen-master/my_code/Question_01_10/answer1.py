# _*_ encoding: utf-8 _*_
__author__ = 'nzb'
__date__ = '2020/6/6 17:24'
__doc__ = "通道交换"

import cv2



def BGR2RGB(img):
    img_temp = img.copy()
    img_temp[:, :] = img_temp[:, :, (2, 1, 0)]

    return img_temp


img = cv2.imread("../../assets/imori.jpg")
img2 = BGR2RGB(img)

cv2.imshow("img", img)
cv2.imshow("ret", img2)

cv2.waitKey(0)
cv2.destroyAllWindows()

