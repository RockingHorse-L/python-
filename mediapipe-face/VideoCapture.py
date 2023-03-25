"""
    人脸识别

    怎样才能算一张脸：
    眼睛、眉毛、鼻子、嘴巴......

    级联分类器
"""
import time

import cv2
from face import Face
from hand import Hand
class HandleCapture:
    def __init__(self):
        self.face = Face()
        self.hand = Hand()
        self.faceVideo = cv2.VideoCapture('test4.mp4')
        pass
    def videoDetect(self):
        faceVideo = self.faceVideo
        while faceVideo.isOpened():
            retval, image = faceVideo.read()
            if not retval:
                return
            prev_time = time.time()
            self.face.process(image)
            self.face.drawFPS(image, prev_time)
            cv2.imshow('image', image)
            key = cv2.waitKey(1)
            if key == ord('q'):
                break
        # 释放支援
        faceVideo.release()
        cv2.destroyAllWindows()
        pass
capture = HandleCapture()
capture.videoDetect()


