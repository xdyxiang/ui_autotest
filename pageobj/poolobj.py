from selenium.webdriver.common.by import By


class PoolOBJ:
    dashboard = (By.XPATH, '//*[@id="l-default"]/main/div/div[1]/ul/li[3]/a')
    worker = (By.XPATH, '//*[@id="l-default"]/main/div/div[1]/ul/li[4]/a')
    profit = (By.XPATH, '//*[@id="l-default"]/main/div/div[1]/ul/li[5]/a')
