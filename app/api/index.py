from httpserver.httpclient import HttpClient

_http = HttpClient()

#获取app版本详情信息
def getAppInfo():
    try:
        back = _http.do_get("/system/software",None,1)
        if back:
            print("getAppInfo back", back.json())
        return back
    except ConnectionError:
        print("请求客户端版本接口连接错误！",ConnectionError)
        return False

#获取人脸库列表
def get_librarys():
    try:
        # print("get_librarys/library/")
        back = _http.do_get("/library")
        # print("get_librarys back", back.json())
        return back
    except ConnectionError:
        print("请求人脸库列表接口连接错误！", ConnectionError)
        return False

#删除人脸库
def delete_library(params):
    try:
        print("delete_library", params)
        back = _http.do_post('/library/delete', params)
        if back:
            print("delete_library back", back.json())
        return back
    except ConnectionError:
        print("请求客户端版本接口连接错误！", ConnectionError)
        return False

#停止单个视频任务
def stopTask(params):
    try:
        print("stopTask", params)
        back = _http.do_post('/task/stream/stop', params)
        if back:
            print("stopTask back", back.json())
        return back
    except ConnectionError:
        print("停止单个视频任务接口连接错误！", ConnectionError)
        return False

#通过人脸库id，获取人脸库名字
def get_library_by_id(library_id):
    try:
        # print("get_library_by_id",library_id)
        back = _http.do_get("/library/" + library_id)
        # print("get_library_by_id back", back.json())
        return back
    except ConnectionError:
        print("通过人脸库id，获取人脸库名字接口连接错误！", ConnectionError)
        return False

#删除人脸
def del_faces(params):
    try:
        print("del_faces", params)
        back = _http.do_post('/face/delete', params)
        if back:
            print("del_faces back", back.json())
        return back
    except ConnectionError:
        print("删除人脸接口连接错误！", ConnectionError)
        return False

#获取单个人脸库所有的人脸
def getAllFaces(face_lib_id):
    try:
        print("getAllFaces", face_lib_id)
        back = _http.do_get("/face/query/" + face_lib_id)
        if back:
            print("getAllFaces back", back.json())
        return back
    except ConnectionError:
        print("获取单个人脸库所有的人脸接口连接错误！", ConnectionError)
        return False

#添加人脸库
def add_library(params):
    try:
        print("add_library", params)
        back = _http.do_post('/library/new', params)
        if back:
            print("add_library back", back.json())
        return back
    except ConnectionError:
        print("添加人脸库接口连接错误！", ConnectionError)
        return False

#添加单个人脸
def add_face(params):
    try:
        print("add_face", params)
        back = _http.do_post('/face/new', params)
        if back:
            print("add_face back", back.json())
        return back
    except ConnectionError:
        print("添加单个人脸接口连接错误！", ConnectionError)
        return False

#检测人脸照片质量
def detectImage(params):
    try:
        # print("detectImage", params)
        back = _http.do_post('/face/detect', params)
        if back:
            pass
            #print("detectImage back", back.json())
        return back
    except ConnectionError:
        print("检测人脸照片质量接口连接错误！", ConnectionError)
        return False

#获取任务id列表
def get_tasks_list():
    try:
        # print("get_tasks_list/task/stream/query/")
        back = _http.do_get("/task/stream/query/all")
        # print("get_tasks_list back", back.json())
        return back
    except ConnectionError:
        print("任务id列表接口连接错误！", ConnectionError)
        return False

#获取单个任务详情
def get_task_info_list(task_id):
    try:
        # print("get_task_info_list","/task/stream/query/"+task_id)
        back = _http.do_get("/task/stream/query/" + task_id)
        # print("get_task_info_list back", back.json())
        return back
    except ConnectionError:
        print("单个任务详情接口连接错误！", ConnectionError)
        return False

#新建任务
def newTask(params):
    try:
        print("newTask", params)
        back = _http.do_post('/task/stream/start', params)
        if back:
            print("newTask back", back.json())
        return back
    except ConnectionError:
        print("新建任务接口连接错误！", ConnectionError)
        return False