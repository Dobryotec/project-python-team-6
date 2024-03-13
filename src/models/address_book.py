import pickle
from collections import UserDict, defaultdict
from datetime import datetime
from src.models.notes import *


class AddressBook(UserDict):
    def __init__(self):
        super().__init__()
        self.notes = []

    def add_note(self, title, text=None, tags=None):
        note = Note(title, text)
        if tags:
            note.add_tags(tags)
        self.notes.append(note)

    def delete_note_by_title(self, title):
        for note in self.notes:
            if note.title.value == title:
                self.notes.remove(note)
                return f"Note '{title}' deleted."
        return f"Note '{title}' not found."

    def find_note_by_title(self, title):
        for note in self.notes:
            if note.title.value == title:
                return str(note)
        return f"Note '{title}' not found."

    def find_note_by_tag(self, tag):
        notes = []
        for note in self.notes:
            if tag in note.tags:
                text = note.text.value
                notes.append(text if text else note.title.value)
        return '\n'.join(notes)
    
    def save_to_file(self, filename):
        with open(filename, "wb") as file:
            data = {"records": self.data, "notes": self.notes}
            pickle.dump(data, file)

    def load_from_file(self, filename):
        try:
            with open(filename, "rb") as file:
                content = pickle.load(file)

            if content.get('records'):
                for k, v in content.get('records').items():
                    self.add_record(v)

            self.notes = content.get("notes")

        except FileNotFoundError:
            self.data = {}
            self.notes = []

    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, value):
        for name, record in self.data.items():
            if value == name or value == record.email.value:
                return record
            else:
                return "Contact not found"

    def delete(self, name):
        del self.data[name]

    def get_birthdays_within_days(self, days):

        birthdays_within_days = defaultdict(list)
        today = datetime.today()

        for record in self.values():
            if record.birthday is not None:
                birthday_this_year = datetime.strptime(record.birthday.value, '%d.%m.%Y').replace(year=today.year)

                if birthday_this_year < today:
                    birthday_this_year = birthday_this_year.replace(year=today.year + 1)

                delta_days = (birthday_this_year - today).days

                if 0 <= delta_days <= days:
                    birthdays_within_days[birthday_this_year].append(record.name.value)

        return birthdays_within_days
