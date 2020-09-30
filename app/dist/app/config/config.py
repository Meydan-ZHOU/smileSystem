from configobj import ConfigObj
path = r'./config/config.ini'


def config_read():
    config = ConfigObj(path, encoding='UTF8')
    host = config['server']['host']
    print("current host: ", host)
    return host

def config_write(host):
    config = ConfigObj(path, encoding='UTF8')
    config['server']['host'] = host
    config.write()