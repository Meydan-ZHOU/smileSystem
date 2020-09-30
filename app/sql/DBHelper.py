import os,sys,shutil,stat
import base64
import datetime
from sql.Sqlite import ConnectSqlite

dirname, filename = os.path.split(os.path.abspath(sys.argv[0]))

notify_image_total_path = dirname+"\\allTasksImages\\"
lib_face_all_image_path = dirname+'\\allFace\\'

class DBHelper(object):
    def __init__(self,*args, **kwargs):
        super(DBHelper,self).__init__()
        self.db = ConnectSqlite("../faceManagement.db")

    #删除任务相关notify
    def delete_notify(self,task_id):
        sql = "DELETE FROM notify WHERE task_id='{id}'".format(id=task_id)
        self.remove_task_notify_face(task_id)
        return self.db.delete_table(sql)

    #删除notify捕获的图片
    def remove_task_notify_face(self,task_id):
        path = notify_image_total_path+task_id
        self.delete_file(path)

    #更新摄像头
    def update_camera(self,camera):
        ip = camera['ip']
        sn = camera['sn']
        name = camera['name']
        username = camera['username']
        password = camera['password']
        url = camera['url']
        sql = " UPDATE camera SET name='{name}',sn='{sn}',username='{username}',password='{password}',url='{url}' where ip='{ip}'".format(ip=ip,name=name,username=username,password=password,url=url,sn=sn)
        return self.db.insert_update_table(sql)

    #删除摄像头
    def delete_camera(self,ip):
        sql = "DELETE FROM camera WHERE ip='{ip}'".format(ip=ip)
        return self.db.delete_table(sql)

    #查询所有摄像头
    def select_all_camera(self):
        sql = "SELECT * from camera"
        return self.db.fetchall_table(sql)

        # 查询所有摄像头

    def select_camera_by_url(self,url):
        sql = "SELECT * from camera WHERE url='{url}'".format(url=url)
        return self.db.fetchall_table(sql)

    #插入摄像头
    def insert_camera(self,data):
        name = data['name']
        ip = data['ip']
        username = data['username']
        password = data['password']
        sn = data['sn']
        url = data['url']

        sql = """
                    INSERT INTO camera
                    (name,ip,sn,username,password,url)
                    VALUES (?,?,?,?,?,?)
                """
        value = [(name, ip, sn, username, password, url)]
        return self.db.insert_table_many(sql, value)

    #查询单个人脸
    def select_single_face(self,face_id):
        sql = "SELECT * from face where face_id='{id}'".format(id=face_id)
        return self.db.fetchall_table(sql)

    #查询所有人脸
    def select_all_face(self,id):
        sql = "SELECT * from face where face_lib_id='{id}'".format(id=id)
        return self.db.fetchall_table(sql)

    #删除单个人脸
    def delete_face(self,face_id,face_name,lib_name):
        sql = "DELETE FROM face WHERE face_id='{id}'".format(id=face_id)
        path = lib_face_all_image_path+lib_name+'/'+face_name+'.jpg'
        db_back = self.db.delete_table(sql)
        if(db_back):
            os.remove(path)
        return db_back

    #删除某人脸库所有人脸
    def delete_library_all_face(self,lib_id):
        sql = "DELETE FROM face WHERE face_lib_id='{id}'".format(id=lib_id)
        return self.db.delete_table(sql)

    #向某人脸库插入一人脸
    def insert_library_face(self,data):
        lib_name, lib_id  = data["library"]
        face_name = data["name"]
        face_id = data["face_id"]
        origin_image = data["origin_image"]
        age = data["age"]
        sex = data["sex"]
        tel = data["tel"]

        path = lib_face_all_image_path+lib_name
        filename = face_name + '.jpg'
        face_path = path+'/'+filename

        if (not os.path.isdir(path)):
            os.makedirs(path)

        self.save_image_to_file(path,filename,origin_image)
        sql = """
                 INSERT INTO face
                 (face_lib_name,face_lib_id,face_id,face_name,face_photo,age,sex,tel)
                 VALUES (?,?,?,?,?,?,?,?)
             """
        value = [(lib_name, lib_id,face_id, face_name, face_path, age, sex, tel)]
        return self.db.insert_table_many(sql, value)

    #查询所有人脸库
    def select_all_library(self):
        sql = "SELECT * from library"
        return self.db.fetchall_table(sql)

    #查询单个人脸库
    def select_single_library(self,lib_id):
        sql = "SELECT * from library where face_lib_id='{id}'".format(id=lib_id)
        return self.db.fetchall_table(sql)

    #删除人脸库
    def delete_library(self,id,name):
        sql = "DELETE FROM library WHERE face_lib_id='{id}'".format(id=id)
        db_back = self.db.delete_table(sql)
        print("del_library db", db_back)
        if(db_back):
            #删除人脸库文件夹和里面的人脸头像
            self.remove_libray_all_faces(id,name)
        return db_back

    #删除文件夹及内部文件
    def delete_file(self,filePath):
        if os.path.exists(filePath):
            for fileList in os.walk(filePath):
                for name in fileList[2]:
                    os.chmod(os.path.join(fileList[0], name), stat.S_IWRITE)
                    os.remove(os.path.join(fileList[0], name))
            shutil.rmtree(filePath)
            return "delete ok"
        else:
            return "no filepath"

    #删除某人脸库所有人脸
    def remove_libray_all_faces(self,id,name):
        path = lib_face_all_image_path + name
        self.delete_file(path)
        return self.delete_library_all_face(id)

    #插入人脸库
    def insert_library(self,data):
        sql = """
                 INSERT INTO library
                 (face_lib_name,face_lib_id)
                 VALUES (?,?)
             """
        value = [(data['face_lib_name'],data['face_lib_id'])]
        return self.db.insert_table_many(sql, value)

    #保存图片文件
    def save_image_to_file(self,path,fileName,image):
        file = open(path+'/'+fileName,'wb')
        file.write(image)
        file.close()

    #插入通知信息
    def insert_notify(self,data):
        task_id = data["task_id"]
        camera_url = data["camera_url"]
        notify_time = data["notify_time"]
        similarity = data["similarity"]
        face_id = data["face_id"]
        face_lib_id = data["face_lib_id"]
        capture_image = data["capture_image"]
        register_image = data["register_image"]
        face_lib_name = data["face_lib_name"]
        camera_name = data["camera_name"]
        face_name = data["face_name"]
        extras = str(data["extras"])
        capture_face_image = data["capture_face_image"]
        face_image = base64.b64decode(capture_face_image)

        today = datetime.datetime.now().strftime('%Y-%m-%d')
        task_dir_path = notify_image_total_path+task_id+'\\'+today+"\\"+face_id
        face_file_name = 'face_'+notify_time+'.jpg'

        face_path = task_dir_path + '\\' + face_file_name

        #存图片到本地
        if(not os.path.isdir(task_dir_path)):
            os.makedirs(task_dir_path)

        self.save_image_to_file(task_dir_path, face_file_name,face_image)

        sql = """
            INSERT INTO notify
            (notify_time,task_id,camera_url,face_id,face_lib_id,similarity,extras,face_image,register_image,face_lib_name,camera_name,face_name)
            VALUES (?,?,?,?,?,?,?,?,?,?,?,?)
        """
        values = [(notify_time,task_id,camera_url,face_id,face_lib_id,similarity,extras,face_path,register_image,face_lib_name,camera_name,face_name)]
        print(values)
        print(self.db.insert_table_many(sql, values))

    #查询某一任务所有通知
    def select_task_all_notify(self,task_id,params):
        name = params['name']
        sql = "SELECT * from notify where task_id='{id}' AND face_name like '%{name}%'  order by notify_time desc  LIMIT 0,20 ".format(id=task_id,name=name)
        print(sql)
        return self.db.fetchall_table(sql)

    #创建人脸表
    def create_face_table(self):
        # 创建人脸表
        sql = """
                   CREATE TABLE  IF NOT EXISTS `face` (
                     'face_lib_name' TEXT,
                     `face_lib_id` TEXT,
                     `face_id` TEXT ,
                     `face_name` TEXT ,
                     `face_photo` TEXT ,
                     `age` TEXT ,
                     `sex` TEXT ,
                     `tel` TEXT)
                 """
        self.db.create_tabel(sql)

    #创建摄像头表
    def create_camera_table(self):
        # 创建摄像头表
        sql = """
              CREATE TABLE  IF NOT EXISTS `camera` (
                'name' TEXT,
                `ip` TEXT,
                `sn` TEXT ,
                `username` TEXT ,
                `password` TEXT ,
                `url` TEXT )
            """
        self.db.create_tabel(sql)


    #创建人脸库表
    def create_library_table(self):
        # 创建人脸库表
        sql = """
                 CREATE TABLE  IF NOT EXISTS `library` (
                   'face_lib_name' TEXT,
                   `face_lib_id` TEXT)
               """
        self.db.create_tabel(sql)

    #创建通知表
    def create_notify_table(self):
        # 创建通知表
        sql = """
                   CREATE TABLE  IF NOT EXISTS `notify` (
                     'notify_time' TEXT,
                     `task_id` TEXT,
                     `camera_url` TEXT ,
                     `face_id` TEXT ,
                     `face_lib_id` TEXT ,
                     `similarity` TEXT ,
                     `extras` TEXT,
                     `face_image` TEXT,
                     `register_image` TEXT,
                     `face_lib_name` TEXT,
                     `camera_name` TEXT,
                     `face_name` TEXT)
                 """
        self.db.create_tabel(sql)
