from selenium.webdriver.common.by import By


class LoginOBJ:
    email = (By.XPATH, '//input[@placeholder="邮箱/手机号"]')
    password = (By.XPATH, '//input[@placeholder="密码"]')
    button = (By.XPATH, '//*[@id="l-sign-layout"]/main/div/div[2]/form/div[4]/div/button')
    reset_passwd = (By.XPATH, '//*[@id="l-sign-layout"]/main/div/div[2]/form/a')
    signup = (By.XPATH, '//*[@id="l-sign-layout"]/main/div/div[3]/a')
    title_text = (By.XPATH, '//*[@id="l-sign-layout"]/main/div/div[1]')

    check_box = (By.XPATH, '//*[@id="l-sign-layout"]/main/div/div[2]/form/div[4]/div/div/div/label/span[1]/span')
    server_terms_link = (By.XPATH, '//*[@id="l-sign-layout"]/main/div/div[2]/form/div[4]/div/div/div/label/span[2]/a')
    signup_login = (By.XPATH, '//*[@id="l-sign-layout"]/main/div/div[2]/form/div[6]/a')

    reset_mobile_email_link = (By.XPATH, '//*[@id="l-sign-layout"]/main/div/div[2]/div/a')

    googleinput = (By.XPATH, '//input[@placeholder="谷歌验证码"]')
    googlebuttun = (By.XPATH, '//button[@class="el-button el-button--primary"]')
