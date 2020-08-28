

class CommonHelper:
    @staticmethod
    def readQSS(style):
        with open(style,'r') as f:
            return f.read()

SYS_STYLE = CommonHelper.readQSS("./static/style/style.qss")