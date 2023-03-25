from time import sleep
import cv2
import mediapipe as mp

class Grade:
    def __init__(self):
        self.grade = 0
        self.flag = False
        self.times = 3
        self.countDownTime = 6

    def count(self,img,  angle):
        if angle < 25 and self.flag == False:
            print(f'{angle}')
            self.grade += 1
            self.flag = True
        if angle > 80 and self.flag == True:
            self.flag = False
        cv2.putText(img,
                        str(f'count:{self.grade}'),
                        org=(50, 200),
                        fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                        fontScale=2,
                        color=(208, 224, 64),
                        thickness=4)

    def StartCountdown(self, img):
        # 开始倒计时3秒后显示
        if self.times == -1:
            cv2.putText(img,
                        str('Ready Go!'),
                        org=(50, 450),
                        fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                        fontScale=4,
                        color=(108, 224, 64),
                        thickness=17)
            self.times = -2
        # 过程倒计时10秒
        if self.countDownTime >= 0 and self.times == -2:
            #倒计时
            cv2.putText(img,
                        str(f'countdown:{self.countDownTime}'),
                        org=(50, 100),
                        fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                        fontScale=2,
                        color=(208, 224, 64),
                        thickness=2)
            sleep(1)
            self.countDownTime -= 1
        if self.times >= 0:
            # 开始倒计时3秒
            cv2.putText(img,
                        str(self.times),
                        org=(300, 450),
                        fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                        fontScale=4,
                        color=(208, 224, 64),
                        thickness=17)
            sleep(1)
            self.times -= 1

    #def Countdown(self, img):


    def endFlag(self, img):
        cv2.putText(img,
                    str('Game over!'),
                    org=(50, 300),
                    fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                    fontScale=4,
                    color=(208, 224, 64),
                    thickness=15)


