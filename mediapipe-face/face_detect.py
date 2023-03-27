import cv2
import numpy as np

def drawLogo(img, logo, rect):
    logoGray = cv2.cvtColor(logo, cv2.COLOR_BGR2GRAY)
    retval, logoBinary = cv2.threshold(logoGray, 100, 255, cv2.THRESH_OTSU)
    image, contours, hierarchy = cv2.findContours(logoBinary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    mask = np.zeros(logoBinary.shape, dtype=np.uint8)
    cv2.drawContours(mask, contours, 1, color=(255, 255, 255), thickness=-1)
    loveX = rect[0]
    loveY = rect[1]
    loveW = rect[2]
    loveH = loveW
    smallLogo = cv2.resize(logo, dsize=(loveW, loveH))
    smallMask = cv2.resize(mask, dsize=(loveW, loveH))
    smallMaskH, smallMaskW = smallMask.shape[:2]
    a = np.array([255, 255, 255])
    for row in range(smallMaskH):
        for col in range(smallMaskW):
            if smallMask[row, col].all() == a.all():
                img[loveY + row - smallMaskH, loveX + col] = smallLogo[row, col]
            pass

    pass

