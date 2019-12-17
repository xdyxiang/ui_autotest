from  flow.homeflow import HomeFlow


def test_check_home(init_function):
    HomeFlow(init_function).check_home()


def test_check_header_not_login(init_function):
    HomeFlow(init_function).check_header_not_login()


def test_check_header_login(init_function):
    HomeFlow(init_function).check_header_login()


def test_check_footer(init_function):
    HomeFlow(init_function).check_footer()
