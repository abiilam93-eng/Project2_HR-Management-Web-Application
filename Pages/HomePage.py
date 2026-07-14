from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class homepage:
    ADMIN_MENU = (By.XPATH, "//span[text()='Admin']")
    PIM_MENU = (By.XPATH, "//span[text()='PIM']")
    LEAVE_MENU = (By.XPATH, "//span[text()='Leave']")
    TIME_MENU = (By.XPATH, "//span[text()='Time']")
    RECRUITMENT_MENU = (By.XPATH, "//span[text()='Recruitment']")
    MYINFO_MENU = (By.XPATH, "//span[text()='My Info']")
    PERFORMANCE_MENU = (By.XPATH, "//span[text()='Performance']")
    DASHBOARD_MENU = (By.XPATH, "//span[text()='Dashboard']")

    ADMIN_HEADER = (By.XPATH, "//h6[text()='Admin']")
    PIM_HEADER = (By.XPATH, "//h6[text()='PIM']")
    LEAVE_HEADER = (By.XPATH, "//h6[text()='Leave']")
    TIME_HEADER = (By.XPATH, "//h6[text()='Time']")
    RECRUITMENT_HEADER = (By.XPATH, "//h6[text()='Recruitment']")
    MYINFO_HEADER = (By.XPATH, "//h6[text()='PIM']")
    PERFORMANCE_HEADER = (By.XPATH, "//h6[text()='Performance']")
    DASHBOARD_HEADER = (By.XPATH, "//h6[text()='Dashboard']")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def is_menu_visible_and_enabled(self, locator):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        return element.is_displayed() and element.is_enabled()

    def click_menu_and_verify(self, menu_locator, header_locator):
        menu = self.wait.until(EC.element_to_be_clickable(menu_locator))
        menu.click()
        # Verify page loaded by checking header
        self.wait.until(EC.visibility_of_element_located(header_locator))
        return True