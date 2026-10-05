from pages.login import LoginPage
from pages.pim import PIM
import pytest
from utilities.faker_data import generate_employee_data, generate_personal_details


@pytest.fixture
def test_add_employee(page, login_data):

    employee = generate_employee_data()

    login_page = LoginPage(page)
    login_page.navigate()

    login_page.do_login(
        login_data["username"],
        login_data["password"]
    )

    pim_page = PIM(page)
    pim_page.navigate_to_pim()

    pim_page.add_employee(
        employee["first_name"],
        employee["last_name"],
        employee["employee_id"]
            )
    return test_add_employee
def test_personal_details(page, test_add_employee):
    personal_details = generate_personal_details()

    pim_page = PIM(page)
    page.wait_for_timeout(6000)  # Wait for 2 seconds to ensure the page is ready
    pim_page.personal_details(
        personal_details["driver_license_number"],
        personal_details["license_expire_date"]
    )