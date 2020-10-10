import time
from PyQt5.QtWidgets import QWidget
from ui.FaceNotifyDetailUI import Ui_Form
from PyQt5.QtGui import QPixmap

from utils.common import displayOriginImage

class FaceNotifyDetailPage(Ui_Form,QWidget):
    def __init__(self,HomeLayout,data):
        super(FaceNotifyDetailPage,self).__init__()
        self.setupUi(self)
        self.HomeLayout = HomeLayout
        self.notify = data['notify']
        self.initUI()

    def initUI(self):
        time_str,similarity_str,face_image,register_image,camera_name,face_lib_name,capture_image,face_name,camera_url = self.notify
        self.playImage(self.label_capture,capture_image)
        displayOriginImage(self.label_register,register_image,200,None,True,200)
        displayOriginImage(self.label_face,face_image,200,None,True,200)

        self.label_time.setText(time_str)
        self.label_camera_name.setText(camera_name)
        self.label_camera_url.setText(camera_url)
        self.label_name.setText(face_name)
        self.label_similaity.setText(similarity_str)
        self.label_face_lib.setText(face_lib_name)

    def playImage(self,label,image):
        jpj1 = QPixmap(image)
        label.setPixmap(jpj1)
        label.setScaledContents(True)

    def timestamp_to_str(self, timestamp=None, format='%Y-%m-%d %H:%M:%S'):
        if timestamp:
            time_tuple = time.localtime(timestamp)  # 把时间戳转换成时间元祖
            result = time.strftime(format, time_tuple)  # 把时间元祖转换成格式化好的时间
            return result
        else:
            return time.strptime(format)