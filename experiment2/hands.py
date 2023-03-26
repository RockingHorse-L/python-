import cv2
import mediapipe as mp

class Hand:
    def __init__(self):
        # 1、加载模型
        mpHands = mp.solutions.hands
        self.hands = mpHands.Hands()
        self.leftLandmark = []
        self.img = None

        pass


    # 拿来调用函数
    def process(self, img):
        self.img = img
        self.drawLineStyle()
        if len(self.leftLandmark) == 0:
            return
        self.drawPointNum()
        pass

    # 给手指画线
    def drawLineStyle(self):
        img = self.img
        # 2、转为RGB
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        # 3、保存手部的一些数据
        result = self.hands.process(imgRGB)
        if not result.multi_hand_landmarks:
            return
        # 4、绘制关键点和线
        pointStyle = mp.solutions.drawing_utils.DrawingSpec(color=(255, 255, 0),thickness=2)
        lineStyle = mp.solutions.drawing_utils.DrawingSpec(color=(255, 255, 0), thickness=2)
        # 5、关键点连线
        cnn = mp.solutions.hands_connections
        # 6、保存左手关键点坐标
        landmarks = result.multi_hand_landmarks[0]
        print(f'landmark:{landmarks}')
        self.leftLandmark = landmarks.landmark
        # 7、绘制
        mp.solutions.drawing_utils.draw_landmarks(
            img,
            landmarks,
            cnn.HAND_CONNECTIONS,
            pointStyle,
            lineStyle
        )
        pass

    # 绘制关键点
    def drawPointNum(self):
        lanmark = self.leftLandmark
        for idx, lm in enumerate(lanmark):
            print(f'idx:{idx}')
            print(f'lm:{lm}')
            x, y = self.indexCvPoint(idx)
            cv2.putText(
                self.img,
                str(idx),
                org=(x -15, y - 15),
                fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                fontScale=0.4,
                color=(255, 0, 255),
                thickness=1
            )
        pass

    # 显示信息
    def showInfo(self):
        pass



    # 通过索引将关键点转换到对应的屏幕坐标
    def indexCvPoint(self, idx):
        landmark = self.leftLandmark
        imgH, imgW = self.img.shape[:2]
        lm = landmark[idx]
        print(f'indexCvpoint:{lm}')
        x = int(lm.x * imgW)
        y = int(lm.y * imgH)
        return x, y


    # 数字识别
    def gestureFigure(self):
        pass
