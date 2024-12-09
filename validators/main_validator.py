from .validators import FieldValidator


def get_types_of_fields(data: dict[str, str]) -> dict[str, str]:
    current_form: dict[str, str] = dict()
    validators: list[tuple] = [
        (lambda val: FieldValidator(val).phone(), "phone"),
        (lambda val: FieldValidator(val).email(), "email"),
        (lambda val: FieldValidator(val).date("%Y-%m-%d"), "date"),
        (lambda val: FieldValidator(val).date("%d.%m.%Y"), "date"),
    ]
    for key, val in data.items():
        for validator, data_type in validators:
            if validator(val):
                current_form[key] = data_type
                break
        else:
            current_form[key] = "text"

    return current_form
