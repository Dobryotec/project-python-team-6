from prompt_toolkit.shortcuts import message_dialog
from src.utils.styles import styles


def show_message_dialog(title, text):
    return message_dialog(title=title, text=text, style=styles).run()
