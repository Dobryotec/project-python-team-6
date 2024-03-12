from src.exceptions import PhoneException, DateFormatException
from src.models.record import Record
from src.models.address_book_fields.fields import Day



def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError as ve:
            return str(ve)
        except KeyError as ke:
            return str(ke)
        except PhoneException:
            return "Phone number must contain 10 digits"
        except DateFormatException:
            return "Following date format required: DD.MM.YYYY"
    return inner


def parse_input(user_input):
    command, *args = user_input.split()
    command = command.strip().lower()
    return command, *args


@input_error
def add_contact(args, book):
    name, phone = args
    record = book.find(name)
    if record != 'Contact not found':
        record.add_phone(phone)
    else:
        record = Record(name)
        record.add_phone(phone)
        book.add_record(record)

    return "Contact added."


@input_error
def change_contact(args, address_book):
    name, old_phone, new_phone = args
    if name in address_book:
        address_book[name].edit_phone(old_phone, new_phone)
        return "Contact changed"
    else:
        raise KeyError(f"Contact with name {name} doesn't exist yet")


@input_error
def show_phone(args, address_book):
    name = args[0]
    if name in address_book:
        record = address_book[name]
        return f"Phones of {name}: {', '.join(phone.value for phone in record.phones)}"
    else:
        raise KeyError(f"Contact with name {name} doesn't exist yet")


@input_error
def show_all_contacts(address_book):
    if address_book.values():
        for record in address_book.values():
            print(f'{record}')
    else:
        return "You don't have any contacts yet"


@input_error
def add_birthday(args, address_book):
    name, birthday = args
    if name in address_book:
        address_book[name].add_birthday(birthday)
        return f"Birthday added for {name}"
    else:
        raise KeyError(f"Contact with {name} doesn't exist")


@input_error
def show_birthday(args, address_book):
    name = args[0]
    if name in address_book and address_book[name].birthday:
        return f"Birthday of {name}: {address_book[name].birthday}"
    else:
        raise KeyError(f"Contact with {name} doesn't exist or birthday not set")


@input_error
def birthdays(book):
     days = Day.validate_day("Enter number of days: ")

     birthdays_within_days = book.get_birthdays_within_days(days)

     if birthdays_within_days:
        output = ""
        for birthday_date, names in birthdays_within_days.items():
            output += f"{birthday_date.strftime('%A, %d %B')}: {', '.join(names)}\n"
        return output
     else:
        return "No upcoming birthdays"
