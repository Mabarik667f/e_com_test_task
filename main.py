from fastapi import FastAPI
from config import db
from validators import get_types_of_fields

app = FastAPI()


@app.post("/get_form")
def get_form(data: dict[str, str]) -> dict[str, str] | str:
    current_form: dict[str, str] = get_types_of_fields(data)
    res = find_match(current_form)
    return res


def find_match(current_form: dict[str, str]) -> dict[str, str] | str:
    data_set = set(current_form.items())
    for r in db.all():
        r_set = set(r.items())
        intersection = r_set & data_set 
        if len(intersection) == len(r.items()) - 1:
            return r.get("name", "")
    return current_form

