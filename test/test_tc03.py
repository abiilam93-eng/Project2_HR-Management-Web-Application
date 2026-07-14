
from Pages.LoginPage import loginPage

def test_tc03_presence_of_login_fields(setup):
    driver = setup
    login_page = loginPage(driver)
    login_page.launch_url()
    username_status = login_page.username_visible()
    password_status = login_page.password_visible()
    assert username_status == True, "Username field is not visible and enabled"
    assert password_status == True, "Password field is not visible and enabled"
    print("Username and Password fields are visible and enabled")