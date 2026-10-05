from playwright.sync_api import Page, expect


class Dashboard:

    def __init__(self, page: Page):
        self.page = page

        self.dashboard_header = page.locator(
            ".oxd-text.oxd-text--h6.oxd-topbar-header-breadcrumb-module"
        )

    def verify_dashboard(self):
        expect(self.dashboard_header).to_have_text("Dashboard")