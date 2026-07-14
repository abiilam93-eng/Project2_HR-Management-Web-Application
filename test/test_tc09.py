from Pages.LoginPage import loginPage
from Pages.LeavePage import LeavePage
import datetime

def test_tc09_assign_leave_and_verify(setup):
    driver = setup
    login_page = loginPage(driver)
    leave_page = LeavePage(driver)

    login_page.launch_url()
    login_page.enter_username("Admin")
    login_page.enter_password("admin123")
    login_page.click_login()
    leave_page.go_to_assign_leave()

    leave_page.assign_leave("Ranga  Akunuri","US - Personal")
    leave_page.confirmation_popup()

    assert leave_page.check_leave_list("Ranga Akunuri") == True
    print("Leave record found")