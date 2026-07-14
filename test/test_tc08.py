from Pages.LoginPage import loginPage
from Pages.MyInfoPage import MyInfoPage

def test_tc08_validate_my_info_menu_items(setup):
    driver = setup
    login_page = loginPage(driver)
    my_info = MyInfoPage(driver)

    login_page.launch_url()
    login_page.enter_username("Admin")
    login_page.enter_password("admin123")
    login_page.click_login()

    results = my_info.verify_menu_items()

    failures = [item for item, status in results.items() if not status]
    assert len(failures) == 0, f"Missing items: {failures}"

    print("All My Info menu items are present and clickable")