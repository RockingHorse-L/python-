"""
    人脸识别

    怎样才能算一张脸：
    眼睛、眉毛、鼻子、嘴巴......

    级联分类器
"""

import cv2
from hand import Hand
class HandleCapture:
    def __init__(self):
        self.hand = Hand()
        self.faceVideo = cv2.VideoCapture('test2.mp4')
        pass

    def videoDetect(self):
        faceVideo = self.faceVideo
        while True:
            retval, image = faceVideo.read()
            self.hand.process(image)
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


