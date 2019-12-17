from common.config import base_url
from common.tools import driver_add_cookie
from pageobj.poolobj import PoolOBJ
from pageobj.homeobj import HomeOBJ
from common.action_check import AC

class HomeFlow:
    def __init__(self,driver):
        self.driver = driver
        self.ac = AC(driver)

    def check_home(self):
        self.driver.get(base_url)
        # 关掉蒙版弹窗
        self.ac.click(HomeOBJ.close_mask)
        # 检查主页title
        self.ac.check_title('*******')
        # 检查闪页背景文字
        self.ac.check_text(HomeOBJ.ad_text,'********')
        # 检查闪页个数大于3个
        self.ac.check_elements_len(HomeOBJ.ad_list,2)
        # 检查公告链接
        self.ac.check_link_and_back(HomeOBJ.ad_link,"******")
        # 点击教程后，查看跳转是否正确
        self.ac.check_link_and_close(HomeOBJ.coin_guide,"*****")
        # 展开页面，点击大客户招商
        self.ac.click(HomeOBJ.coin_open_detail)
        self.ac.click(HomeOBJ.coin_open_detail_consultation)
        self.ac.check_text(HomeOBJ.coin_consultation_tittle,"*****")
        self.ac.click(HomeOBJ.coin_close_consultation)
        # 点击挖矿教程更多
        self.ac.check_link_and_close(HomeOBJ.guide_more_miming,"******")
        # 点击挖矿教程第一个
        self.ac.check_link_and_close(HomeOBJ.guide_miming_list1,"********")



    def check_header_not_login(self):
        self.driver.get(base_url)
        # 关掉蒙版弹窗
        self.ac.click(HomeOBJ.close_mask)
        # 检查logo图标是否可见
        self.ac.check_visible(HomeOBJ.header_logo)
        # 点击用户面板
        self.ac.click(HomeOBJ.header_dashboard)
        self.ac.check_title('*')
        # 点击资产
        self.ac.click(HomeOBJ.header_assets)
        self.ac.check_title('*')
        # 点击工具
        self.ac.click(HomeOBJ.header_tool)
        self.ac.check_title('*')
        # 点击统计
        self.ac.click(HomeOBJ.header_statistics)
        self.ac.check_title('*')
        # 点击APP
        self.ac.click(HomeOBJ.header_app)
        self.ac.check_title('*')
        # 点击帮助
        self.ac.click(HomeOBJ.header_app)
        self.ac.check_link_and_close(HomeOBJ.header_help,'*')
        # 点击区块浏览器，钱包
        self.ac.click(HomeOBJ.header_product)
        self.ac.check_link_and_close(HomeOBJ.header_product_wallet,'*')
        self.ac.click(HomeOBJ.header_product)
        self.ac.check_link_and_close(HomeOBJ.header_product_explorer,'*')
        # 点击公告
        self.ac.click(HomeOBJ.header_announcement)
        self.ac.click(HomeOBJ.header_announcement_more)
        self.ac.check_title('*')
        self.ac.click(HomeOBJ.header_announcement)
        self.ac.check_link_and_close(HomeOBJ.header_announcement_list1,'**')
        #  点击登录
        self.ac.click(HomeOBJ.header_signin)
        self.ac.check_title('*')
        #  点击注册
        self.ac.click(HomeOBJ.header_signup)
        self.ac.check_title('*')
        #  点击选择多语言
        self.ac.click(HomeOBJ.header_language)
        self.ac.click(HomeOBJ.header_language_list1)
        self.ac.check_title('*')

    def check_header_login(self):
        driver_add_cookie(self.driver)
        self.driver.get(base_url+"/pool/state")
        self.ac.check_text(PoolOBJ.dashboard,'*')
        self.driver.get(base_url+"/wallet/summary")
        self.ac.check_title("*")
        self.ac.check_text1(HomeOBJ.header_username,"gmail001")
        self.ac.click(HomeOBJ.header_username)
        self.ac.click(HomeOBJ.header_user_mycount)
        self.ac.check_title("*")





    def check_footer(self):
        self.driver.get(base_url)
        # 关掉蒙版弹窗
        self.ac.click(HomeOBJ.close_mask)
        # 检查footer 链接
        self.ac.check_link_and_close(HomeOBJ.footer_wallet,'ViaWallet | 专业安全稳定的多链多币种钱包')
        self.ac.check_link_and_close(HomeOBJ.footer_explorer,'ViaBTC多币种区块浏览器')
        self.ac.check_link_and_close(HomeOBJ.footer_coinex,'CoinEx - The Global Digital Coin Exchange')
        self.ac.check_link_and_close(HomeOBJ.footer_aboutus,'ViaBTC | 关于我们')
        self.ac.check_link_and_close(HomeOBJ.footer_jionus,'【微诺招聘】-拉勾网')
        self.ac.check_link_and_close(HomeOBJ.footer_servicepage,'ViaPool | ViaBTC注册服务协议')
        self.ac.check_link_and_close(HomeOBJ.footer_fee_standard,'ViaPool | 费率标准')
        self.ac.check_link_and_close(HomeOBJ.footer_help,'ViaBTC矿池 – ViaBTC 帮助中心')
        self.ac.check_link_and_close(HomeOBJ.footer_ticket,'提交请求 – ViaBTC 帮助中心')
        self.ac.check_link_and_close(HomeOBJ.footer_announcement,'ViaPool | 公告板')

