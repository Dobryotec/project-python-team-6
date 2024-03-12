from src.models.address_book_fields.fields import *

class Note:
    def __init__(self, title, text=None):
        self.title = Field(title, required=True, max_length=50)
        if text:
            self.text = Field(text, max_length=500)
        else:
            self.text = None