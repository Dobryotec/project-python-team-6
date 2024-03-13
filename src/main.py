from src.models.address_book import AddressBook
from src.bot_commands import *
from src.utils.show_message_dialog import show_message_dialog
from src.utils.show_input_dialog import show_input_dialog


def main():
    book = AddressBook()
    book.load_from_file("addressbook.pkl")
    
    show_message_dialog('Assistant Bot', "Welcome to the assistant bot!")

    while True:
        user_input = show_input_dialog('Enter a command', 'Please enter your command:')

        if user_input is None: 
            break

        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            response = "Good bye!"
            show_message_dialog('Assistant Bot Response', response)
            book.save_to_file("addressbook.pkl")
            break

        elif command == "help":
            response = help_me()
        elif command == "hello":
            response = "How can I help you?"
        elif command == "add":
            response = add_contact(args, book)
        elif command == "change":
            response = change_contact(args, book)
        elif command == "phone":
            response = show_phone(args, book)
        elif command == "all":
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
            response = add_note(book)
        elif command == "delete-note":
            response = delete_note(args, book)
        elif command == "find-note":
            response = find_note(args, book)
        elif command == "find-by-tag":
            response = find_note_by_tag(args, book)
        else:
            response = "Invalid command"
        
        show_message_dialog('Assistant Bot Response', response)

    # При виході з програми зберігаємо дані у файл
    book.save_to_file("addressbook.pkl")


if __name__ == "__main__":
    main()
