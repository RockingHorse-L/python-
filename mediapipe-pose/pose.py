"""
    当前使用mediapipe去识别人体的关键点

"""
from time import sleep

import cv2
import mediapipe as mp
import util

from grade import Grade


class Pose:
    def __init__(self):
        mpPose = mp.solutions.pose
        # 加载模型 只需要在初始化的时候加载一次
        self.pose = mpPose.Pose()
        # 存储关键点
        self.landmark = []
        # 被识别的图像
        self.img = None
        # 计数
        self.grade = Grade()

        pass

    def process(self, img):
        self.img = img
        # 开始
        self.grade.StartCountdown()

        # 进行
        self.grade.ingCountDown()
        self.drawPointStyle()
        # 没有关键点不需要执行
        if len(self.landmark) == 0:
            return
        self.armBuildCnt()
        # 结束
        if self.grade.status == 3 :
            self.grade.endFlag()


    def drawPointStyle(self):
        """
        绘制关键点的样式
        :param img:
        :return:
        """
        img = self.img
        # mpPose = mp.solutions.pose
        # # 加载模型
        # pose = mpPose.Pose()
        pose = self.pose
        # 因为处理的是RGB图像所以需要转换
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        # Processes an RGB image and returns the pose landmarks on the most prominent
        #person detected.

        result = pose.process(imgRGB)
        print(result.pose_landmarks)
        # 绘制关键点的连线
        # 参数1：将关键点绘制到什么地方
        # 参数2: 需要绘制的关键点
        # 参数3：将那些点连接起来
        # 参数4：连接点样式
        # 参数5：连接线样式
        pointStyle = mp.solutions.drawing_utils.DrawingSpec(color=(0, 255, 255), thickness=2)
        lineStyle = mp.solutions.drawing_utils.DrawingSpec(color=(255, 255, 0), thickness=2)
        conn = mp.solutions.pose_connections
        mp.solutions.drawing_utils.draw_landmarks(
            img,
            result.pose_landmarks,
            conn.POSE_CONNECTIONS,
            pointStyle,
            lineStyle
        )
        # 绘制关键点的序号
        landmark = result.pose_landmarks.landmark
        # 保存关键点
        self.landmark = landmark
        imgH, imgW = img.shape[:2]
        for idx, lm in enumerate(landmark):
            x = int(lm.x * imgW)
            y = int(lm.y * imgH)
            cv2.putText(img,
                        str(idx),
                        org=(x-15, y-15),
                        fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                        fontScale=0.4,
                        color=(0 ,255, 255),
                        thickness=1)
    def armBuildCnt(self):
        """
            手臂弯曲计数
            作业：
                1、屏幕上显示ready go开始计数 同时开始倒计时
                    状态：开始， 进行， 结束
                2、时间到的时候计时结束
                拓展
                3、显示手臂弯曲的历史记录
        :return:
        """
        # imgH, imgW = self.img.shape[:2]
        # mark12 = self.landmark[12].x, self.landmark[12].y
        # mark14 = self.landmark[14].x, self.landmark[14].y
        # mark16 = self.landmark[16].x, self.landmark[16].y
        point12 = self.indexCvPoint(12)
        point14 = self.indexCvPoint(14)
        point16 = self.indexCvPoint(16)
        point11 = self.indexCvPoint(12)
        point13 = self.indexCvPoint(14)
        point15 = self.indexCvPoint(16)
        #angle = util.getAngle(point12, point14, point16)
        angle = util.getAngle(point11, point13, point15)
        self.grade.count(self.img,angle)

        pass

    def indexCvPoint(self, index):
        """
        传入索引返回对应的坐标
        :param index:
        :return:
        """
        imgH, imgW = self.img.shape[:2]
        lm = self.landmark[index]
        x = lm.x * imgW
        y = lm.y * imgH
        return x, y