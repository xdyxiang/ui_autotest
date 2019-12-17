import time,random
from io import BytesIO
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PIL import Image
# 无界面的情况下
from selenium.webdriver.chrome.options import Options

EMAIL = 'dengyouxin@viabtc.com'
PASSWORD = '123456'
BORDER_1 = 6.45


class CrackGeetest(object):

    def __init__(self):
        self.url = '********/signin'
        # 无界面运行配置
        chrome_options = Options()
        # chrome_options.add_argument('--headless')
        # chrome_options.add_argument('--disable-gpu')
        self.browser = webdriver.Chrome(chrome_options=chrome_options)
        self.wait = WebDriverWait(self.browser, 5)
        self.email = EMAIL
        self.password = PASSWORD
        self.success = False

    def __del__(self):
        self.browser.close()

    # 获取初始验证按钮
    def get_geetest_button(self):
        """
        获取初始验证按钮
        :return:
        """
        button = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, '//button[@class="el-button signin-btn el-button--primary"]')))
        return button

    # 获取截图中验证码的上下左右的位置
    def get_position(self):
        """
        获取验证码位置
        :return: 验证码位置元组
        """
        # 等待图片加载完成
        time.sleep(1)
        img = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'geetest_canvas_img')))
        location = img.location
        size = img.size
        top, bottom, left, right = location['y'], location['y'] + size['height'], location['x'], location['x'] + size[
            'width']
        return top, bottom, left, right

    # 获取网页截图
    def get_screenshot(self):
        """
        获取网页截图
        :return: 截图对象
        """
        screenshot = self.browser.get_screenshot_as_png()
        screenshot = Image.open(BytesIO(screenshot))
        return screenshot

    # 获取滑块对象
    def get_slider(self):
        """
        获取滑块
        :return: 滑块对象
        """
        try:
            slider = self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'geetest_slider_button')))
        except Exception:
            self.crack()
            return
        return slider

    # 获取验证码图片
    def get_geetest_image(self, name='captcha.png'):
        """
        获取验证码图片
        :return: 图片对象
        """
        top, bottom, left, right = self.get_position()
        screenshot = self.get_screenshot()
        captcha = screenshot.crop((left, top, right, bottom))
        captcha.save(name)
        return captcha

    # 打开页面,输入账号与密码
    def open(self):
        """
        打开网页输入用户名密码
        :return: None
        """
        self.browser.get(self.url)
        time.sleep(0.5)
        email = self.wait.until(EC.presence_of_element_located((By.XPATH, '//input[@placeholder="邮箱/手机号"]')))
        password = self.wait.until(EC.presence_of_element_located((By.XPATH, '//input[@placeholder="密码"]')))
        email.send_keys(self.email)
        password.send_keys(self.password)
        time.sleep(0.5)

    # 拖动滑块到缺口处
    def move_to_gap(self, slider, track):
        """
        拖动滑块到缺口处
        :param slider: 滑块
        :param track: 轨迹
        :return:
        """
        ActionChains(self.browser).click_and_hold(slider).perform()
        for x in track:
            ActionChains(self.browser).move_by_offset(xoffset=x, yoffset=0).perform()
        time.sleep(0.5)
        ActionChains(self.browser).release().perform()

    # 获取缺口偏移量
    def get_gap(self, image):
        """
        获取缺口偏移量
        :param image: 带缺口图片
        :return:
        """
        left_list = []
        for i in [10 * i for i in range(1, 14)]:
            for j in range(50, image.size[0] - 30):
                if self.is_pixel_equal(image, j, i, left_list):
                    break
        return left_list

    # 判断缺口偏移量
    @staticmethod
    def is_pixel_equal(image, x, y, left_list):
        """
        判断两个像素是否相同
        :param image: 图片
        :param x: 位置x
        :param y: 位置y
        :return: 像素是否相同
        """
        x_max = image.size[0]
        # 取两个图片的像素点
        pixel1 = image.load()[x, y]
        threshold = 150
        count = 0
        if pixel1[0] < threshold and pixel1[1] < threshold and pixel1[2] < threshold:
            for i in range(x + 1, image.size[0]):
                piexl = image.load()[i, y]
                if piexl[0] < threshold and piexl[1] < threshold and piexl[2] < threshold:
                    count += 1
                else:
                    break
        if int(x_max/8.6) < count < int(x_max/4.3):
            left_list.append((x, count))
            return True
        else:
            return False

    def is_try_again(self):
        """[summary]
        判断是否能够点击重试
        """
        button_text = self.browser.find_element_by_class_name('geetest_panel_error_content')
        text = button_text.text
        if text == '请点击此处重试':
            button = self.browser.find_element_by_class_name('geetest_panel_error_content')
            button.click()

    def slider_try(self,gap, BORDER):
        # 减去缺口位置
        gap -= BORDER
        # 计算滑动距离
        track = [int(gap)]
        # 拖动滑块
        slider = self.get_slider()
        self.move_to_gap(slider, track)
        try:
            self.success = self.wait.until(
                EC.text_to_be_present_in_element((By.CLASS_NAME, 'geetest_result_content'), '秒的速度超过'))
        except Exception as e:
            print("验证失败")

    def two_check(self):
        """[summary]

        判断是否有2次验证
        """
        try:
            googleinput = self.browser.find_element_by_xpath('//input[@placeholder="谷歌验证码"]')
            googlecode= ""
            for i in range(6):
                num = random.randint(0, 9)
                googlecode += str(num)
            print("googlecode:{0}".format(googlecode))
            googleinput.send_keys(googlecode)
            self.browser.find_element_by_xpath('//button[@class="el-button el-button--primary"]').click()
            time.sleep(1)
        except:
            print("没有二次验证")
            pass

    def crack(self):
        # 输入用户名密码
        self.open()
        # 点击验证按钮
        button = self.get_geetest_button()
        button.click()
        time.sleep(2)
        while not self.success:
            # 判断是否需要重试
            self.is_try_again()
            # 获取验证码图片
            try:
                image = self.get_geetest_image()
            except Exception as e:
                # todo: 判断是其他验证，或者是自动识别通过
                self.success = True
                print("自动识别通过，无需滑动%s" % e)
                time.sleep(2)
                return

            # 获取缺口位置
            left_list = self.get_gap(image)
            x_max = image.size[0]
            left_list = sorted(left_list, key=lambda x: abs(x[1]-int(x_max/6.45)))
            print(left_list)
            if not left_list:
                print("left_lsit为空, 无法获取gap")
                break

            gap = left_list[0][0]

            # 第一中请求，gap减少７
            self.slider_try(gap, BORDER_1)

            # 成功后退出
            if self.success:
                print("验证通过")
                time.sleep(2)
                self.success = True

            # 如果不成功，刷新图片，继续验证
            if not self.success:
                self.browser.find_element_by_class_name("geetest_refresh_1").click()
                time.sleep(1)
                print("刷新验证码")

        #  验证码通过后，二次验证
        self.two_check()

        # 检查是否登录成功
        try:
            time.sleep(1)
            t = self.browser.find_element_by_xpath('//*[@id="header-wrapper"]/div[2]/div/div[2]/ul/li[2]/div')
            print(t.get_attribute('textContent'))
            if t.get_attribute('textContent'):
                print('登录成功')
                print(self.browser.get_cookies())
                for i in self.browser.get_cookies():
                    if i.get("name") == "token":
                        print(i.get("value"))
            else:
                raise NameError
        except Exception as e:
            print("登录失败")



if __name__ == '__main__':
    crack = CrackGeetest()
    crack.crack()
