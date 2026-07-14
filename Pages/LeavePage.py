from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import visibility_of_element_located
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class LeavePage:
    LEAVE_MENU = (By.XPATH, "//span[text()='Leave']")
    ASSIGN_LEAVE_SUBMENU = (By.XPATH, "//a[text()='Assign Leave']")
    EMPLOYEE_NAME = (By.XPATH, "//input[@placeholder='Type for hints...']")
    LEAVE_TYPE_DROPDOWN = (By.XPATH, "(//div[@class='oxd-select-text--after'])[1]")
    FROM_DATE = (By.XPATH, "(//input[@placeholder='yyyy-dd-mm'])[1]")
    TO_DATE = (By.XPATH, "//label[text()='To Date']/../following-sibling::div//child::div/*[@placeholder='yyyy-dd-mm']")
    ASSIGN_BTN = (By.XPATH, "//button[text()=' Assign ']")
    OK_BTN = (By.XPATH, "//button[contains(@class,'oxd-button--secondary orangehrm-button-margin') and text()=' Ok ']")
    LEAVE_STATUS = (By.XPATH, "(//div[text()='-- Select --'])[1]")
    STATUS_SCHEDULED = (By.XPATH, "//div[@role='listbox']//span[text()='Scheduled']")
    SEARCH_BTN = (By.XPATH, "//button[text()=' Search ']")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def go_to_assign_leave(self):
        time.sleep(2)
        leave_menu = self.wait.until(EC.element_to_be_clickable(self.LEAVE_MENU))
        leave_menu.click()
        # self.driver.execute_script("arguments[0].click();", leave_menu)
        time.sleep(1)
        self.wait.until(EC.element_to_be_clickable(self.ASSIGN_LEAVE_SUBMENU)).click()

    def assign_leave(self, emp_name,leave_type):
        emp_field = self.wait.until(EC.visibility_of_element_located(self.EMPLOYEE_NAME))
        emp_field.send_keys(emp_name)
        emp_suggestion = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@role='listbox']//span[1]")))
        emp_suggestion.click()

        # Leave type
        self.wait.until(EC.visibility_of_element_located(self.LEAVE_TYPE_DROPDOWN)).click()
        leave_option = (By.XPATH, f"//div[@role='listbox']//span[text()='{leave_type}']")
        self.wait.until(EC.element_to_be_clickable(leave_option)).click()

        from_date=self.wait.until(EC.visibility_of_element_located(self.FROM_DATE))
        from_date.clear()
        from_date.send_keys("2026-17-07")
        from_date.send_keys(Keys.TAB)
        to_date=self.wait.until(EC.visibility_of_element_located(self.TO_DATE))
        to_date.send_keys(Keys.CONTROL+"a")
        to_date.send_keys(Keys.BACKSPACE)
        time.sleep(1)
        to_date.send_keys("2026-20-07")
        to_date.send_keys(Keys.TAB)

        self.wait.until(EC.element_to_be_clickable(self.ASSIGN_BTN)).click()
        time.sleep(1)

    def confirmation_popup(self):
        self.wait.until(EC.element_to_be_clickable(self.OK_BTN)).click()

    def check_leave_list(self, emp_name):
        self.driver.find_element(By.XPATH, "//a[text()='Leave List']").click()
        time.sleep(1)

        self.wait.until(EC.visibility_of_element_located(self.LEAVE_STATUS)).click()
        self.wait.until(EC.element_to_be_clickable(self.STATUS_SCHEDULED)).click()

        self.wait.until(EC.element_to_be_clickable(self.SEARCH_BTN)).click()

        records = self.driver.find_elements(By.XPATH, "//div[@class='orangehrm-paper-container']")
        for row in records:
            cells = row.find_elements(By.XPATH, ".//div[@role='cell']")
            if emp_name in cells[2].text:
                return True
        return False