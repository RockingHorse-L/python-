import cv2
from face_detect import FaceDetect

class FaceCapture:
    def __init__(self):
        self.face = FaceDetect()
        self.video = cv2.VideoCapture(0)
        pass

    def videoCapture(self):
        faceVideo = self.video
        while faceVideo.isOpened():
            retval, img = faceVideo.read()
            if not retval:
                print('not open')
                break
            self.face.faceDetect(img)
            cv2.imshow('img', img)
            key = cv2.waitKey(1)
            if key == ord('q'):
                break
        self.video.release()
        cv2.destroyAllWindows()
        pass

faceDet = FaceCapture()
faceDet.videoCapture()