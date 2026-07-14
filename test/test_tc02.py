from selenium import webdriver
from pytest_html import selfcontained_report

from Pages.LoginPage import loginPage

def test_tc02_URL_accessible(setup):
    driver = setup
    login_page = loginPage(driver)
    login_page.launch_url()
    assert driver.title == "OrangeHRM"
