from http.server import HTTPServer, BaseHTTPRequestHandler
import json
from sql.DBHelper import DBHelper

dbHelper = DBHelper()
dbHelper.create_notify_table()

class Resquest(BaseHTTPRequestHandler):
    def handler(self):
        print("data:", self.rfile.readline().decode())
        self.wfile.write(self.rfile.readline())

    def do_GET(self):
        print("===="+self.requestline)
        if self.path != '/hello':
            self.send_error(404, "Page not Found!")
            return

        data = {
            'result_code': '1',
            'result_desc': 'Success',
            'timestamp': '',
            'data': {'message_id': '25d55ad283aa400af464c76d713c07ad'}
        }
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(data).encode())

    def do_POST(self):
        print("====" + self.requestline)
        req_datas = self.rfile.read(int(self.headers['content-length']))  # 重点在此步!
        jsonData = json.loads(req_datas.decode())
        notify = jsonData['data']
        command = jsonData['command']

        face_id = notify["face_id"]
        # 获取注册个人头像
        db_back = dbHelper.select_single_face(face_id)
        if(db_back):
            if (len(db_back) > 0):
                face = db_back[0]
                notify['register_image'] = face[4]
                notify['face_name'] = face[3]

            #获取人脸库名字
            face_lib_id = notify["face_lib_id"]
            db_back = dbHelper.select_single_library(face_lib_id)
            if (len(db_back) > 0):
                lib = db_back[0]
                notify['face_lib_name'] = lib[0]

            # 获取摄像头名字
            camera_url = notify['camera_url']
            db_back = dbHelper.select_camera_by_url(camera_url)
            if (len(db_back) > 0):
                camera = db_back[0]
                notify['camera_name'] = camera[0]

        if command == 11:
            dbHelper.insert_notify(notify)

        data = {
            'code': 0,
            'msg': 'ok'
        }
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(data).encode('utf-8'))


