from playwright.sync_api import Playwright, expect, Page

from pages.dashboard import Dashboard


class LoginPage():
    def __init__(self,page:Page):
        self.page=page
        self.username = page.get_by_placeholder("Username")
        self.password = page.get_by_placeholder("Password")
        self.button= page.get_by_role("button", name="Login")

    def navigate(self):
        self.page.goto(
            "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login",
            wait_until="domcontentloaded",
            timeout=60000
        )

    def do_login(self, username, password):
        try:
         self.username.fill(username)
         self.password.fill(password)
         self.button.click()
        except Exception as e:
            print("Exception occurred while performing login:", str(e))
            self.page.screenshot(path="screenshots/login_error.png")  # Capture screenshot on error
