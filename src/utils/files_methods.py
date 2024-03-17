import pickle


def save_to_file(filename, records, notes):
    with open(filename, "wb") as file:
        data = {"records": records, "notes": notes}
        pickle.dump(data, file)


def load_from_file(filename, book, note):
    try:
        with open(filename, "rb") as file:
            content = pickle.load(file)

        if content.get("records"):
            for _, v in content.get("records").items():
                book.add_record(v)

        note.notes = content.get("notes")

    except FileNotFoundError:
        book.data = {}
        note.notes = []


def save_name_to_file(name):
    with open("username.txt", "w+", encoding="utf-8") as file:
        file.write(name)


def load_name_from_file():
    try:
        with open("username.txt", "r", encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError:
        return None
