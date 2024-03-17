from src.utils.show_message_dialog import show_message_dialog
from src.utils.show_input_dialog import show_input_dialog


class Card:
    def __init__(self, card_number=None, password=None, cvv=None):
        self.card_number = card_number
        self.password = password
        self.cvv = cvv

    def validate_card(self):
        self.card_number = self.get_valid_input(
            "Enter card number", "Будь ласка, введіть номер Вашої картки:", 16
        )
        self.password = self.get_valid_input(
            "Enter password", "Будь ласка, введіть пароль:", 4
        )
        self.cvv = self.get_valid_input("Enter CVV", "Будь ласка, введіть CVV:", 3)

    def get_valid_input(self, prompt, error_message, length):
        while True:
            user_input = show_input_dialog(prompt, error_message)
            if user_input and len(user_input) == length and user_input.isdigit():
                return user_input
            else:
                show_message_dialog(
                    "Error",
                    f"Будь ласка, введіть коректне значення. Має бути {length}-значне число.",
                )


if __name__ == "__main__":
    card = Card()
    card.validate_card()
