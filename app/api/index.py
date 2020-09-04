from httpserver.httpclient import HttpClient

_http = HttpClient()

def get_librarys():
    return _http.do_get("/library")


def add_library(params):
    print("add_library",params)
    return _http.do_post('/library/new',params)

def add_face(params):
    print("add_face",params)
    return _http.do_post('/face/new', params)

def detectImage(params):
    print("detectImage", params)
    return _http.do_post('/face/detect', params)