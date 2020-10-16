from PyQt5.QtWidgets import QWidget
import av, os, threading,time
from ui.VideoUI import Ui_Form
from PyQt5.QtGui import QImage, QPixmap,QMovie
import numpy as np

mu = threading.Lock()

class Video(Ui_Form,QWidget):
    def __init__(self):
        super(Video,self).__init__()
        self.setupUi(self)
        # 创建一个关闭事件并设为未触发
        self.initUI()
        self.initSlot()
        self.player = {}
        self.isClosing = False
        self.currentUrl = ''
        self.threadList = []
        print("video 进程pid:", os.getpid())

    def initUI(self):
        self.width = self.size().width()
        self.height = self.size().height()
        self.label.setText("请点击左侧摄像头进行播放")
        self.label.setStyleSheet("background-color:transparent;")
        self.widget_tools.hide()

    def isLoading(self):
        print("----------------------loading video-----------------------------------------")
        path = "static/images/loading.gif"
        move = QMovie(path)
        self.label.clear()
        self.label.setMovie(move)
        self.label.setStyleSheet("background-color:#000;")
        move.start()

    def initSlot(self):
        self.pushButton_close.clicked.connect(self.Close)

    def Open(self,url,name):
        if url=='' or self.currentUrl == url:
            print("==============尚未结束===================")
            return

        if(not self.currentUrl == url):
            print("llllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllll")

        self.initUI()
        self.isLoading()
        self.playerClose()

        try:
            while(len(self.threadList)>0):
                print("上一个还在播放尼")
                self.playerClose()
                time.sleep(0.5)

            th = threading.Thread(target=self.Display,args=[url,name])
            th.setDaemon(True)
            th.start()
            self.threadList.append(th)
        except Exception as e:
            print('fate1 error:{}'.format(e))
            self.PlayError()
            return

    def PlayError(self):
        self.isClosing = False
        self.label.setText("视频打开异常")
        self.label.setProperty('class', 'error')
        self.widget_tools.hide()

    def playerClose(self):
        print('close self.player------------',threading.currentThread().name,'--------------', self.player)
        self.isClosing = True
        self.isLoading()
        start_time = time.time()
        for th in self.threadList:
            thName = th.name
            print("---------------close----------", th)
            player = self.player[thName]['player']
            self.player[thName]['isPlaying'] = False
            if th.is_alive() == False:
                if(not player == None):
                    player.close()
                th.join()
                self.threadList.remove(th)
                self.player.pop(thName)
        end_time =  time.time()

        print("len self.threadList", len(self.threadList))
        print("use time ", end_time - start_time)


    def Close(self):
        # 关闭事件设为触发，关闭视频播放
        try:
            # 关闭事件设为触发，关闭视频播放
            self.currentUrl = ''
            self.playerClose()
            self.initUI()
        except Exception as e:
            print('video close error:{}'.format(e))


    def Display(self,url,name):
        try:
            current_thread = threading.currentThread()
            th_name = current_thread.name
            if (self.player.get(th_name) == None):
                self.player[th_name] = {
                    'name':current_thread,
                    'isPlaying': True,
                    'player': None
                }
                print("-----------", self.player[th_name], '-----------')
            dicOption = {'buffer_size': '1024000', 'rtsp_transport': 'tcp', 'stimeout': '3000000',
                         'max_delay': '3000000', '-an':''}
            self.currentUrl = url
            self.player[th_name]['player'] = av.open(url, 'r', format=None, options=dicOption, metadata_errors='strict')
            print('open', url)
            print("===================", self.player, '==================')
            self.widget_tools.show()
            self.label_camera_name.setText(name)
            self.player[th_name]['isPlaying'] = True
            self.isClosing = False

            show_width = int(self.label.width()/16)*16
            show_height = int(self.label.height()/16)*16
            start_time = time.time()
            print("danny: start open",self.player[th_name]['player'])
            if self.player[th_name]['player']:
                for frame in self.player[th_name]['player'].decode(video=0):
                    if(frame.pts == None):
                        continue
                    if(False == self.player[th_name]['isPlaying']):
                        self.initUI()
                        self.isClosing = False
                        print("8888888888888888888888888888888888888----关闭流----888888888888888888888888888888888888")
                        break
                    frame_show = frame.reformat(width=show_width,height=show_height)
                    img_array = frame_show.to_ndarray(format='rgb24')
                    in_frame = (
                        np.frombuffer(img_array, np.uint8).reshape([show_height,show_width, 3])
                    )
                    temp_image = QImage(in_frame, show_width, show_height, QImage.Format_RGB888)
                    temp_pixmap = QPixmap.fromImage(temp_image)
                    self.label.setPixmap(temp_pixmap)
                print("********************************播放完毕**********",url)
            else:
                self.PlayError()
                print("xxxxxxxxxxxxxxxxxxxxxxxx播放器被删除啦xxxxxxxxxxxx")

        except Exception as e:
            self.PlayError()
            print('video fate2 error:{}'.format(e))

