import random
import time

from Pages.AdminPage import AdminPage
from Pages.LoginPage import loginPage

def test_tc06_validate_user_in_admin_list(setup):
    driver = setup

    driver = setup
    login_page = loginPage(driver)
    login_page.launch_url()
    login_page.enter_username("Admin")
    login_page.enter_password("admin123")
    login_page.click_login()
    assert login_page.login_success() == True


    with open("new_user.txt", "r") as f:
        new_username = f.read().strip()

    admin = AdminPage(driver)
    admin.click_on_admin()
    time.sleep(3)
    admin.validate_loaded_page()
    assert admin.check_for_new_user(new_username) == True  # Pass username here
    print(f"User {new_username} found in Admin table")