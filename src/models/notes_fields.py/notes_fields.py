from src.models.address_book_fields.fields import Field

class Title(Field):
    def __init__(self, value):
        super().__init__(value, required=True, max_length=50)

    def validate(self):
        super().validate()

class Text(Field):
    def __init__(self, value):
        super().__init__(value, max_length=500)

    def validate(self):
        super().validate()