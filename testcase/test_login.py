import time
from flow.loginflow import LoginFlow
import pytest


test_login_data = [("******", "123456","gmail001")
                    # ("******", "123456","gmail001")
                   ]
@pytest.mark.parametrize("email, password,username", test_login_data)
def test_login(init_function,email,password,username):
    LoginFlow(init_function).login_action(email,password,username)


def test_check_login_info(init_function):
    LoginFlow(init_function).check_login_pageinfo()


def test_ckeck_and_set_cookie(init_function):
    LoginFlow(init_function).ckeck_and_set_cookie()
