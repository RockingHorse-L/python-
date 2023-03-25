"""
    当前我们使用mediapipe的解决方案
    solutions pose /hand/ face /selfie_segmentation

    大体步骤：
            1、加载模型
                mpHands = mp.solutions.hands
                self.hands = mpHands.Hands()
            2、将图片转为RGB
                imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            3、保存返回的手部的各种数据
                result = self.hands.process(imgRGB)
            4、绘制关键点
                 mp.solutions.drawing_utils.draw_landmarks（）
            5、精准定位关键点的坐标
            7、绘制
"""
import math
import cv2
import mediapipe as mp
import numpy as np
import hands_type
import face_detect
from cutdown import CutDown

class Hand:
    def __init__(self):
        # 1、加载模型
        self.loveLogo = cv2.imread('love.jpg')
        mpHands = mp.solutions.hands
        self.hands = mpHands.Hands()
        self.img = None
        #self.result = None
        # 保存左手关键点
        self.leftLandmark = []
        self.rightLandmark = []
        # 初始化倒计时
        self.cutdown = CutDown(CUT_DOWN = 10)
        # 存储左右手
        self.mulHands = []
        self.leftPoint = ()
        self.rightPoint = ()
        self.pts = []
        pass

    def process(self, img):
        self.img = img
        self.drawLineStyle()
        if len(self.leftLandmark) == 0 and len(self.rightLandmark) == 0:
            return
        for handType in self.mulHands:
            isRight = handType == hands_type.RIGHT_HAND_TYPE
            self.drawPointNum(isRight)
            self.gestureFigure(isRight)
        self.drawLove()
        self.cutDownTime()
        pass

    def cutDownTime(self):
        info = self.cutdown.process()[0]
        self.showInfo(info, None, (500, 200), (255, 255, 0))

    def drawLineStyle(self):
        """
        手部关键点识别处理
        :param img:
        :return:
        """
        img = self.img
        # 1、加载模型
        # mpHands = mp.solutions.hands
        # hands = mpHands.Hands()

        # 2、转换为RGB
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        # 3、返回的是手部的各种数据，可以点process进去看返回的数据，再保存给变量result
        self.result = self.hands.process(imgRGB)

        # 4、如果没有看见手部就不绘制
        if not self.result.multi_hand_landmarks:
            return
        """
            两只手开始了
        """
        # 1、存储当前有几只手
        mulHands = []
        self.mulHands = mulHands
         # 2、双重循环的目的就是找出lable，因为里面是左右手的类型
        for handedness in self.result.multi_handedness:
            for classification in handedness.classification:
                if classification.label not in mulHands:
                    mulHands.append(classification.label)
                    pass
        # 3、mulHands里面存放了左右手特征,现在就可以来判断了
        for idx, handType in enumerate(mulHands):
            isRight = handType == hands_type.RIGHT_HAND_TYPE
            if isRight:
                # 5、绘制关键点和线的style
                pointStyle = mp.solutions.drawing_utils.DrawingSpec(color=(255, 255, 0), thickness=2)
                lineStyle = mp.solutions.drawing_utils.DrawingSpec(color=(255, 255, 0), thickness=2)

                # 6、关键点的连接点
                conn = mp.solutions.hands_connections

                # 7、将左手部的关键点坐标保存给hand_leftLandmarks
                hand_Landmark = self.result.multi_hand_landmarks[idx]


                # 8、因为在hand_leftLandmarks下面一层才是landemark关键点 所以要多点一个landmark
                self.rightLandmark = hand_Landmark.landmark

                # 9、绘制
                mp.solutions.drawing_utils.draw_landmarks(
                    img,
                    #表示左手 ，result.multi_hand_landmarks[0]表示右手
                    hand_Landmark,
                    conn.HAND_CONNECTIONS,
                    pointStyle,
                    lineStyle
                )
            else:
                # 5、绘制关键点和线的style
                pointStyle = mp.solutions.drawing_utils.DrawingSpec(color=(0, 255, 255), thickness=2)
                lineStyle = mp.solutions.drawing_utils.DrawingSpec(color=(0, 255, 255), thickness=2)

                # 6、关键点的连接点
                conn = mp.solutions.hands_connections

                # 7、将左手部的关键点坐标保存给hand_leftLandmarks
                hand_Landmark = self.result.multi_hand_landmarks[idx]

                # 8、因为在hand_leftLandmarks下面一层才是landemark关键点 所以要多点一个landmark
                self.leftLandmark = hand_Landmark.landmark

                # 9、绘制
                mp.solutions.drawing_utils.draw_landmarks(
                    img,
                    # 表示左手 ，result.multi_hand_landmarks[0]表示右手
                    hand_Landmark,
                    conn.HAND_CONNECTIONS,
                    pointStyle,
                    lineStyle
                )
        pass

    # def twoHands(self, result):
    #     """
    #         判断两只手了！
    #         handedness.classification,这里面存放了三个值
    #                 {
    #                  index:1
    #                  score:0.9994548754554
    #                   lable:"Right"
    #                   }
    #            """
    #     # 1、存储当前有几只手
    #     mulHands = []
    #     self.mulHands = mulHands
    #     # 2、双重循环的目的就是找出lable，因为里面是左右手的类型
    #     for handedness in result.multi_handedness:
    #         for classification in handedness.classification:
    #             if classification.lable not in mulHands:
    #                 mulHands.append(classification.lable)
    #             pass
    #
    #     # 3、mulHands里面存放了左右手特征,现在就可以来判断了
    #     for idx, handType in enumerate(mulHands):
    #         isRight = handType == hands_type.RIGHT_HAND_TYPE
    #         if isRight:
    #             self.drawLineStyle(idx, (255, 255, 0))
    #         else:
    #             self.drawLineStyle(idx, (0, 255, 255))

    def gestureFigure(self, isRight):
        """
        手势数字识别
        当前除大拇指外
        使用指尖point8_y坐标 < point6_y 没有弯曲
        ....
        :return:
        """
        # 方式一
        # count = 0
        # point8_y = self.indexCvPoint(8)[1]
        # point6_y = self.indexCvPoint(6)[1]
        # point12_y = self.indexCvPoint(12)[1]
        # point10_y = self.indexCvPoint(10)[1]
        # point16_y = self.indexCvPoint(16)[1]
        # point14_y = self.indexCvPoint(14)[1]
        # point20_y = self.indexCvPoint(20)[1]
        # point18_y = self.indexCvPoint(18)[1]
        # if point8_y < point6_y:
        #     count += 1
        #     print('食指未弯曲')
        #     if point12_y < point10_y:
        #         count += 1
        #         print('中指未弯曲')
        #         if point16_y < point14_y:
        #             count += 1
        #             print('无名指未弯曲')
        #             if point20_y < point18_y:
        #                 count += 1
        #                 print('小指未弯曲')
        # cv2.putText(self.img,
        #             str(count),
        #             org=(100, 100),
        #             fontFace=cv2.FONT_HERSHEY_SIMPLEX,
        #             fontScale=2,
        #             color=(255, 255, 0),
        #             thickness=1
        #             )
        # 手指顶点
        topFigureNums = [4, 8, 12, 16, 20]
        figureStatus = np.zeros((5,), dtype=np.uint8)
        for idx, num in enumerate(topFigureNums):
            if idx == 0:
                topX = self.indexCvPoint(num, isRight)[0]
                midX = self.indexCvPoint(num - 2, isRight)[0]
                if isRight:
                    figureStatus[idx] = topX < midX
                    self.rightPoint = self.indexCvPoint(4, isRight)
                else:
                    figureStatus[idx] = topX > midX
                    self.leftPoint = self.indexCvPoint(8, isRight)
                    self.pts.append(self.leftPoint)
                continue

            topY = self.indexCvPoint(num, isRight)[1]
            midY = self.indexCvPoint(num - 2, isRight)[1]
            figureStatus[idx] = topY < midY
        #print(f'11111:{figureStatus}')
        # if topY < midY:
        # print('没有弯曲')
        pts_np = np.array(self.pts)
        total = np.sum(figureStatus)
        print(self.pts)
        self.drawline(pts_np)
        if isRight:
            self.showInfo(total,isRight, (500, 100), (255, 255, 0))
        else:
            self.showInfo(total, isRight,(200, 100), (0, 255, 255))
        pass

    def showInfo(self, total, isRight, org , color ):
        if isRight:
            cv2.putText(self.img,
                        str(total),
                        org=org,
                        fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                        fontScale=2,
                        color=color,
                        thickness=1
                        )
        else:
            cv2.putText(self.img,
                        str(total),
                        org=org,
                        fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                        fontScale=2,
                        color=color,
                        thickness=1
                        )

    def drawPointNum(self, isRight = True):
        """
        绘制关键点的序号
        :return:
        """
        # 遍历关键点进行绘制
        if isRight:
            landmark = self.rightLandmark
            color = (255, 255, 0)
        else:
            landmark = self.leftLandmark
            color = (0, 255, 255)
        for idx, lm in enumerate(landmark):
            x, y = self.indexCvPoint(idx, isRight)
            cv2.putText(self.img,
                        str(idx),
                        org=(x - 15, y - 15),
                        fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                        fontScale=0.4,
                        color=color,
                        thickness=1)

    def drawline(self,pts):
        cv2.polylines(self.img, [pts], isClosed=False, color=(0, 255, 255), thickness=2)
        pass

    def draw0k(self):
        point4_Y = self.indexCvPoint(4)[1]
        point8_Y = self.indexCvPoint(8)[1]
        point12_y = self.indexCvPoint(12)[1]
        point10_y = self.indexCvPoint(10)[1]
        point16_y = self.indexCvPoint(16)[1]
        point14_y = self.indexCvPoint(14)[1]
        point20_y = self.indexCvPoint(20)[1]
        point18_y = self.indexCvPoint(18)[1]
        if abs(point4_Y - point8_Y) < 50 and point12_y < point10_y and point16_y < point14_y\
            and point20_y < point18_y:
            cv2.putText(self.img,
                        str('OK'),
                        org=(200, 100),
                        fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                        fontScale=0.4,
                        color=(0, 255, 255),
                        thickness=1)
        pass

    def drawLove(self):
        if len(self.mulHands) != 2:
            return
        rightHand_4 = self.indexCvPoint(4, isRight=True)
        leftHand_4 = self.indexCvPoint(4, isRight=False)
        point_4 = math.hypot(rightHand_4[0] - leftHand_4[0], rightHand_4[1] - leftHand_4[1])
        rightHand_8 = self.indexCvPoint(8, isRight=True)
        leftHand_8 = self.indexCvPoint(8, isRight=False)
        point_8 = math.hypot(rightHand_8[0] - leftHand_8[0], rightHand_8[1] - leftHand_8[1])

        h = w = abs(rightHand_4[0] - rightHand_8[0])
        x = rightHand_8[0] - h // 2
        y = rightHand_8[1]
        if point_4 < 000 and point_8 < 200:
            face_detect.drawLogo(self.img, self.loveLogo, (x, y, w, h))
        pass

    def indexCvPoint(self, index, isRight = True):
        """
        通过索引将关键点转换到对应的屏幕坐标
        :param index:
        :return:
        """
        if isRight:
            landmark = self.rightLandmark
        else:
            landmark = self.leftLandmark
        # 屏幕的大小
        imgH, imgW = self.img.shape[:2]
        # print(imgH, imgW)
        # 保存该关键点的坐标
        lm =landmark[index]
        # 精准定位
        x = int(lm.x * imgW)
        y = int(lm.y * imgH)
        # print(x, y)
        return x, y