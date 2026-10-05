from  playwright.sync_api import Playwright, expect, Page
class PIM:
    def __init__(self, page:Page):
        self.page=page
        self.pim=page.locator("span.oxd-main-menu-item--name").filter(
            has_text="PIM")
        self.add=page.get_by_role("button", name=" Add ")
        self.addemployee_text=page.get_by_text("Add Employee",exact=True)
        self.firstname=page.get_by_placeholder("First Name")
        self.lastname=page.get_by_placeholder("Last Name")
        self.employee_id=page.locator("input").nth(3)
        self.save=page.get_by_role("button", name=" Save ")
        self.personal_details_text=page.get_by_role("heading", name="Personal Details")
        #self.driver_license_number=page.get_by_label("Driver's License Number")
        self.driver_license_number=page.locator(
            "body > div:nth-child(3) > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > form:nth-child(3) > div:nth-child(3) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > input:nth-child(1)")
        self.licence_expire_date=page.get_by_placeholder("yyyy-dd-mm").nth(0)
        self.button_save=page.locator("button").filter(has_text="Save").first

    def navigate_to_pim(self):
        try:
            self.pim.click()
            expect(self.addemployee_text).to_be_visible()
            print("Navigated to PIM section successfully.")
        except Exception as e:
            print("Exception occurred while navigating to PIM:", str(e))
            self.page.screenshot(path="screenshots/pim_navigation_error.png")  # Capture screenshot on error
    def add_employee(self, first_name, last_name, employee_id):
        try:
            self.add.click()
            self.firstname.fill(first_name)
            self.lastname.fill(last_name)
            self.employee_id.fill(employee_id)
            self.save.click()
            print("Employee added successfully.")
            expect(self.personal_details_text).to_be_visible()
        except Exception as e:
            print("Exception occurred while adding employee:", str(e))
            self.page.screenshot(path="screenshots/add_employee_error.png")
            raise # Capture screenshot on error

    def personal_details(self, driver_license_number, license_expire_date):
        try:
         self.driver_license_number.fill(driver_license_number)
         self.licence_expire_date.fill(license_expire_date)
         self.button_save.click()
        except Exception as e:
            print("Exception occurred while filling personal details:", str(e))
            self.page.screenshot(path="screenshots/personal_details_error.png")
            raise # Capture screenshot on error
