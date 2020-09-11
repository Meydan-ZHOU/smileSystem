import requests
from config.config import SYS_HOST

class HttpClient(object):
    def __init__(self):
        super(HttpClient,self).__init__()

    def do_post(self, url, params=None):
        res = requests.post(SYS_HOST+url, json=params)
        return res

    def do_get(self,url,params=None):
        res = requests.get(SYS_HOST+url, params=params)
        return res


