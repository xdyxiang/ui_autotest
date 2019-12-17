import pytest
from common.base_dr import *
from flow.loginflow import LoginFlow


# fixture的作用域：function、module、session ，autouse=True使得函数将默认执行
#  session 所有目录下运行用例，只执行1次
# @pytest.fixture(scope="session",autouse=True)
# def init_session():
#     LoginFlow(init_driver_noUI()).ckeck_and_set_cookie()


@pytest.fixture(scope="function")
def init_function(request):
    print("funtion start------------------")
    driver = init_driver()
    # driver = init_driver_noUI()
    def fin():
        driver.quit()
        print("function end-----------------")
    request.addfinalizer(fin)
    return driver
