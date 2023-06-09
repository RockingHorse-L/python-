"""
    人脸识别

    怎样才能算一张脸：
    眼睛、眉毛、鼻子、嘴巴......

    级联分类器
"""

import cv2
from pose import Pose
class HandleCapture:
    def __init__(self):
        self.pose = Pose()
        self.faceVideo = cv2.VideoCapture('me.mp4')
        pass

    def videoDetect(self):
        faceVideo = self.faceVideo
        while True:
            retval, image = faceVideo.read()
            self.pose.process(image)
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


