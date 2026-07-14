import pytest
from Pages.LoginPage import loginPage
from Pages.ClaimPage import ClaimPage

def test_tc10_claim_request(setup):
    driver = setup
    login = loginPage(driver)
    login.launch_url()
    login.enter_username("Admin")
    login.enter_password("admin123")
    login.click_login()

    claim_page = ClaimPage(driver)
    claim_page.go_to_claim()

    # Fill claim details
    claim_page.create_claim(
        emp_name="Ranga Akunuri",
        event ="Medical Reimbursement",  # check dropdown for exact text
        )

    claim_page.submit_assigned_claim()
    claim_page.verify_claim_submission()