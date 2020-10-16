from PyQt5.QtWidgets import QWidget
import av, os, threading,time
from ui.VideoUI import Ui_Form
from PyQt5.QtGui import QImage, QPixmap
import numpy as np

mu = threading.Lock()

class Video(Ui_Form,QWidget):
    def __init__(self):
        super(Video,self).__init__()
        self.setupUi(self)
        # 创建一个关闭事件并设为未触发
        self.stopEvent = threading.Event()
        self.stopEvent.clear()
        self.initUI()
        self.initSlot()
        self.threadList = []
        self.player = None
        self.isPlaying = False
        print("进程pid:", os.getpid())

    def initUI(self):
        self.width = self.size().width()
        self.height = self.size().height()
        self.label.setText("请点击左侧摄像头进行播放")
        self.widget_tools.hide()

    def isLoading(self):
        print("is loading video")
        path = "static/images/loading.gif"
        jpg = QPixmap(path)
        self.label.setText('')
        self.label.setPixmap(jpg)
        self.label.setScaledContents(True)

    def initSlot(self):
        self.pushButton_close.clicked.connect(self.Close)
        self.destroyed.connect(lambda :self.Close())

    def Open(self,url,name):
        print("线程",threading.enumerate())
        if url=='':
            return
        self.initUI()
        self.isLoading()
        try:
            if mu.acquire():  ##加锁
                self.isPlaying = False
                mu.release()
            time.sleep(0.0001)
            th = threading.Thread(target=self.Display,name='videoPlayer',args=[url,name])
            th.setDaemon(True)
            th.start()
            self.threadList.append(th)
        except Exception as e:
            print('fate1 error:{}'.format(e))
            self.PlayError()
            return

    def PlayError(self):
        self.label.setText("视频打开异常")
        self.label.setProperty('class', 'error')
        self.isPlaying = False
        self.widget_tools.hide()

    def Close(self):
        # 关闭事件设为触发，关闭视频播放
        try:
            # 关闭事件设为触发，关闭视频播放
            if self.player == None or self.isPlaying == False:
                return
            if mu.acquire():  ##加锁
                self.isPlaying = False
                mu.release()
            self.player.close()
            print("video close", self.player)
            self.player = None
            self.clearThread()
            self.initUI()
        except Exception as e:
            print('video close error:{}'.format(e))

    def clearThread(self):
        try:
            for th in self.threadList:
                if th.is_alive() == False:
                    th.join()
                    self.threadList.remove(th)
        except Exception as e:
            print("th",e)

    def Display(self,url,name):
        try:
            print("open", url)
            dicOption = {'buffer_size': '1024000', 'rtsp_transport': 'tcp', 'stimeout': '6000000',
                         'max_delay': '3000000'}
            if self.isPlaying == True:
                return
            self.player = av.open(url, 'r', format=None, options=dicOption, metadata_errors='strict')
            self.widget_tools.show()
            self.label_camera_name.setText(name)

            if mu.acquire():  ##加锁
                self.isPlaying = True
                mu.release()

            show_width = int(self.label.width()/16)*16
            show_height = int(self.label.height()/16)*16
            start_time = time.time()
            print("danny: start open")
            if self.player and self.player.decode:
                print("danny: start open success")
                for frame in self.player.decode(video=0):
                    # 判断关闭事件是否已触发
                    if False == self.isPlaying or self.player == None:
                        # 关闭事件置为未触发，清空显示label
                        print("判断关闭事件是否已触发")
                        #self.initUI()
                        return

                    if mu.acquire():  ##加锁
                        if (time.time() - start_time) > 0.1:
                            if(frame.pts == None):
                                mu.release()  ##释放锁
                                continue
                            frame_show = frame.reformat(width=show_width,height=show_height)
                            img_array = frame_show.to_ndarray(format='rgb24')
                            in_frame = (
                                np.frombuffer(img_array, np.uint8).reshape([show_height,show_width, 3])
                            )
                            temp_image = QImage(in_frame, show_width, show_height, QImage.Format_RGB888)
                            temp_pixmap = QPixmap.fromImage(temp_image)
                            self.label.setPixmap(temp_pixmap)
                            start_time = time.time()

                        mu.release()  ##释放锁
            else:
                print("danny: start open failed")

        except Exception as e:
            print('video fate2 error:{}'.format(e))
            self.PlayError()

