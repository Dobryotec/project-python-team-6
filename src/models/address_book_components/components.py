from datetime import datetime

from src.exceptions import DateFormatException, PhoneException


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)    


class Name(Field):
    pass


class Phone(Field):
    def validate_phone(self):
        if not (len(self.value) == 10 and str(self.value).isdigit()):
            raise PhoneException


class Birthday(Field):
    def validate_date(self):
        try:
            datetime.strptime(self.value, "%d.%m.%Y").strftime("%d.%m.%Y")
        except ValueError:
            raise DateFormatException
