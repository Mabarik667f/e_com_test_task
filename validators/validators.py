import re
from email_validator import validate_email, EmailNotValidError
from datetime import datetime


class FieldValidator:

    def __init__(self, val: str):
        self.val = val

    def validate(self) -> bool:
        return True

    def email(self) -> bool:
        return EmailChecker(self.val).validate()

    def phone(self) -> bool:
        return PhoneChecker(self.val).validate()

    def date(self, date_format: str) -> bool:
        return DateChecker(self.val, date_format).validate()


class PhoneChecker(FieldValidator):

    phone_regexp = r"^\+7 \d{3} \d{3} \d{2} \d{2}$"

    def validate(self) -> bool:
        return re.fullmatch(self.phone_regexp, self.val) is not None


class EmailChecker(FieldValidator):

    def validate(self) -> bool:
        try:
            validate_email(self.val)
            return True
        except EmailNotValidError:
            return False


class DateChecker(FieldValidator):

    def __init__(self, val: str, date_format: str):
        super().__init__(val)
        self.date_format = date_format

    def validate(self) -> bool:
        try:
            datetime.strptime(self.val, self.date_format)
            return True
        except ValueError:
            return False
