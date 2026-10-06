from faker import Faker

fake = Faker()


def generate_employee_data():

    return {
        "first_name": fake.first_name(),
        "last_name": fake.last_name(),
        "employee_id": fake.numerify("#####")
    }

def generate_personal_details():
    return {
        "driver_license_number": fake.bothify(text='??######'),
        "license_expire_date": fake.date(pattern="%Y-%m-%d", end_datetime=None)
    }
def generate_login_data():
    return {
        "username": fake.user_name(),
        "password": fake.password(length=10, special_chars=True, digits=True, upper_case=True, lower_case=True)
    }