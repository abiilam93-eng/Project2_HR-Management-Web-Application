import random
from Pages.AdminPage import AdminPage
from Pages.LoginPage import loginPage


def test_tc05_create_user_and_validate_login(setup):

    driver = setup
    login_page = loginPage(driver)
    login_page.launch_url()
    login_page.enter_username("Admin")
    login_page.enter_password("admin123")
    login_page.click_login()
    admin = AdminPage(driver)
    admin.click_on_admin()
    admin.click_on_PlusAdd()
    admin.user_role("ESS")
    admin.emp_name()
    admin.status_dropdown("Enabled")

    new_username = "TESTER " + str(random.randint(100, 900))
    new_password = "Test@123"

    admin.new_cred(new_username, new_password)
    admin.validate_loaded_page()

    login_page.logout()
    login_page.launch_url()
    login_page.enter_username(new_username)
    login_page.enter_password(new_password)
    login_page.click_login()
    assert login_page.login_success() == True

    with open("new_user.txt", "w") as f:
        f.write(new_username)