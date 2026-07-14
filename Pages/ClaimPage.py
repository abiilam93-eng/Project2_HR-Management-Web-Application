from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class ClaimPage:
    CLAIM_MENU = (By.XPATH, "//a//span[text()='Claim']")  # <-- FIXED
    ASSIGN_CLAIM_BTN = (By.XPATH, "//button[normalize-space()='Assign Claim']")  # <-- This is a button, not submenu
    EMPLOYEE_NAME = (By.XPATH, "//input[@placeholder='Type for hints...']")
    EVENT_DROPDOWN = (By.XPATH, "(//div[@class='oxd-select-text-input'])[1]")
    CURRANCY = (By.XPATH, "(//div[@class='oxd-select-text-input'])[2]")
    CREATE_BTN = (By.XPATH, "//button[text()=' Create ']")  # Demo uses Save
    SUBMIT_BTN = (By.XPATH, "//button[text()=' Submit ']")
    SUCCESS_MSG = (By.XPATH, "//p[contains(@class,'oxd-toast-content-text')]")
    CLAIM_HISTORY_LIST = (By.XPATH, "//div[@class='oxd-table-body']//div[@role='row']")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    def go_to_claim(self):
        # Wait for dashboard
        self.wait.until(EC.visibility_of_element_located((By.XPATH, "//h6[text()='Dashboard']")))
        time.sleep(2)

        # Click Claim menu with JS to avoid overlay
        claim_menu = self.wait.until(EC.presence_of_element_located(self.CLAIM_MENU))
        self.driver.execute_script("arguments[0].click();", claim_menu)
        time.sleep(1)

    def create_claim(self, emp_name, event):
        self.wait.until(EC.element_to_be_clickable(self.ASSIGN_CLAIM_BTN)).click()        # Assign Claim

        emp_field = self.wait.until(EC.visibility_of_element_located(self.EMPLOYEE_NAME))
        emp_field.send_keys(emp_name)
        emp_suggestion = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@role='listbox']//span[1]")))
        emp_suggestion.click()

        self.wait.until(EC.element_to_be_clickable(self.EVENT_DROPDOWN)).click()
        time.sleep(1)
        type_option = (By.XPATH, f"//div[@role='option']//span[text()='{event}']")
        self.wait.until(EC.element_to_be_clickable(type_option)).click()

        self.wait.until(EC.visibility_of_element_located(self.CURRANCY)).click()
        time.sleep(1)
        cur_dropdown = (By.XPATH, "//div[@role='option']//span[contains(text(),'Indian Rupee')]")
        self.wait.until(EC.element_to_be_clickable(cur_dropdown)).click()
        self.wait.until(EC.element_to_be_clickable(self.CREATE_BTN)).click()    #create button
        time.sleep(1)

    def submit_assigned_claim(self):
        element= self.wait.until(EC.visibility_of_element_located(self.SUBMIT_BTN))
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        self.wait.until(EC.element_to_be_clickable(self.SUBMIT_BTN)).click()
        time.sleep(1)


    def verify_claim_submission(self):
        msg = self.wait.until(EC.visibility_of_element_located(self.SUCCESS_MSG)).text
        assert "Success" in msg, f"Expected success message, got: {msg}"
        print("Claim submitted successfully")
        time.sleep(2)  # wait for toast to disappear

