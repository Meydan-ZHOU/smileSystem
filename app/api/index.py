from httpserver.httpclient import HttpClient

_http = HttpClient()

#获取人脸库列表
def get_librarys():
    #print("get_librarys/library/")
    back =  _http.do_get("/library")
    #print("get_librarys back", back.json())
    return back

#删除人脸库
def delete_library(params):
    print("delete_library", params)
    back = _http.do_post('/library/delete', params)
    print("delete_library back", back.json())
    return back

#停止单个视频任务
def stopTask(params):
    print("stopTask", params)
    back = _http.do_post('/task/stream/stop', params)
    print("stopTask back", back.json())
    return back

#通过人脸库id，获取人脸库名字
def get_library_by_id(library_id):
    #print("get_library_by_id",library_id)
    back = _http.do_get("/library/"+library_id)
    #print("get_library_by_id back", back.json())
    return back

#删除人脸
def del_faces(params):
    print("del_faces", params)
    back = _http.do_post('/face/delete', params)
    print("del_faces back", back.json())
    return back

#获取单个人脸库所有的人脸
def getAllFaces(face_lib_id):
    print("getAllFaces", face_lib_id)
    back = _http.do_get("/face/query/"+face_lib_id)
    print("getAllFaces back", back.json())
    return back

#添加人脸库
def add_library(params):
    print("add_library",params)
    back = _http.do_post('/library/new',params)
    print("add_library back", back.json())
    return back

#添加单个人脸
def add_face(params):
    print("add_face",params)
    back = _http.do_post('/face/new', params)
    print("add_face back", back.json())
    return back

#检测人脸照片质量
def detectImage(params):
    print("detectImage", params)
    back = _http.do_post('/face/detect', params)
    print("detectImage back", back.json())
    return back

#获取任务id列表
def get_tasks_list():
    print("get_tasks_list/task/stream/query/")
    back = _http.do_get("/task/stream/query/all")
    print("get_tasks_list back", back.json())
    return back

#获取单个任务详情
def get_task_info_list(task_id):
    print("get_task_info_list","/task/stream/query/"+task_id)
    back = _http.do_get("/task/stream/query/"+task_id)
    #print("get_task_info_list back", back.json())
    return back

#新建任务
def newTask(params):
    print("newTask", params)
    back = _http.do_post('/task/stream/start', params)
    print("newTask back", back.json())
    return back