from main import app
from fastapi.testclient import TestClient


client = TestClient(app)


def test_unknown_form():
    data = {
        "additionalProp1": "string",
        "additionalProp2": "+7 444 333 22 11",
        "additionalProp3": "test.example@gmail.com",
        "date": "2024-11-26",
        "date2": "26.11.2024",
    }
    res = {
        "additionalProp1": "text",
        "additionalProp2": "phone",
        "additionalProp3": "email",
        "date": "date",
        "date2": "date",
    }
    response = client.post("/get_form", json=data)
    assert response.json() == res



def test_register_form():
    data = {
        "email": "test.example@gmail.com",
        "user_name": "Name",
        "password": "password",
        "password2": "password",
    }

    response = client.post("/get_form", json=data)
    assert response.json() == "Register form template"

def test_create_order_form():
    data = {
        "created": "2024-11-12",
        "product": "Product",
        "address": "Address",
        "phone_for_order": "+7 999 888 77 66",
    }

    response = client.post("/get_form", json=data)
    assert response.json() == "Create order form template"
def test_login_form():
    data = {"email": "test.example@gmail.com", "password": "password"}

    response = client.post("/get_form", json=data)

    assert response.json() == "Login form template"

def test_order_history_form():
    data = {
        "user_name": "Name",
        "order": "Order",
        "phone": "+7 111 222 33 44",
    }

    response = client.post("/get_form", json=data)
    assert response.json() == "Order history form template"
