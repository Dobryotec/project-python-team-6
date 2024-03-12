from collections import UserDict, defaultdict
from datetime import timedelta, datetime


class AddressBook(UserDict):

    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, value):
        return self.data.get(value, "Contact not found")
     
    def delete(self, name):
        del self.data[name]

    def get_birthdays_per_week(self):
        birthdays_per_week = defaultdict(list)
        today = datetime.today()

        for record in self.values():
            if record.birthday is not None:
                birthday_this_year = datetime.strptime(record.birthday.value, '%d.%m.%Y').replace(year=today.year)

                if birthday_this_year < today:
                    birthday_this_year = birthday_this_year.replace(year=today.year + 1)

                delta_days = (birthday_this_year - today).days
                next_birthday_weekday = (today + timedelta(days=delta_days)).strftime('%A')

                if next_birthday_weekday == "Saturday":
                    delta_days += 2
                elif next_birthday_weekday == "Sunday":
                    delta_days += 1

                next_birthday_date = today + timedelta(days=delta_days)
                next_birthday_weekday = next_birthday_date.strftime('%A')

                if delta_days > 0 and delta_days < 7:
                    birthdays_per_week[next_birthday_weekday].append(record.name.value)
            else:
                continue
        return birthdays_per_week
