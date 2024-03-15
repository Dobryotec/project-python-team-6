from src.exceptions import PhoneException, DateFormatException
from src.models.record import Record
from src.models.address_book_fields.fields import Day

from tabulate import tabulate
from src.utils.commands_list import commands_l

from src.utils.show_input_dialog import show_input_dialog

DEFAULT_INPUT_MESSAGE = 'Введіть команду.'


def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Введіть корректні дані."
        except KeyError as ke:
            return str(ke)
        except IndexError:
            return "Введіть значення."
        except PhoneException:
            return "Номер телефону має складатися з 10 цифр."
        except DateFormatException:
            return "Формат дати має виглядати так: DD.MM.YYYY"

    return inner


@input_error
def parse_input(user_input):
    command, *args = user_input.split()
    command = command.strip().lower()
    return command, *args


@input_error
def add_contact(args, address_book):
    name, phone = args
    if name in address_book:
        phones = [p.value for p in address_book[name].phones]
        if phone in phones:
            return "Номер для цього контакту вже існує."
        else:
            address_book[name].add_phone(phone)
    else:
        record = Record(name)
        record.add_phone(phone)
        address_book.add_record(record)

    return "Контакт додано."


@input_error
def find_contact(args, address_book):
    value = args[0]
    return address_book.find(value)


@input_error
def change_contact(args, address_book):
    name, old_phone, new_phone = args
    if name in address_book:
        address_book[name].edit_phone(old_phone, new_phone)
        return "Контакт змінено."
    else:
        raise KeyError(f"Контакту з ім'ям '{name}' не існує.")


@input_error
def delete_contact(args, address_book):
    name = args[0]
    if name in address_book:
        address_book.delete(name)
        return f"Контакт '{name}' успішно видалено."
    else:
        raise KeyError(f"Контакту з ім'ям '{name}' не існує.")
    

@input_error
def add_email(args, address_book):
    name, email = args
    if name in address_book:
        address_book[name].add_email(email)
        return f"Email додано до контакту '{name}'."
    else:
        raise KeyError(f"Контакту з ім'ям '{name}' не існує.")


@input_error
def change_email(args, address_book):  
    name, new_email = args
    if name in address_book:
        address_book[name].edit_email(new_email)
        return "Електронну пошту змінено."
    else:
        raise KeyError(f"Контакту з ім'ям '{name}' не існує.")
    

@input_error
def show_email(args, address_book):
    name = args[0]
    if name in address_book and address_book[name].email:
        return f"Email контакту '{name}': {address_book[name].email.value}"
    else:
        raise KeyError(f"Контакту з ім'ям '{name}' не існує або адреса електронної пошти для цього контакту не задана.")


@input_error
def show_phone(args, address_book):
    name = args[0]
    if name in address_book:
        record = address_book[name]
        return f"Номер телефону контакту '{name}': {', '.join(phone.value for phone in record.phones)}"
    else:
        raise KeyError(f"Контакту з ім'ям '{name}' ще не існує.")


@input_error
def show_address(args, address_book):
    name = args[0]
    if name in address_book:
        record = address_book[name]
        return f"Адреса контакту '{name}': {record.address.value}"
    else:
        raise KeyError(f"Контакту з ім'ям '{name}' ще не існує.")


@input_error
def show_all_contacts(address_book):
    contacts_info = ""
    if address_book.values():
        for record in address_book.values():
            contacts_info += f'{record}\n' 
    else:
        contacts_info = "У Вас ще немає жодного контакту."

    return contacts_info 


@input_error
def add_birthday(args, address_book):
    name, birthday = args
    if name in address_book:
        address_book[name].add_birthday(birthday)
        return f"День народження додано до контакту '{name}'"
    else:
        raise KeyError(f"Контакту з ім'ям '{name}' не існує.")


@input_error
def add_address(args, address_book):
    name, *address = args
    if name in address_book:
        address_book[name].add_address(' '.join(address))
        return f"Адресу додано до контакту '{name}'"
    else:
        raise KeyError(f"Контакту з ім'ям '{name}' не існує.")


@input_error
def show_birthday(args, address_book):
    name = args[0]
    if name in address_book and address_book[name].birthday:
        return f"День народження контакту '{name}': {address_book[name].birthday}"
    else:
        raise KeyError(f"Контакту з ім'ям '{name}' не існує або дата народження для цього контакту не задана.")


@input_error
def birthdays(book):
    while True:
        value = show_input_dialog(DEFAULT_INPUT_MESSAGE, "Введіть кількість днів: ")
        day = Day(value)
        validated_day = day.validate_day()
        if validated_day is not None:
            birthdays_within_days = book.get_birthdays_within_days(validated_day)
            if birthdays_within_days:
                output = ""
                for birthday_date, names in birthdays_within_days.items():
                    output += f"{birthday_date.strftime('%A, %d %B')}: {', '.join(names)}\n"
                return output
            else:
                return "Немає найближчих днів народження"


@input_error
def add_note(notes):
    title = show_input_dialog(DEFAULT_INPUT_MESSAGE, "Введіть заголовок: ")
    text = show_input_dialog(DEFAULT_INPUT_MESSAGE, "Введіть текст (необов'язково): ")
    tags = show_input_dialog(DEFAULT_INPUT_MESSAGE, "Введіть теги через кому (необов'язково): ")
    notes.add_note(title, text, tags)
    return f"Примітка з заголовком: '{title}' успішно додана."


@input_error
def delete_note(args, notes):
    title = args[0]
    return notes.delete_note_by_title(title)


@input_error
def find_note(args, notes):
    title = args[0]
    return notes.find_note_by_title(title)


@input_error
def find_note_by_tag(args, address_book):
    tag = args[0]
    return address_book.find_note_by_tag(tag)


def help_me():
    print("\033[94m", "Доступні команди:", "\033[0m")
    command_d = dict(sorted(commands_l.items()))

    hlp_tbl_headers = [
        "Команда",
        "Приклад",
    ]
    hlp_tbl = [
        [
            command,
            info["example"],
        ]
        for command, info in command_d.items()
    ]
    return tabulate(hlp_tbl, hlp_tbl_headers, tablefmt="rounded_grid")
