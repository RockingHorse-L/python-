
import mediapipe as mp
import cv2
import numpy as np

class Hand:
    def __init__(self):
        mpHands = mp.solutions.hands
        self.hands = mpHands.Hands()
        self.leftLandmark = []
        self.img = None
        self.figureTopNum = [4, 8, 12, 16, 20]

    def handleImg(self, img):
        self.img = img
        self.drawPointsLine()
        # 改为len()
        if len(self.leftLandmark) == 0:
            return
        self.drawPointsNum(img)
        self.detectFigureNum()
        pass

    def drawPointsLine(self):
        img = self.img
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        result = self.hands.process(img_rgb)
        # 改为multi_hand_landmarks
        if not result.multi_hand_landmarks:
            return
        # 添加这一句
        for handnedess in result.multi_hand_landmarks:
            # hand_leftLandmark = result.multi_hand_landmarks[0]
            self.leftLandmark = handnedess.landmark
            #print(handnedess)
            print(handnedess.landmark)
            pointStyle = mp.solutions.drawing_utils.DrawingSpec(color=(0, 0, 255), thickness=2)
            lineStyle = mp.solutions.drawing_utils.DrawingSpec(color=(0, 0, 255), thickness=1)
            conn = mp.solutions.hands_connections
            mp.solutions.drawing_utils.draw_landmarks(img,
                                                      handnedess,
                                                      conn.HAND_CONNECTIONS,
                                                      pointStyle,
                                                      lineStyle
                                                      )
        pass

    # 绘制关键点的序号
    def drawPointsNum(self, img):
        imgH = img.shape[0]
        imgW = img.shape[1]
        for index, mark in enumerate(self.leftLandmark):
            # 改为整型
            x = int(mark.x * imgW)
            y = int(mark.y * imgH)
            cv2.putText(img, str(index), (x - 15, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.3, (0, 0, 255), 1)

    def detectFigureNum(self):
        topFigureNums = np.zeros((5,), np.uint8)
        for index, num in enumerate(self.figureTopNum):
            if index == 0:
                # 添加这两行 并且是mix_x减一 并且索引为0
                mark_top_X = self.indexCVPoint(num)[0]
                mark_mid_X = self.indexCVPoint(num - 1)[0]
                topFigureNums[index] = mark_top_X > mark_mid_X
                continue
            # 添加索引[1]
            mark_top_y = self.indexCVPoint(num)[1]
            mark_mid_y = self.indexCVPoint(num-2)[1]
            # 改为小于
            topFigureNums[index] = mark_top_y < mark_mid_y

        cnt = np.sum(topFigureNums)
        cv2.putText(self.img, str(cnt), (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, color=(0, 0, 255), thickness=2)

    def indexCVPoint(self, index):
        imgH = self.img.shape[0]
        imgW = self.img.shape[1]
        mark = self.leftLandmark[index]
        x = int(mark.x * imgW)
        y = int(mark.y * imgH)
        return x, y

