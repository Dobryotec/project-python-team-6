from src.models.notes_fields.notes_fields import Title, Text


class Note:
    def __init__(self, title, text=None):
        self.title = Title(title)
        self.text = Text(text)

    def __str__(self):
        if self.text:
            return f"Title: {self.title.value}\nText: {self.text.value}"
        else:
            return f"Title: {self.title.value}"
