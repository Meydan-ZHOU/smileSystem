from configobj import ConfigObj
path = r'./config/config.ini'


def config_read():
    config = ConfigObj(path, encoding='UTF8')
    host = config['server']['host']
    return host

def config_write(host):
    config = ConfigObj(path, encoding='UTF8')
    config['server']['host'] = host
    config.write()


def get_server_ip():
    host = config_read()
    ip = host.split('//')[1].split(':')[0]
    return ip


SERVER_IP = get_server_ip()