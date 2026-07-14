import pytest
from Pages.LoginPage import loginPage
from Pages.HomePage import homepage

def test_tc04_verify_main_menu_items(setup):
    driver = setup
    login_page = loginPage(driver)
    login_page.launch_url()
    login_page.enter_username("Admin")
    login_page.enter_password("admin123")
    login_page.click_login()
    assert login_page.login_success() == True, "Login Failed"

    loaded_page = homepage(driver)

    menus = {
        "Admin": (loaded_page.ADMIN_MENU, loaded_page.ADMIN_HEADER),
        "PIM": (loaded_page.PIM_MENU, loaded_page.PIM_HEADER),
        "Leave": (loaded_page.LEAVE_MENU, loaded_page.LEAVE_HEADER),
        "Time": (loaded_page.TIME_MENU, loaded_page.TIME_HEADER),
        "Recruitment": (loaded_page.RECRUITMENT_MENU, loaded_page.RECRUITMENT_HEADER),
        "MyInfo": (loaded_page.MYINFO_MENU, loaded_page.MYINFO_HEADER),
        "Performance": (loaded_page.PERFORMANCE_MENU, loaded_page.PERFORMANCE_HEADER),
        "Dashboard":(loaded_page.DASHBOARD_MENU, loaded_page.DASHBOARD_HEADER)
    }

    for menu_name, (menu_loc, header_loc) in menus.items():
        assert loaded_page.is_menu_visible_and_enabled(menu_loc) == True, f"{menu_name} menu not visible/enabled"
        assert loaded_page.click_menu_and_verify(menu_loc, header_loc) == True, f"{menu_name} menu not clickable"
        print(f"{menu_name} menu is visible, enabled and clickable")