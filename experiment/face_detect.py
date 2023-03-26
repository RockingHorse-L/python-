import cv2
import numpy as np


class FaceDetect:
    def __init__(self):
        self.faceImg = None
        self.logoImg = cv2.imread('logo.jpg')
        self.classifier = cv2.CascadeClassifier()
        self.classifier.load('haarcascade_frontalface_alt.xml')
        pass

    def faceDetect(self, faceImg):
        self.faceImg = faceImg
        faceRect = self.classifier.detectMultiScale(faceImg)
        for x, y ,w ,h in faceRect:
            cv2.rectangle(faceImg, (x, y), (x+w, y+h), color=(255, 0, 255), thickness=2)
            rect = (x, y, w, h)
            self.drawLogo(self.logoImg, rect)
        pass

    def drawLogo(self, logo, rect):
        logoGray = cv2.cvtColor(logo, cv2.COLOR_BGR2GRAY)
        # 设置自动阈值 retVal:得到的阈值,dst:阈值化后的图像
        retval, dst = cv2.threshold(logoGray, 100, 255, cv2.THRESH_OTSU)
        # 会返回三个值
        # contours：一个包含了图像中所有轮廓的list对象。其中每一个独立的轮廓信息以边界点坐标（x,y）的形式储存在numpy数组中。
        # hierarchy：一个包含4个值的数组：[Next, Previous, First Child, Parent]。
            # Next：与当前轮廓处于同一层级的下一条轮廓
            # Previous：与当前轮廓处于同一层级的上一条轮廓
            # First Child：当前轮廓的第一条子轮廓
            # Parent：当前轮廓的父轮廓
        image, contours, hierarchy = cv2.findContours(dst, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        mask = np.zeros(dst.shape, dtype=np.uint8)

        # 绘制轮廓
        # 第一个参数是指明在哪幅图像上绘制轮廓；image为三通道才能显示轮廓
        # 第二个参数是轮廓本身，在Python中是一个list;
        # 第三个参数指定绘制轮廓list中的哪条轮廓，如果是 - 1，则绘制其中的所有轮廓。后面的参数很简单。其中thickness表明轮廓线的宽度，如果是 - 1（cv2.FILLED），则为填充模式。
        cv2.imshow('mask', mask)
        cv2.drawContours(mask, contours, 1, color=(255, 255, 255), thickness=-1)
        cv2.imshow('mask1', mask)
        ratio = logo.shape[0] / logo.shape[1]
        faceX = rect[0]
        faceY = rect[1]
        faceW = rect[2]
        faceH = int(faceW * ratio)
        smallLogo = cv2.resize(logo, dsize=(faceW, faceH))
        smallMask = cv2.resize(mask, dsize=(faceW, faceH))
        cv2.imshow('smallMask', smallMask)
        cv2.imshow('smollLogo', smallLogo)
        smallMaskH, smallMaskW = smallMask.shape[:2]
        for row in range(smallMaskH):
            for col in range(smallMaskW):
                if smallMask[row, col] == 255:
                    self.faceImg[faceY + row, faceX + col] = smallLogo[row, col]

        pass