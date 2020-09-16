import sys, cv2, os, threading, time
from PyQt5.QtGui import QImage, QPixmap

class Camera:
    def __init__(self, url, label):
        # 创建一个关闭事件并设为未触发
        self.url = url
        self.label = label
        self.stopEvent = threading.Event()
        self.stopEvent.clear()
        print("进程pid:", os.getpid())

    def Open(self):
        print("open",self.url)
        if self.url=='':
            return
        try:
            self.cap = cv2.VideoCapture(self.url)
            self.frameRate = self.cap.get(cv2.CAP_PROP_FPS)
        except(ConnectionError):
            self.Close()
            print("视频打开异常")

        th = threading.Thread(target=self.Display)
        th.start()

    def Close(self):
        print("close",self.stopEvent)
        # 关闭事件设为触发，关闭视频播放
        self.stopEvent.set()
        self.cap.release()
        self.cap = None
        self.label.clear()

    def Display(self):
        startTime = time.time()
        try:
            while self.cap.isOpened():
                success, frame = self.cap.read()
                if success:
                    if (time.time() - startTime) > 0.1:
                        # RGB转BGR
                        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
                        newRate = int(frame.shape[0] / 500)  # 求出resize的比值
                        newHeight = int(frame.shape[0] / newRate)  # resize后的高和宽
                        newWidth = int(frame.shape[1] / newRate)
                        newFrame = cv2.resize(frame, (newWidth, newHeight), interpolation=cv2.INTER_AREA)
                        bytesPerLine = 3 * newWidth
                        self.label.setScaledContents(True)
                        temp_image = QImage(newFrame.data, newWidth, newHeight, bytesPerLine, QImage.Format_RGB888)
                        self.label.setPixmap(QPixmap.fromImage(temp_image))
                        cv2.waitKey(int(1000 / self.frameRate))
                        startTime = time.time()
                        #print(startTime)

                        # 判断关闭事件是否已触发
                        if True == self.stopEvent.is_set():
                            # 关闭事件置为未触发，清空显示label
                            print("判断关闭事件是否已触发")
                            self.stopEvent.clear()
                            self.label.clear()
                            break

                else:
                    break
        except(ConnectionError):
            self.Close()
            print("视频播放异常")

        if not self.cap.isOpened():
            self.Close()

