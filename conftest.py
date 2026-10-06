import json
from pathlib import Path

import pytest


def load_login_data():
    file_path = Path("test_data") / "login_credential.json"

    with open(file_path, "r") as file:
        data = json.load(file)

    return data["user_credentials"]


@pytest.fixture(params=load_login_data())
def login_data(request):
    return request.param