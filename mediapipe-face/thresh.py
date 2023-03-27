import util

class Thresh:
    def __init__(self):
        self.thresh = -1
        self.threshHolds = []
        self.avgThresh = 0
        pass

    def getThresh(self, EAR):

        self.threshHolds.append(EAR)
        cnt = len(self.threshHolds)
        if cnt == 10:
            self.avgThresh = sum(self.threshHolds) / cnt
        return self.avgThresh


