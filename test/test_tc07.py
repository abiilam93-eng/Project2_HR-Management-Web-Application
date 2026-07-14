from Pages.LoginPage import loginPage


def test_tc07_logout_functionality_validation(setup):
    driver = setup
    login_page = loginPage(driver)
    login_page.launch_url()
    login_page.forgot_password_link()