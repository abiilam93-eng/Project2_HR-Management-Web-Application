from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class MyInfoPage:
    MY_INFO_MENU = (By.XPATH, "//span[text()='My Info']")

    MENU_ITEMS = {
        "Personal Details": (By.XPATH, "//a[text()='Personal Details']"),
        "Contact Details": (By.XPATH, "//a[text()='Contact Details']"),
        "Emergency Contacts": (By.XPATH, "//a[text()='Emergency Contacts']"),
        "Dependents": (By.XPATH, "//a[text()='Dependents']"),
        "Immigration": (By.XPATH, "//a[text()='Immigration']"),
        "Job": (By.XPATH, "//a[text()='Job']"),
        "Salary": (By.XPATH, "//a[text()='Salary']"),
        "Report-to": (By.XPATH, "//a[text()='Report-to']"),
        "Qualifications": (By.XPATH, "//a[text()='Qualifications']"),
        "Memberships": (By.XPATH, "//a[text()='Memberships']")
    }

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def go_to_my_info(self):
        self.wait.until(EC.element_to_be_clickable(self.MY_INFO_MENU)).click()

    def verify_menu_items(self):
        self.go_to_my_info()

        results = {}
        for item_name, locator in self.MENU_ITEMS.items():
            try:
                element = self.wait.until(EC.element_to_be_clickable(locator))
                results[item_name] = True
                print(f"{item_name} is present and clickable")
            except:
                results[item_name] = False
                print(f"{item_name} is missing or not clickable")

        return results