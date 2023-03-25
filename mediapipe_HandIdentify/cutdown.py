import time


class CutDown:
    def __init__(self, READ_TIME = 3, CUT_DOWN = 10, OVER_TIME = 2):
        self.status = 1
        self.READ_TIME = READ_TIME
        self.CUT_DOWN = CUT_DOWN
        self.OVER_TIME = OVER_TIME
        # 起始时间 要屏幕显示的时候才开始计时，这里写了的话可能视频都没打开就开始计时了
        # 最好写在看见屏幕的时候就开始，初始化一个默认时间-1方便后面处理
        #self.startTime = time.time()
        self.startTime = -1


    def initTime(self):
        """
        初始化时间
        :return:能够看见屏幕的时候的时间
        """
        # 小于等于0的时候才初始化
        if self.startTime <= 0:
            self.startTime = time.time()
        return self.startTime

    def getUseTime(self):
        """
        使用时间s
        :return:
        """
        # 因为startTime和useTime获取的都是当前时间，是一样的，useTime没效果
        # 所以在初始化的时候判断一下
        startTime = self.initTime()
        useTime = time.time() - startTime
        return useTime

    def resetTime(self):
        """
        重置时间
        :return:
        """
        self.startTime = time.time()

    def process(self):
        # 每轮的总时间 0 - 15
        roundTime = self.READ_TIME + self.OVER_TIME + self.CUT_DOWN
        # 运行时间 0- 13
        runTime = self.READ_TIME + self.CUT_DOWN
        # 倒计时的时间
        useTime = self.getUseTime()
        # 0 - 13
        cutdownTime = runTime - useTime

        if useTime <= self.READ_TIME: # 0-3
            # 开始
            self.status = 1
            info = 'ready!'
        elif useTime <= runTime: # 3-13
            # 准备中
            self.status = 2
            info = cutdownTime
        else:
            # 结束 13-15
            self.status = 3
            info = 'over'
            # 重置时间不要写在这里，存在的问题，满足结束条件就会重置 结束两秒就看不见了
            #self.resetTime()

        # 当前看一下时间
        if useTime >= roundTime:
            self.resetTime()

        return info, self.status
