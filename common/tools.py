import os
from common.config import cookie,base_url

dirname,filename=os.path.split(__file__)

def write_cookie(cookie):
    f = open(dirname+'/cookie.txt', 'w+')
    f.write(cookie)
    f.close()

def read_cookie():
    with open(dirname+'/cookie.txt','r') as f:
        cookie = f.readline()
    return cookie

def make_cookie():
    filecookie = read_cookie()
    ck = cookie
    ck["value"] = filecookie
    print(ck)
    return ck

def driver_add_cookie(driver):
    driver.get(base_url+"/signin")
    ck = make_cookie()
    driver.add_cookie(ck)

