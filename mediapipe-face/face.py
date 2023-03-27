"""
    使用mediapipe识别脸部
"""
import time

import cv2
import mediapipe as mp
import util
from thresh import Thresh
class Face:
    def __init__(self):
        self.faceVideo = cv2.VideoCapture('test4.mp4')
        self.mpFaceMesh = mp.solutions.face_mesh
        # 加载模型
        self.face = self.mpFaceMesh.FaceMesh()
        # 当前这种方式使用frame的地方比较多 所以定义为成员变量
        self.frame = None
        self.eyeLandmark = []
        # 左眼关键点序号
        self.FACEMESH_LEFT_EYE = [362, 385, 387, 263, 373, 380]
        # 右眼关键点序号
        self.FACEMESH_RIGHT_EYE = [33, 160, 158, 133, 153, 144]
        self.thresh = Thresh()
        # 脸部关键点检查
        mpfaceDetect = mp.solutions.face_detection
        self.facedatect = mpfaceDetect.FaceDetection()
        self.landmark = []
        pass

    def process(self, frame):
        """
        识别脸部
        :return:
        """
        self.frame = frame
        faceDetectResult, multi_face_landmarks = self.getlandmark()
        self.getlandmark()
        if not multi_face_landmarks:
            return
        self.drawStlye(multi_face_landmarks)
        self.drawFaceNum(frame)
        self.drawFaceStlye(faceDetectResult)
        self.calEAR()
        pass

    def getlandmark(self):
        face = self.face
        frameRGB = cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGB)
        result = face.process(frameRGB)

        multi_face_landmarks = result.multi_face_landmarks
        if not multi_face_landmarks:
            return None, None
        # 存储关键点
        self.landmark = multi_face_landmarks[0].landmark
        # A NamedTuple object with a "detections" field that contains a list of the
        #       detected face location data.
        faceDetectResult = self.facedatect.process(frameRGB)

        return faceDetectResult, multi_face_landmarks

    def drawFaceStlye(self, faceDetectResult):
        frame = self.frame
        frameH, frameW = frame.shape[:2]
        #print(faceDetectResult.detections)
        if faceDetectResult == None:
            return
        if faceDetectResult.detections == None:
            return
        # detections 里面存放的是人脸位置数据
        for detection in faceDetectResult.detections:
            #print(f'detection:{detection}')
            # 方式一
            mp.solutions.drawing_utils.draw_detection(self.frame, detection)
            # 方式二
            #x = detection
            pass

    def drawStlye(self, multi_face_landmarks):
        pointStyle = mp.solutions.drawing_utils.DrawingSpec(color=(255, 255, 0), thickness=1)
        lineStyle = mp.solutions.drawing_utils.DrawingSpec(color=(255, 255, 0), thickness=1)
        # 6、关键点的连接点
        conn = mp.solutions.face_mesh_connections
        for face_landmarks in multi_face_landmarks:
            self.eyeLandmark = face_landmarks.landmark
            mp.solutions.drawing_utils.draw_landmarks(
                self.frame,
                face_landmarks,
                conn.FACEMESH_TESSELATION,
                pointStyle,
                lineStyle
            )
        pass

    def drawFaceNum(self, img):
        for idx, lm in enumerate(self.eyeLandmark):
            if (idx not in self.FACEMESH_RIGHT_EYE) and (idx not in self.FACEMESH_LEFT_EYE):
                continue
            x, y = self.indexCVPoint(idx)
            cv2.putText(img, str(idx), (x - 15, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.3, (0, 255, 255), 1)

    def drawFPS(self, frame, prev_time):

        fps_my = int(1 / (time.time() - prev_time))
        cv2.putText(frame, str(f'FPS:{fps_my}'), (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 255), 1)

    def calEAR(self):
        """
        计算纵横比
        """
        # 计算右眼左侧的关键点
        p2 = self.indexCVPoint(160)
        p6 = self.indexCVPoint(144)
        # 计算右眼右侧的关键点
        p3 = self.indexCVPoint(158)
        p5 = self.indexCVPoint(153)
        # 横向的关键点
        p1 = self.indexCVPoint(33)
        p4 = self.indexCVPoint(133)
        dis_p2_p6 = util.getDistance(p2, p6)
        dis_p3_p5 = util.getDistance(p3, p5)
        dis_p1_p4 = util.getDistance(p1, p4)
        # 计算纵横比
        EAR = (dis_p2_p6 + dis_p3_p5) / (dis_p1_p4 * 2.0) * 10
        """
        2.618914004394621
        2.618914004394621
        2.618914004394621
        2.4358945078080914
        2.529582758108403
        2.618914004394621
        2.4358945078080914
        2.4358945078080914
        2.4358945078080914
        2.4358945078080914
        """
        avgThresh = self.thresh.getThresh(EAR)
        if avgThresh <= 0:
            return
        if EAR < avgThresh * 0.9:
            print(f'眨眼啦:{EAR}')

    def indexCVPoint(self, index):
        imgH = self.frame.shape[0]
        imgW = self.frame.shape[1]
        mark = self.eyeLandmark[index]
        x = int(mark.x * imgW)
        y = int(mark.y * imgH)
        return x, y