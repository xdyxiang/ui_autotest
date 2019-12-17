from selenium.webdriver.common.by import By


class AccCenOBJ:
    # 我的账号
    myaccount = (By.XPATH, '//*[@id="l-setting"]/main/div/div/div[1]/div/div/ul/li[1]/ul/li[1]')
    shareaccount = (By.XPATH, '//*[@id="l-setting"]/main/div/div/div[1]/div/div/ul/li[1]/ul/li[2]')
    myaccount_all_account = (By.XPATH, '//*[@id="tab-shown"]')
    myaccount_hide_account = (By.XPATH, '//*[@id="tab-hidden"]')
    myaccount_select_coin = (By.XPATH, '//*[@id="l-setting"]/main/div/div/div[2]/div/div[1]/div[2]/div[1]/i')
    myaccount_new_subaccount = (By.XPATH, '//*[@id="l-setting"]/main/div/div/div[2]/div/div[1]/div[2]/div[1]/button[1]/span')
    myaccount_manage_subaccount_exit = (By.XPATH, '//*[@id="l-setting"]/main/div/div/div[2]/div/div[1]/div[2]/div[1]/button[2]')
    myaccount_manage_hidebutton = (By.XPATH, '//*[@id="pane-shown"]/div/div[4]/div[2]/table/tbody/tr[3]/td[1]/div/button/span')
    myaccount_manage_showbutton = (By.XPATH, '//*[@id="pane-hidden"]/div/div[4]/div[2]/table/tbody/tr/td[1]/div/button/span')
    myaccount_all_list1_account = (By.XPATH, '//*[@id="pane-shown"]/div/div[4]/div[2]/table/tbody/tr[2]/td[2]/div/div/a')
    myaccount_all_list1_BCH = (By.XPATH, '//*[@id="pane-shown"]/div/div[3]/table/tbody/tr[2]/td[4]/div/a')


    # 共享账号

