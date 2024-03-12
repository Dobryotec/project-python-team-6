from src.models.address_book_fields.fields import *


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []  
        self.birthday = None

    def add_phone(self, phone):
        phone_obj = Phone(phone)
        phone_obj.validate_phone()
        self.phones.append(phone_obj)

    def remove_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                self.phones.remove(p)
                break

    def edit_phone(self, old_phone, new_phone):
        for p in self.phones:
            if p.value == old_phone:
                p.value = new_phone
                break
    
    def find_phone(self, phone):      
        for p in self.phones:
            if p.value == phone:
                return phone
    
    def add_birthday(self, birthday):
        birthday_obj = Birthday(birthday)      
        birthday_obj.validate_date()
        self.birthday = birthday_obj

    def __str__(self):
        phones_info = '; '.join(p.value for p in self.phones)
        if self.birthday is not None:
            birthday_info = f", birthday: {self.birthday.value}"
        else:
            birthday_info = ""   
        return f"Contact name: {self.name.value}, phones: {phones_info}{birthday_info}"
