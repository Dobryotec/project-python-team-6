from src.introduction_dialogs import introduction, last_donation_dialog
from src.models.notes import Notes
from src.models.address_book import AddressBook
from src.bot_commands import *
from src.utils.show_message_dialog import show_message_dialog
from src.utils.show_input_dialog import show_input_dialog
from src.utils.files_methods import load_from_file, save_to_file


def main():
    book = AddressBook()
    notes = Notes()
    load_from_file("data.pkl", book, notes)
    user_name = introduction()

    while True:
        user_input = show_input_dialog(f"How can I assist you, {user_name}?", 'Будь ласка, введіть вашу команду:')
        if user_input is None:
            break

        command, *args = parse_input(user_input)
        if command in ["close", "exit"]:
            last_donation_dialog()
            save_to_file("data.pkl", book.data, notes.notes)
            break

        elif command == "help":
            response = help()
        elif command == "hello":
            response = "How can I help you?"
        elif command == "add-contact":
            response = add_contact(args, book)
        elif command == "change-phone":
            response = change_contact(args, book)
        elif command == "show-phone":
            response = show_phone(args, book)
        elif command == "all-contacts":
            response = show_all_contacts(book)
        elif command == "add-birthday":
            response = add_birthday(args, book)
        elif command == "show-birthday":
            response = show_birthday(args, book)
        elif command == "birthdays":
            response = birthdays(book)
        elif command == "add-address":
            response = add_address(args, book)
        elif command == "show-address":
            response = show_address(args, book)
        elif command == "add-email":
            response = add_email(args, book)
        elif command == "show-email":
            response = show_email(args, book)
        elif command == "change-email":
            response = change_email(args, book)
        elif command == "find-contact":
            response = find_contact(args, book)
        elif command == "delete-contact":
            response = delete_contact(args, book)
        elif command == "add-note":
            response = add_note(notes)
        elif command == "delete-note":
            response = delete_note(notes)
        elif command == "find-note":
            response = find_note(notes)
        elif command == "find-note-by-tag":
            response = find_note_by_tag(notes)
        elif command == "update-note-by-title":
            response = update_note_by_title(notes)
        elif command == "show-notes":
            response = show_notes(notes)
        else:
            response = "Некоректна команда. Щоб переглянути перелік команд, введіть 'help'"

        show_message_dialog('Personal Assistant Diia', response)

    # При виході з програми зберігаємо дані у файл
    save_to_file("data.pkl", book.data, notes.notes)


if __name__ == "__main__":
    main()
