import pickle
from collections import UserDict, defaultdict
from datetime import datetime
from src.models.notes import *

class AddressBook(UserDict):
    def __init__(self):
        super().__init__()
        self.notes = []

    def add_note(self, title, text=None):
        note = Note(title, text)
        self.notes.append(note)

    def delete_note_by_title(self, title):
        for note in self.notes:
            if note.title == title:
                self.notes.remove(note)
                return f"Note '{title}' deleted."
        return f"Note '{title}' not found."

    def find_note_by_title(self, title):
        for note in self.notes:
            if note.title == title:
                return note
        return f"Note '{title}' not found."
    
    def save_to_file(self, filename):
        with open(filename, "wb") as file:
            pickle.dump(self.data, file)

    def load_from_file(self, filename):
        try:
            with open(filename, "rb") as file:
                content = pickle.load(file)
            for k, record in content.items():
                self.add_record(record)

        except FileNotFoundError:
            self.data = {}

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
