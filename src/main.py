from card.validate_card import Card
from models.notes import Notes
from src.models.address_book import AddressBook
from src.bot_commands import *
from src.utils.show_message_dialog import show_message_dialog
from src.utils.show_input_dialog import show_input_dialog
from utils.files_methods import load_from_file, save_to_file


def main():
    book = AddressBook()
    notes = Notes()
    load_from_file("data.pkl", book, notes)

    show_message_dialog('Personal Assistant Diia', "Bac вітає Особистий помічник Дія!")
    user_name = show_input_dialog('Enter your name', 'Як до Bac можна звертатися?')

    user_input = None
    show_message_dialog('Personal Assistant Diia', f"Вітаю, {user_name}! Наш бот абсолютно безкоштовний, але ми також маємо розширену версію, яка працює за донат.")

    while user_input not in ['1', '2']:
        user_input = show_input_dialog('Choose an option', 'Зробіть вибір:\n1. Безкоштовна версія\n2. Розширена версія за донат')

        if user_input not in ['1', '2']:
            show_message_dialog('Error', 'Введіть "1" або "2".')

    if user_input == '1':
        show_message_dialog('Personal Assistant Diia', f"{user_name}, Ви обрали безкоштовну версію.")
        show_message_dialog('Personal Assistant Diia', "Ми від усієї команди бажаємо Вам вдалого дня!")
        show_message_dialog('Personal Assistant Diia', "Ha цьому функціонал безкоштовної версії скінчився.")

        user_input = None
        while user_input not in ['1', '2']:
           user_input = show_input_dialog('Exit or Donate?', 'Що Ви бажаєте зробити?\n1.Вийти\n2.Придбати розширену версію за донат')
           if user_input not in ['1', '2']:
               show_message_dialog('Error', 'Введіть "1" або "2".')

        if user_input == '1':
             show_message_dialog('Personal Assistant Diia', f"{user_name}, тепер yci знають, хто не донатить. Але дякуємо, що обрали наш бот! До побачення!")
             exit()

    if user_input == '2':
        show_message_dialog('Personal Assistant Diia', f"{user_name}, Ви зробили правильний вибір!")

    try:
        card = Card()
        card.validate_card()
    except ValueError as e:
        show_message_dialog('Error', str(e))
        return

    donation_choice = None

    while donation_choice not in ['1', '2']:
        donation_choice = show_input_dialog('Виберіть суму донату', 'Будь ласка, оберіть суму донату:\n1. 10 грн\n2. 10 000$')

        if donation_choice not in ['1', '2']:
            show_message_dialog('Error', 'Введіть "1" або "2"')

    if donation_choice == '1':
        show_message_dialog('Personal Assistant Diia', "Дякуємо за ваш донат y розмірі 10 грн!")
        show_message_dialog('Personal Assistant Diia', "Вам надано доступ до Personal Assistant Diia")
    elif donation_choice == '2':
        show_message_dialog('Personal Assistant Diia', "Дякуємо за ваш щедрий донат y розмірі 10 000$!")
        show_message_dialog('Personal Assistant Diia', "Ha жаль, ми виявили підозріло велику суму на вашому рахунку.")
        show_message_dialog('Personal Assistant Diia', "Ваші дані були відправлені Державній податковій службі України!")
        show_message_dialog('Personal Assistant Diia', "Але є i хороша новина - Ви тепер можете користуватися ботом!")
        show_message_dialog('Personal Assistant Diia', "Вам надано доступ до Personal Assistant Diia")

    while True:
        user_input = show_input_dialog(f"How can I assist you, {user_name}?", 'Будь ласка, введіть вашу команду:')

        if user_input is None:
            break

        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            response = "Перед виходом з боту пропонуємо Вам зробити внесок до перемоги."
            show_message_dialog('Assistant Bot Response', response)
            donation_response = show_input_dialog('Donate?', 'Виберіть опцію:\n1. Донат 100 грн \n2. Ваші дані будуть відправлені до ТЦК')

            if donation_response == '1':
                show_message_dialog('Personal Assistant Diia', "Дякуємо, що обрали наш бот i за внесок до перемоги!")

            if donation_response == '2':
                show_message_dialog('Personal Assistant Diia', "Ваші дані успішно відправлені до найближчого ТЦК. Дякуємо, що обрали наш бот i за майбутній внесок до перемоги!")

            # book.save_to_file("addressbook.pkl")
            save_to_file("data.pkl", book.data, notes.notes)
            break

        elif command == "help":
            response = help_me()
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
            response = delete_note(args, notes)
        elif command == "find-note":
            response = find_note(args, notes)
        elif command == "find-note-by-tag":
            response = find_note_by_tag(args, notes)
        else:
            response = "Некоректна команда. Щоб переглянути перелік команд, введіть 'help'"

        show_message_dialog('Personal Assistant Diia', response)

    # При виході з програми зберігаємо дані у файл
    save_to_file("data.pkl", book.data, notes.notes)


if __name__ == "__main__":
    main()
