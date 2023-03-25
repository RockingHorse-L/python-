
import cv2
from hand import Hand


class VideoProcess:
    def __init__(self):
        self.hand = Hand()
        self.video = cv2.VideoCapture('test.mp4')
        pass

    def process(self):
        cap = self.video
        while cap.isOpened():
            # retval 是否读取到图像
            # image 就是读取的图像
            retval, image = cap.read()
            if not retval:
                print('can not read image')
                break
            # 1 表示图像水平翻转
            image = cv2.flip(image, 1)
            self.hand.handleImg(image)
            # 3、显示图像
            # 参数1:窗口名称
            # 参数2:显示的具体图像
            cv2.imshow('sy', image)
            # 如果数字是大于0,1000(1000ms---1s)
            # 如果是0，等待按键按下
            key = cv2.waitKey(25)
            if key == ord('q'):
                break
        # 释放资源
        cap.release()
        cv2.destroyAllWindows()

videoProcess = VideoProcess()
videoProcess.process()
