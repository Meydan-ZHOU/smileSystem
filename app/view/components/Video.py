from PyQt5.QtWidgets import QWidget,qApp
import cv2, av, os, threading, time
from ui.VideoUI import Ui_Form
from PyQt5.QtGui import QImage, QPixmap
import numpy as np

from utils.common import displayOriginImage

class Video(Ui_Form,QWidget):
    def __init__(self):
        super(Video,self).__init__()
        self.setupUi(self)
        # 创建一个关闭事件并设为未触发
        self.initUI()
        self.initSlot()
        self.player = None
        self.isPlaying = False
        self.stopEvent = threading.Event()
        self.stopEvent.clear()
        print("进程pid:", os.getpid())

    def initUI(self):
        self.width = self.size().width()
        self.height = self.size().height()
        print("video size", (self.width, self.height))
        self.label.setText("请点击左侧摄像头进行播放")
        self.widget_tools.hide()

    def isLoading(self):
        print("isloadding")
        print(self.label)
        path = "static/images/loading.gif"
        jpg = QPixmap(path)
        self.label.setPixmap(jpg)
        self.label.setScaledContents(True)

    def initSlot(self):
        self.pushButton_close.clicked.connect(self.Close)
        self.destroyed.connect(lambda :self.Close())

    def Open(self,url,name):
        if url=='':
            return
        self.Close()
        self.isLoading()
        self.stopEvent.clear()
        try:
            print("open", url)
            dicOption = {'buffer_size': '1024000', 'rtsp_transport': 'tcp', 'stimeout': '20000000',
                         'max_delay': '3000000'}
            self.player = av.open(url, 'r', format=None, options=dicOption, metadata_errors='strict')
        except Exception as e:
            print('fate error:{}'.format(e))
            self.label.setText("视频打开异常")
            self.label.setProperty('class','error')
            self.widget_tools.hide()
            return

        self.isPlaying = True
        self.widget_tools.show()
        self.label_camera_name.setText(name)

        self.th = threading.Thread(target=self.Display)
        self.th.setDaemon(True)
        self.th.start()

    def Close(self):
        print("close", self.stopEvent)
        # 关闭事件设为触发，关闭视频播放
        self.stopEvent.set()
        # 关闭事件设为触发，关闭视频播放
        try:
            if(self.player):
                print("video close",self.player)
                self.isPlaying = False
                self.player.close()
                self.initUI()
                self.th.join()
                print("akkaakak")
        except Exception as e:
            print('video close error:{}'.format(e))

    def Display(self):
        try:
            show_width = int(self.label.width()/16)*16
            show_height = int(self.label.height()/16)*16
            print(show_width, show_height)
            if(self.player):
                for frame in self.player.decode(video=0):
                    if(frame.pts == None):
                        continue
                    if(self.isPlaying==False):
                        break

                    frame_show = frame.reformat(width=show_width,height=show_height)
                    img_array = frame_show.to_ndarray(format='rgb24')
                    in_frame = (
                        np.frombuffer(img_array, np.uint8).reshape([show_height,show_width, 3])
                    )
                    temp_image = QImage(in_frame, show_width, show_height, QImage.Format_RGB888)
                    temp_pixmap = QPixmap.fromImage(temp_image)
                    self.label.setPixmap(temp_pixmap)

                    # 判断关闭事件是否已触发
                    if True == self.stopEvent.is_set():
                        # 关闭事件置为未触发，清空显示label
                        print("判断关闭事件是否已触发")
                        self.stopEvent.clear()
                        self.initUI()
                        break

        except Exception as e:
            print('video fate error:{}'.format(e))

