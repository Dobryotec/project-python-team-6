from src.bot_commands import *


commands_l = {
    "help": {
        "description": "Show available commands and their usage examples.",
        "example": None,
    },
    "hello": {
        "description": "Greet the user.",
        "example": None,
    },
    "close": {
        "description": "Close the program.",
        "example": None,
    },
    "add-contact": {
        "description": "Add a new contact with a name and phone number.",
        "example": "add-contact 'John Doe' '0501234455'",
    },
    "show-phone": {
        "description": "Show all phone numbers for a contact.",
        "example": "show-phone 'name'",
    },
    "add-birthday": {
        "description": "Add a birthday to a contact.",
        "example": "add-birthday 'John' '20.01.1990'",
    },
    "show-birthday": {
        "description": "Show the birthday of a contact.",
        "example": "show-birthday 'John'",
    },
    "show-birthdays": {
        "description": "Show upcoming birthdays.",
        "example": "show-birthdays",
    },
    "add-address": {
        "description": "Add a physical address to a contact.",
        "example": "add-address 'John Doe' 'address here'",
    },
    "add-email": {
        "description": "Add an email address to a contact.",
        "example": "add-email 'John Doe' 'john@doe.com'",
    },
    "delete-contact": {
        "description": "Delete a contact.",
        "example": "delete-contact 'John'",
    },
    "add-note": {
        "description": "Add a note to a contact.",
        "example": "add-note 'John'",
    },
    "update-note-by-title": {
        "description": "Update a note for a contact.",
        "example": "update-note-by-title 'John'",
    },
    "delete-note": {
        "description": "Delete a note for a contact.",
        "example": "delete-note 'John'",
    },
}
