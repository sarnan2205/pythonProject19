from pages.login import LoginPage
from pages.dashboard import Dashboard


def test_valid_login(page, login_data):

    username = login_data["username"]
    password = login_data["password"]

    login_page = LoginPage(page)
    dashboard = Dashboard(page)

    login_page.navigate()
    login_page.do_login(username, password)

    dashboard.verify_dashboard()