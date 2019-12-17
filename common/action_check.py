from selenium.webdriver.support import expected_conditions as EC
import time
from common.base_dr import init_wait


class AC:
    def __init__(self,driver):
        self.driver = driver
        self.wait = init_wait(self.driver)

    # 检查元素中的text
    def check_text(self,locator,text):
        result = EC.text_to_be_present_in_element(locator,text)
        print(result.text)
        self.true_or_false(result(self.driver))

    # 元素中的text和html标签，检查text包含其中
    def check_text1(self,locator,text):
        t =  self.wait.until(EC.visibility_of_element_located(locator)).get_attribute('textContent')
        self.a_in_b(text,t)

    # 检查title
    def check_title(self,title):
        result = EC.title_is(title)(self.driver)
        print(self.driver.title)
        self.true_or_false(result)

    # 检查元素是否可见
    def check_visible(self,locator):
        result = EC.visibility_of_element_located(locator)(self.driver)
        self.true_or_false(result)

    # 检查元素个数大于某个数
    def check_elements_len(self,locator,num=0):
        result = EC.presence_of_all_elements_located(locator)(self.driver)
        self.true_or_false(result)
        self.compare_num_gt(len(result),3)

    # 检查点击链接后，跳转的页面后关闭
    def check_link_and_close(self,locator,title):
        # 点击后跳转链接
        self.wait.until(EC.element_to_be_clickable(locator)).click()
        windows = self.driver.current_window_handle
        windows1 = self.driver.window_handles[1]
        self.driver.switch_to.window(windows1)
        self.check_title(title)
        self.driver.close()
        self.driver.switch_to.window(windows)

    # 检查点击链接后，跳转的页面后关闭
    def check_link_and_back(self,locator,title):
        time.sleep(0.5)
        self.wait.until(EC.element_to_be_clickable(locator)).click()
        self.check_title(title)
        self.driver.back()


    # 点击
    def click(self,locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()
        time.sleep(0.5)

    # 输入
    def send_key(self,locator,text):
        self.wait.until(EC.visibility_of_element_located(locator)).send_keys(text)


    def compare_num_gt(self,num1,num2):
        if num1 > num2:
            assert True
        else:
            assert False

    def compare_num_eq(self,num1,num2):
        if num1 == num2:
            assert True
        else:
            assert False

    def true_or_false(self,result):
        if result:
            assert True
        else:
            assert False

    def a_in_b(self,a,b):
        if a in b:
            assert True
        else:
            assert False
