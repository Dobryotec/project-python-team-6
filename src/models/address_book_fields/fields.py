import re
from datetime import datetime
from src.exceptions import DateFormatException, PhoneException


class Field:
    def __init__(self, value, required=False, max_length=None):
        self.value = value
        self.required = required
        self.max_length = max_length

    def validate(self):
        if self.required and not self.value:
            raise ValueError("This field is required.")
        if self.max_length is not None and len(str(self.value)) > self.max_length:
            raise ValueError(f"This field must be at most {self.max_length} characters long.")
        # Додаткові перевірки

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


class Address(Field):
    def validate_address(self):
        if len(self.value) < 10:
            raise ValueError("The address must contain more then 10 characters")
        if str(self.value).isdigit():
            raise ValueError("The address must contain more than just numbers")
        

class Email(Field):
    def validate_email(self):
        if not re.match(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", self.value):
            raise ValueError("Invalid email format")


class Day(Field):
    def validate_day(self):
        try:
            value = int(self.value)
            if value <= 0:
                print("Days must be a positive number.")
                return None
            else:
                return value
        except ValueError:
            print("Days must be a number.")
            return None
