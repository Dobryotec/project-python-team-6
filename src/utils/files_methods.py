import pickle


def save_to_file(filename, records, notes):
    with open(filename, "wb") as file:
        data = {"records": records, "notes": notes}
        pickle.dump(data, file)


def load_from_file(filename, book, note):
    try:
        with open(filename, "rb") as file:
            content = pickle.load(file)

        if content.get('records'):
            for k, v in content.get('records').items():
                book.add_record(v)

        note.notes = content.get("notes")

    except FileNotFoundError:
        book.data = {}
        note.notes = []
