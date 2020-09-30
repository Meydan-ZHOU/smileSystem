import requests
from config.config import config_read

SYS_HOST = config_read()

class HttpClient(object):
    def __init__(self):
        super(HttpClient,self).__init__()

    def do_post(self, url, params=None):
        if(SYS_HOST==''):
            return

        try:
            res = requests.post(SYS_HOST+url, json=params)
            return res
        except (ConnectionError,):
            print('Crawling Failed', url)
            return None

    def do_get(self,url,params=None):
        if (SYS_HOST == ''):
            return
        try:
            res = requests.get(SYS_HOST+url, params=params)
            return res
        except (ConnectionError):
            print('Crawling Failed', url)
            return None

