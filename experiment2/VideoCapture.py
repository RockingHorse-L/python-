"""
    人脸识别

    怎样才能算一张脸：
    眼睛、眉毛、鼻子、嘴巴......

    级联分类器
"""

import cv2
from hands import Hand

class HandleCapture:
    def __init__(self):
        self.faceVideo = cv2.VideoCapture(0)
        self.hands = Hand()
        pass

    def videoDetect(self):
        faceVideo = self.faceVideo
        while faceVideo.isOpened():
            retval, image = faceVideo.read()
            if not retval:
                print('not open')
                break
            self.hands.process(image)
            #self.pose.process(image)
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


