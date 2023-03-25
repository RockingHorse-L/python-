import cv2


class Grade:
    def __init__(self):
        self.flag = False


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

    def endFlag(self, img):
        cv2.putText(img,
                    str('Game over!'),
                    org=(50, 300),
                    fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                    fontScale=4,
                    color=(208, 224, 64),
                    thickness=15)
