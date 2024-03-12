from collections import UserDict, defaultdict
from datetime import timedelta, datetime


class AddressBook(UserDict):

    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, value):
        return self.data.get(value, "Contact not found")
     
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
