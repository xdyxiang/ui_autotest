from  flow.homeflow import HomeFlow


def test_account_manager(init_function):
    HomeFlow(init_function).check_home()


def test_setting_center(init_function):
    HomeFlow(init_function).check_home()
