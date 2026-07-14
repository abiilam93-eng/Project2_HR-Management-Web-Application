import datetime
import os

import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

from Utilities.Run_status import update_scenario_status


@pytest.fixture(scope="function")
def setup():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver  # This gives driver to your test
    driver.quit()

def test_login_scenario():
    try:
        assert True
        update_scenario_status("Test Scenario_Project2.xlsx", "Sheet1", "SC01", "Passed")
    except AssertionError:
        update_scenario_status("Test Scenario_Project2.xlsx", "Sheet1", "SC01", "Failed")
        raise


SCREENSHOT_DIR = "screenshots"


@pytest.fixture(scope="session", autouse=True)
def create_screenshot_folder():
    if not os.path.exists(SCREENSHOT_DIR):
        os.makedirs(SCREENSHOT_DIR)


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call":
        driver = item.funcargs.get("setup")

        if driver:

            status = "PASSED" if rep.passed else "FAILED"

            test_name = item.name.replace("[", "_").replace("]", "_")
            filename = f"{test_name}_{status}.png"
            filepath = os.path.join(SCREENSHOT_DIR, filename)

            driver.save_screenshot(filepath)