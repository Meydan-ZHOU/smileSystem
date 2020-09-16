import os,sys
import base64
import datetime
from sql.Sqlite import ConnectSqlite

dirname, filename = os.path.split(os.path.abspath(sys.argv[0]))

class DBHelper(object):
    def __init__(self,*args, **kwargs):
        super(DBHelper,self).__init__()
        self.db = ConnectSqlite("faceManagement.db")

    def insert_library_face(self,data):
        print("save_library_face")
        face_name = data["name"]
        face_id = data["face_id"]
        face_lib_id = data["face_lib_id"]
        face_lib_name = data["face_lib_name"]
        origin_image = data["origin_image"]
        age = data["age"]
        sex = data["sex"]
        tel = data["tel"]

        path = dirname+'/allFace/'+face_lib_name
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
        value = [(face_lib_name, face_lib_id,face_id, face_name, face_path, age, sex, tel)]
        print("face value",value)
        self.db.insert_table_many(sql, value)

    def select_all_library(self):
        sql = "SELECT * from library"
        return self.db.fetchall_table(sql)

    def del_library(self,id):
        sql = "DELETE FROM library WHERE face_lib_id='{id}'".format(id=id)
        return self.db.delete_table(sql)

    def insert_library(self,data):
        sql = """
                 INSERT INTO library
                 (face_lib_name,face_lib_id)
                 VALUES (?,?)
             """
        value = [(data['face_lib_name'],data['face_lib_id'])]
        return self.db.insert_table_many(sql, value)

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



    def create_library_table(self):
        # 创建人脸库表
        sql = """
                 CREATE TABLE  IF NOT EXISTS `library` (
                   'face_lib_name' TEXT,
                   `face_lib_id` TEXT)
               """
        self.db.create_tabel(sql)

    def save_image_to_file(self,path,fileName,image):
        file = open(path+'/'+fileName,'wb')
        file.write(image)
        file.close()

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
                   `face_image` TEXT)
                   
               """
        self.db.create_tabel(sql)

    def save_notify(self,data):
        task_id = data["task_id"]
        camera_url = data["camera_url"]
        notify_time = data["notify_time"]
        similarity = data["similarity"]
        face_id = data["face_id"]
        face_lib_id = data["face_lib_id"]
        capture_image = data["capture_image"]
        capture_face_image = data["capture_face_image"]
        face_image = base64.b64decode(capture_face_image)

        today = datetime.datetime.now().strftime('%Y-%m-%d')
        task_dir_path = dirname+"/allTasksImages/"+task_id+'/'+today+"/"+face_id
        face_file_name = 'face_'+notify_time+'.jpg'

        face_path = task_dir_path + '/' + face_file_name

        #存图片到本地
        if(not os.path.isdir(task_dir_path)):
            os.makedirs(task_dir_path)

        self.save_image_to_file(task_dir_path, face_file_name,face_image)

        sql = """
            INSERT INTO notify
            (notify_time,task_id,camera_url,face_id,face_lib_id,similarity,face_image)
            VALUES (?,?,?,?,?,?,?)
        """
        value = [(notify_time,task_id,camera_url,face_id,face_lib_id,similarity,face_path)]
        self.db.insert_table_many(sql,value)