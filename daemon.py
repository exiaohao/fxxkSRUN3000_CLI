import time
import requests
import logging

DEBUG = False
TEST_GET_ADDR = 'http://115.239.210.27'

AUTH_ACTION_URL = 'http://10.100.1.251:{port}/include/auth_action.php'
AUTH_USERNAME = '00106710'
AUTH_PASSWORD = '210712'

def get_ac_port(url):
    start_str = url.find('://')
    url_pies = url[start_str+3:].split('/')
    try:
        addr = url_pies[0]
    except Exception as ex:
        logging.exception(ex)

    try:
        return addr.split(':')[1]
    except Exception as ex:
        logging.exception(ex)

def auth():
    ac_detect_response = requests.get('http://10.100.1.251/ac_detect.php?ac_id=1')
    access_controller_port = get_ac_port(ac_detect_response.url)

    req = requests.Session()
    auth_payload = {
        "action": "login",
        "username": AUTH_USERNAME,
        "password": AUTH_PASSWORD,
        "ac_id": 1,
        "user_ip": "",
        "nas_ip": "",
        "user_mac": "",
        "save_me": 1,
        "ajax": 1,
    }
    response = req.post(AUTH_ACTION_URL.format(port=access_controller_port), data=auth_payload)

def alive_check():
    try:
        response = requests.get(TEST_GET_ADDR, timeout=2)
    except Exception:
        auth()

    if response.url.find('10.100') > -1:
        if DEBUG:
            print('Fuck, Trying Auth!')
        auth()
    elif DEBUG:
        print('Online')

if __name__ == "__main__":
    while(1):
        alive_check()
        time.sleep(10.0)

