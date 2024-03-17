from collections import UserDict, defaultdict
from datetime import datetime


class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, value):
        for name, record in self.data.items():
            if value == name or value == record.email.value:
                return record
            else:
                return "Контакт не знайдено."

    def delete(self, name):
        del self.data[name]

    def get_birthdays_within_days(self, days):
        birthdays_within_days = defaultdict(list)
        today = datetime.today()

        for record in self.values():
            if record.birthday is not None:
                birthday_this_year = datetime.strptime(
                    record.birthday.value, "%d.%m.%Y"
                ).replace(year=today.year)

                if birthday_this_year < today:
                    birthday_this_year = birthday_this_year.replace(year=today.year + 1)

                delta_days = (birthday_this_year - today).days

                if 0 <= delta_days <= days:
                    birthdays_within_days[birthday_this_year].append(record.name.value)

        return birthdays_within_days
