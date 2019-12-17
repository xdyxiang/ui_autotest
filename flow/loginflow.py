from pageobj.homeobj import HomeOBJ
from pageobj.loginobj import LoginOBJ
import time,random
from common.gtcode import CrackGeetest
from common.config import base_url
from common.action_check import AC
from common.tools import write_cookie,driver_add_cookie

class LoginFlow:
    def __init__(self,driver):
        self.ac = AC(driver)
        self.driver = driver

    def login_action(self,email,pwd,username):
        self.driver.get(base_url+"/signin")
        self.ac.send_key(LoginOBJ.email,email)
        self.ac.send_key(LoginOBJ.password,pwd)
        time.sleep(0.5)
        self.ac.click(LoginOBJ.button)
        crack = CrackGeetest(self.driver,self.ac.wait)
        crack.crack()
        # self.login_safe_check()
        self.ac.check_text1(HomeOBJ.header_username,username)
        token = self.get_token()


    def check_login_pageinfo(self):
        self.driver.get(base_url+"/signin")
        self.ac.check_title('*')
        self.ac.check_text(LoginOBJ.title_text,"登录")
        self.ac.check_text(LoginOBJ.reset_passwd,"忘记密码？")
        self.ac.check_text(LoginOBJ.signup,"注册")
        self.ac.click(LoginOBJ.signup)
        self.ac.check_text(LoginOBJ.title_text,"注册")
        self.ac.check_title('ViaPool | 注册')
        self.ac.click(LoginOBJ.check_box)
        self.ac.check_link_and_close(LoginOBJ.server_terms_link,'*')
        self.ac.check_text(LoginOBJ.signup_login,"*")
        self.ac.click(LoginOBJ.signup_login)
        self.ac.check_title('*')
        self.ac.click(LoginOBJ.reset_passwd)
        self.ac.check_title('*')
        self.ac.check_text(LoginOBJ.title_text, "*")
        self.ac.check_text(LoginOBJ.reset_mobile_email_link,'通过手机号重置密码 ')
        self.ac.click(LoginOBJ.reset_mobile_email_link)
        self.ac.check_text(LoginOBJ.reset_mobile_email_link,'通过邮箱重置密码')


    def ckeck_and_set_cookie(self):
        self.driver.get(base_url + "/wallet/summary")
        driver_add_cookie(self.driver)
        self.driver.get(base_url + "/wallet/summary")
        if self.driver.title == "*":
            print("cookie 有效-----")
        else:
            self.login_action("dengyouxin001@gmail.com", "123456","gmail001")


    # 登录安全校验
    def login_safe_check(self):
        """[summary]
        判断是否有2次验证
        """
        try:
            googlecode= ""
            for i in range(6):
                num = random.randint(0, 9)
                googlecode += str(num)
            self.ac.send_key(LoginOBJ.googleinput,googlecode)
            self.ac.click(LoginOBJ.googlebuttun)
            time.sleep(1)
        except:
            print("登录不需要安全验证")

    # 获取token，打印token,设置cookie
    def get_token(self):
        token = self.driver.get_cookie("token").get("value")
        write_cookie(token)
        print(token)
        return token


