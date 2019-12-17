from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options


def init_driver():
    # 有界面运行配置
    chrome_options = Options()
    driver = webdriver.Chrome(options=chrome_options)
    driver.set_window_size(1366,768)
    return driver

def init_driver_noUI():
    # 无界面运行配置
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    driver = webdriver.Chrome(options=chrome_options)
    driver.set_window_size(1366,768)
    return driver

def init_wait(driver):
    wait = WebDriverWait(driver, 5)
    return wait

