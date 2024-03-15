from src.card.validate_card import Card
from src.utils.show_input_dialog import show_input_dialog
from src.utils.show_message_dialog import show_message_dialog
from src.utils.files_methods import load_name_from_file, save_name_to_file

PERSONAL_ASSISTANT_TITLE = 'Personal Assistant Diia'
VALID_CHOICE = ['1', '2']
exiting_user = load_name_from_file() != None


def greeting_dialog():
    show_message_dialog(PERSONAL_ASSISTANT_TITLE, "Bac вітає Особистий помічник Дія!")
    if exiting_user:
        user_name = load_name_from_file()
        return user_name
    else:
        user_name = show_input_dialog('Enter your name', 'Як до Bac можна звертатися?')
        save_name_to_file(user_name)
        return user_name


def free_version_dialog(user_name):
    show_message_dialog(PERSONAL_ASSISTANT_TITLE, f"{user_name}, Ви обрали безкоштовну версію.")
    show_message_dialog(PERSONAL_ASSISTANT_TITLE, "Ми від усієї команди бажаємо Вам вдалого дня!")
    show_message_dialog(PERSONAL_ASSISTANT_TITLE, "Ha цьому функціонал безкоштовної версії скінчився.")

    user_input = None
    while user_input not in VALID_CHOICE:
        user_input = show_input_dialog(
            'Exit or Donate?', 'Що Ви бажаєте зробити?\n1.Вийти\n2.Придбати розширену версію за донат'
        )
        if user_input not in VALID_CHOICE:
            show_message_dialog('Error', 'Введіть "1" або "2".')

    if user_input == '1':
        show_message_dialog(
            PERSONAL_ASSISTANT_TITLE, f"{user_name}, тепер yci знають, хто не донатить. "
                                      f"Але дякуємо, що обрали наш бот! До побачення!"
        )
        exit()


def chose_version_dialog(user_name):
    user_input = None
    show_message_dialog(
        PERSONAL_ASSISTANT_TITLE, f"Вітаю, {user_name}! Наш бот абсолютно безкоштовний, "
                                  f"але ми також маємо розширену версію, яка працює за донат."
    )

    while user_input not in VALID_CHOICE:
        user_input = show_input_dialog(
            'Choose an option', 'Зробіть вибір:\n1. Безкоштовна версія\n2. Розширена версія за донат'
        )

        if user_input not in VALID_CHOICE:
            show_message_dialog('Error', 'Введіть "1" або "2".')

    if user_input == '1':
        free_version_dialog(user_name)

    if user_input == '2':
        show_message_dialog(PERSONAL_ASSISTANT_TITLE, f"{user_name}, Ви зробили правильний вибір!")


def fill_card_data():
    try:
        card = Card()
        card.validate_card()
    except ValueError as e:
        show_message_dialog('Error', str(e))
        return


def donation_dialog():
    donation_choice = None
    while donation_choice not in VALID_CHOICE:
        donation_choice = show_input_dialog(
            'Виберіть суму донату', 'Будь ласка, оберіть суму донату:\n1. 10 грн\n2. 10 000$'
        )

        if donation_choice not in VALID_CHOICE:
            show_message_dialog('Error', 'Введіть "1" або "2"')

    if donation_choice == '1':
        show_message_dialog(PERSONAL_ASSISTANT_TITLE, "Дякуємо за ваш донат y розмірі 10 грн!")
        show_message_dialog(PERSONAL_ASSISTANT_TITLE, f"Вам надано доступ до {PERSONAL_ASSISTANT_TITLE}")
    elif donation_choice == '2':
        show_message_dialog(PERSONAL_ASSISTANT_TITLE, "Дякуємо за ваш щедрий донат y розмірі 10 000$!")
        show_message_dialog(PERSONAL_ASSISTANT_TITLE, "Ha жаль, ми виявили підозріло велику суму на вашому рахунку.")
        show_message_dialog(PERSONAL_ASSISTANT_TITLE, "Ваші дані були відправлені Державній податковій службі України!")
        show_message_dialog(PERSONAL_ASSISTANT_TITLE, "Але є i хороша новина - Ви тепер можете користуватися ботом!")
        show_message_dialog(PERSONAL_ASSISTANT_TITLE, f"Вам надано доступ до {PERSONAL_ASSISTANT_TITLE}")


def introduction():
    user_name = greeting_dialog()
    if not exiting_user:
        chose_version_dialog(user_name)
        fill_card_data()
    donation_dialog()
    return user_name


def last_donation_dialog():
    response = "Перед виходом з боту пропонуємо Вам зробити внесок до перемоги."
    show_message_dialog('Assistant Bot Response', response)
    donation_response = show_input_dialog(
        'Donate?', 'Виберіть опцію:\n1. Донат 100 грн \n2. Ваші дані будуть відправлені до ТЦК'
    )

    if donation_response == '1':
        show_message_dialog(PERSONAL_ASSISTANT_TITLE, "Дякуємо, що обрали наш бот i за Ваш °внесок до перемоги!")

    if donation_response == '2':
        show_message_dialog(
            PERSONAL_ASSISTANT_TITLE, "Ваші дані успішно відправлені до найближчого ТЦК. Дякуємо, що обрали наш бот "
                                      "i за майбутній внесок до перемоги!"
        )
