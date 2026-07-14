import driver
from selenium.common import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from Utilities import logger

class loginPage:
    username = (By.XPATH,"//input[@name = 'username']")
    password = (By.XPATH, "//input[@name = 'password']")
    login_btn = (By.XPATH, "//button[@type = 'submit']")
    DASHBOARD = (By.XPATH, "//h6[text()= 'Dashboard']")
    USER_DROPDOWN = (By.XPATH, "//p[@class='oxd-userdropdown-name']")
    LOGOUT = (By.XPATH, "//a[text()='Logout']")
    FORGOT_PASSWORD = (By.XPATH, "//p[@class='oxd-text oxd-text--p orangehrm-login-forgot-header']")
    RESET_PASSWORD_HEADER = (By.XPATH, "//h6[text()= 'Reset Password']")
    RESET_EMAILID = (By.XPATH, "//input[@class='oxd-input oxd-input--active']")
    REST_PSWD_BTN = (By.XPATH,"//button[contains(@class,'orangehrm-forgot-password-button--reset')]")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def launch_url(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    def username_visible(self):
        user_element = self.wait.until(EC.visibility_of_element_located(self.username))
        return user_element.is_displayed() and user_element.is_enabled()


    def password_visible(self):
        password_element = self.wait.until(EC.visibility_of_element_located(self.password))
        return password_element.is_displayed() and password_element.is_enabled()

    def enter_username(self, username):
        self.wait.until(EC.visibility_of_element_located(self.username)).send_keys(username)

    def enter_password(self, password):
        self.wait.until(EC.visibility_of_element_located(self.password)).send_keys(password)

    def click_login(self):
        self.wait.until(EC.element_to_be_clickable(self.login_btn)).click()

    def login_success(self):
        try:
            self.wait.until(lambda d: "dashboard" in d.current_url.lower())
            return True
        except TimeoutException:
            return False

    def logout(self):
        self.wait.until(EC.element_to_be_clickable(self.USER_DROPDOWN)).click()
        self.wait.until(EC.element_to_be_clickable(self.LOGOUT)).click()
        self.wait.until(EC.visibility_of_element_located(self.username))

    def forgot_password_link(self):
        self.wait.until(EC.element_to_be_clickable(self.FORGOT_PASSWORD)).click()
        header_element = self.wait.until(EC.presence_of_element_located(self.RESET_PASSWORD_HEADER))
        assert header_element.text == "Reset Password"
        self.wait.until(EC.visibility_of_element_located(self.RESET_EMAILID)).send_keys("user9")
        self.wait.until(EC.element_to_be_clickable(self.REST_PSWD_BTN)).click()
        current_url= self.driver.current_url
        assert "sendPasswordReset" in current_url