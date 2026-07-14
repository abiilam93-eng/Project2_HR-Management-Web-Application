import random
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AdminPage:
    ADMIN_MENU = (By.XPATH, "//span[text()='Admin']")
    ADMIN_HEADER = (By.XPATH, "//h6[text()='Admin']")
    PLUS_ADD = (By.XPATH, "//button[@class='oxd-button oxd-button--medium oxd-button--secondary']")

    ADMIN_TABLE_ROWS = (By.XPATH, "//div[@class='oxd-table-card']")
    ADMIN_TABLE_USERNAME_COL = (By.XPATH, ".//div[@role='cell'][2]")

    USER_ROLE_DROPDOWN = (By.XPATH, "(//div[text()='-- Select --'])[1]")
    USER_ROLE_VALUE = (By.XPATH, "//div[text()='ESS']")
    STATUS_DROPDOWN = (By.XPATH, "(//div[@class='oxd-select-text-input'])[2]")
    EMPLOYEE_NAME = (By.XPATH, "//input[@placeholder='Type for hints...']")
    USERNAME = (By.XPATH, "//label[text()='Username']/parent::div/following-sibling::div/input")
    PASSWORD = (By.XPATH, "//label[text()='Password']/parent::div/following-sibling::div/input")
    CONFIRM_PASSWORD = (By.XPATH, "//label[text()='Confirm Password']/parent::div/following-sibling::div/input")
    SAVE_BTN = (By.XPATH, "//button[text()=' Save ']")


    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 30)

    def click_on_admin(self):
        self.wait.until(EC.element_to_be_clickable(self.ADMIN_MENU)).click()
        self.wait.until(EC.visibility_of_element_located(self.ADMIN_HEADER))

    def click_on_PlusAdd(self):
        self.wait.until(EC.element_to_be_clickable(self.PLUS_ADD)).click()

    def user_role(self,role):
        dropdown = self.wait.until(EC.visibility_of_element_located(self.USER_ROLE_DROPDOWN))
        dropdown.click()
        option = (By.XPATH, f"//div[@role='option']//span[text()='{role}']")
        self.wait.until(EC.element_to_be_clickable(option)).click()

    def emp_name(self):
        emp = self.wait.until(EC.visibility_of_element_located(self.EMPLOYEE_NAME))
        emp.send_keys("a")
        first_suggestion = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@role='listbox']//span[1]")))
        first_suggestion.click()

    def status_dropdown(self,status):
        status_field = self.wait.until(EC.visibility_of_element_located(self.STATUS_DROPDOWN))
        status_field.click()
        option = (By.XPATH, f"//div[@role='option']//span[text()='{status}']")
        self.wait.until(EC.element_to_be_clickable(option)).click()

    def new_cred(self, username, password):
        self.wait.until(EC.visibility_of_element_located(self.USERNAME)).send_keys(username)
        self.wait.until(EC.visibility_of_element_located(self.PASSWORD)).send_keys(password)
        self.wait.until(EC.visibility_of_element_located(self.CONFIRM_PASSWORD)).send_keys(password)
        self.wait.until(EC.element_to_be_clickable(self.SAVE_BTN)).click()

    def validate_loaded_page(self):
        self.wait.until(EC.visibility_of_element_located(self.PLUS_ADD))

    def check_for_new_user(self, username):  # Pass the username you created
        self.wait.until(EC.visibility_of_element_located(self.ADMIN_TABLE_ROWS))
        time.sleep(2)
        found=False
        rows = self.driver.find_elements(*self.ADMIN_TABLE_ROWS)
        print(f"Total rows found: {len(rows)}")

        for row in rows:
            try:
                username_cell = row.find_element(*self.ADMIN_TABLE_USERNAME_COL)
                username_in_table = username_cell.text.strip()
                print(f"Checking user: {username_in_table}")
                if username_in_table.lower() == username.lower():  # ignore case
                    return True
            except:
                continue

        return False