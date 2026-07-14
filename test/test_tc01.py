import os
from selenium.webdriver.support.wait import WebDriverWait

from Pages.LoginPage import loginPage
from Utilities import logger

def test_tc01_login_with_multiple_credentials(setup):
    driver = setup
    url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
    base_dir = os.path.dirname(os.path.abspath(__file__))
    excel_file = os.path.join("test","Test Data.xlsx")
    sheet_name = "Sheet1"

    total_rows = logger.get_row_count(excel_file, sheet_name)

    for r in range(2, total_rows+1):
        try:
            driver.get(url)
            username = logger.read_data(excel_file, sheet_name, r, 6)
            password = logger.read_data(excel_file, sheet_name, r, 7)
            login_pg = loginPage(driver)
            login_pg.enter_username(username)
            login_pg.enter_password(password)
            login_pg.click_login()

            if login_pg.login_success():
                logger.write_result(excel_file, sheet_name, r, "PASS")

            else:
                logger.write_result(excel_file, sheet_name, r, "FAIL")

        except Exception as e:
            print(f"Row {r} failed due to: {e}")
            logger.write_result(excel_file, sheet_name, r, "FAIL")
            continue
