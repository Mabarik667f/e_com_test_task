from config import db


def insert_values() -> None:
    db.insert(
        {
            "name": "Register form template",
            "email": "email",
            "user_name": "text",
            "password": "text",
            "password2": "text",
        }
    )
    db.insert({"name": "Login form template", "email": "email", "password": "text"})
    db.insert(
        {
            "name": "Create order form template",
            "created": "date",
            "product": "text",
            "address": "text",
            "phone_for_order": "phone",
        }
    )
    db.insert(
        {
            "name": "Order history form template",
            "username": "text",
            "order": "text",
            "phone": "phone",
        }
    )


if __name__ == "__main__":
    insert_values()
