from prompt_toolkit.shortcuts import input_dialog

from src.utils.styles import styles


def show_input_dialog(title, text):
    return input_dialog(
        title=title,
        text=text,
        style=styles
    ).run()
