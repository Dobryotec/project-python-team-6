from src.models.address_book_fields.fields import *


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []  
        self.birthday = None
        self.address = None
        self.email = None

    def add_phone(self, phone):
        phone_obj = Phone(phone)
        phone_obj.validate_phone()
        self.phones.append(phone_obj)

    def remove_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                self.phones.remove(p)

    def edit_phone(self, old_number, new_number):
        if old_number in [p.value for p in self.phones]:
            self.remove_phone(old_number)
            self.add_phone(new_number)
    
    def find_phone(self, phone):      
        for p in self.phones:
            if p.value == phone:
                return phone
    
    def add_birthday(self, birthday):
        birthday_obj = Birthday(birthday)      
        birthday_obj.validate_date()
        self.birthday = birthday_obj

    def add_address(self, address):
        address = Address(address)
        address.validate_address()
        self.address = address

    def add_email(self, email):
        email_obj = Email(email)
        email_obj.validate_email()
        self.email = email_obj

    def edit_email(self, new_email):
        email_obj = Email(new_email)
        email_obj.validate_email()
        self.email = email_obj    

    def __str__(self):
        phones_info = '; '.join(p.value for p in self.phones)
        if self.birthday is not None:
            birthday_info = f", день народження: {self.birthday.value}"
        else:
            birthday_info = "" 
        if self.email is not None:
            email_info = f", email: {self.email.value}"
        else:
            email_info = ""
        address_info = f", адреса: {self.address.value}" if self.address else ""
        return (
            f"Ім'я контакту: {self.name.value}, номер телефону: "
            f"{phones_info}{birthday_info}{email_info}{address_info}"
        )
