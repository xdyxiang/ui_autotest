from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class HomeOBJ:
    # def __init__(self, wait):
    #     self.wait = wait

    header_logo = (By.XPATH, '//*[@id="header-wrapper"]/div[1]/div/a/div')
    header_dashboard = (By.XPATH, '//*[@id="header-wrapper"]/div[2]/div/div[1]/ul/li[1]/a')
    header_assets = (By.XPATH, '//*[@id="header-wrapper"]/div[2]/div/div[1]/ul/li[2]/a')
    header_tool = (By.XPATH, '//*[@id="header-wrapper"]/div[2]/div/div[1]/ul/li[3]/a')
    header_statistics = (By.XPATH, '//*[@id="header-wrapper"]/div[2]/div/div[1]/ul/li[4]/a')
    header_app = (By.XPATH, '//*[@id="header-wrapper"]/div[2]/div/div[1]/ul/li[5]/a')
    header_help = (By.XPATH, '//*[@id="header-wrapper"]/div[2]/div/div[1]/ul/div/a')
    header_product = (By.XPATH, '//*[@id="header-wrapper"]/div[2]/div/div[1]/ul/li[6]/div')
    header_product_explorer = (By.XPATH, '//a[starts-with(@href,"https://explorer.viabtc.com?lang=")]')
    header_product_wallet = (By.XPATH, '//a[starts-with(@href,"https://wallet.viabtc.com?lang=")]')
    header_announcement = (By.XPATH, '//*[@id="header-wrapper"]/div[2]/div/div[2]/ul/li[1]/div[1]/i')
    header_announcement_more = (By.XPATH, '//*[@id="header-wrapper"]/div[2]/div/div[2]/ul/li[1]/div[2]/div/div[1]/a')
    header_announcement_list1 = (
    By.XPATH, '//*[@id="header-wrapper"]/div[2]/div/div[2]/ul/li[1]/div[2]/div/div[2]/div[1]/a')
    header_language = (By.XPATH, '//*[@id="header-wrapper"]/div[2]/div/div[2]/ul/div/div')
    header_language_list1 = (By.XPATH, '//ul/li[@index="en_US"]/div')
    header_signin = (By.XPATH, '//*[@id="header-wrapper"]/div[2]/div/div[2]/ul/li[2]/a')
    header_signup = (By.XPATH, '//*[@id="header-wrapper"]/div[2]/div/div[2]/ul/li[3]/a')
    header_username = (By.XPATH, '//*[@id="header-wrapper"]/div[2]/div/div[2]/ul/li[2]/div[1]')
    header_user_mycount = (By.XPATH, '//a[@href="/setting/account"]')

    close_mask = (By.XPATH, '//*[@id="p-index"]/div[4]/div/div[2]/div/div[1]')

    ad_text = (By.XPATH, '//*[@id="banner"]/h1')
    ad_list = (By.XPATH, '//*[@id="banner"]/div/div/div/div[1]/div/div')
    ad_link = (By.XPATH, '//*[@id="p-index"]/div[2]/div[1]/div/div/div[1]/div[1]/a/span')

    coin_consultation_tittle = (By.XPATH, '//*[@id="p-index"]/div[3]/div/div[1]/div')
    coin_guide = (By.XPATH, '//*[@id="summary"]/div/div[2]/div[2]/div[1]/div[7]/button')
    coin_open_detail = (By.XPATH, '//*[@id="summary"]/div/div[2]/div[2]/div[1]/div[1]/i')
    coin_open_detail_consultation = (
    By.XPATH, '//*[@id="summary"]/div/div[2]/div[2]/div[2]/div[2]/div[2]/div[5]/div/button')
    coin_close_consultation = (By.XPATH, '//*[@id="p-index"]/div[3]/div/div[1]/button')
    coin_consultation = (By.XPATH, '//*[@id="customer"]/div[2]/button')

    guide_more_miming = (By.XPATH, '//*[@id="p-index"]/div[2]/div[6]/div/div[1]/div/div[1]/span[2]/a')
    guide_miming_list1 = (By.XPATH, '//*[@id="p-index"]/div[2]/div[6]/div/div[1]/div/ul/li[1]/a')

    footer_wallet = (By.XPATH, '//*[@id="c-footer"]/div/div[1]/div[3]/div/div[1]/div[2]/div[1]/a')
    footer_explorer = (By.XPATH, '//*[@id="c-footer"]/div/div[1]/div[3]/div/div[1]/div[2]/div[2]/a')
    footer_coinex = (By.XPATH, '//*[@id="c-footer"]/div/div[1]/div[3]/div/div[1]/div[2]/div[3]/a')
    footer_aboutus = (By.XPATH, '//*[@id="c-footer"]/div/div[1]/div[3]/div/div[2]/div[2]/div[1]/a')
    footer_jionus = (By.XPATH, '//*[@id="c-footer"]/div/div[1]/div[3]/div/div[2]/div[2]/div[2]/a')
    footer_servicepage = (By.XPATH, '//*[@id="c-footer"]/div/div[1]/div[3]/div/div[2]/div[2]/div[3]/a')
    footer_fee_standard = (By.XPATH, '//*[@id="c-footer"]/div/div[1]/div[3]/div/div[3]/div[2]/div[1]/a')
    footer_help = (By.XPATH, '//*[@id="c-footer"]/div/div[1]/div[3]/div/div[3]/div[2]/div[2]/a')
    footer_ticket = (By.XPATH, '//*[@id="c-footer"]/div/div[1]/div[3]/div/div[3]/div[2]/div[3]/a')
    footer_announcement = (By.XPATH, '//*[@id="c-footer"]/div/div[1]/div[3]/div/div[3]/div[2]/div[4]/a')

    # def click_close_mask(self):
    #     self.wait.until(EC.visibility_of_element_located(self.close_mask)).click()
    #
