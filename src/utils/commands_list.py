from src.bot_commands import *


commands_l = {
    "add-contact": {
        "description": "Add a new contact with a name and phone number.",
        "example": "add-contact 'John' '0501234455'",
    },
    "change-phone": {
        "description": "Change the phone number for a contact.",
        "example": "change-phone 'John' '0501234455'",
    },
    "all_contacts": {
        "description": "Show all contacts.",
        "example": "all-contacts",
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
    "birthdays": {
        "description": "Show upcoming birthdays.",
        "example": "birthdays",
    },
    "add-address": {
        "description": "Add a physical address to a contact.",
        "example": "add-address 'John' 'address here'",
    },
    "show-address": {
        "description": "Show the address of a contact.",
        "example": "show-address 'John'",
    },
    "add-email": {
        "description": "Add an email address to a contact.",
        "example": "add-email 'John' 'john@doe.com'",
    },
    "show-email": {
        "description": "Show the email of a contact.",
        "example": "show-email 'John'",
    },
    "change-email": {
        "description": "Change the email address of a contact.",
        "example": "change-email 'John' 'new email'",
    },
    "find-contact": {
        "description": "Find a contact by name or email.",
        "example": "find-contact 'John'",
    },
    "delete-contact": {
        "description": "Delete a contact.",
        "example": "delete-contact 'John'",
    },
    "add-note": {
        "description": "Add a note to a contact.",
        "example": "add-note",
    },
    "find-note": {
        "description": "Find a note by title.",
        "example": "find-note 'note'",
    },
    "find-note-by-tag": {
        "description": "Find a note by tag.",
        "example": "find-note-by-tag 'John' 'tag'",
    },
    "update-note-by-title": {
        "description": "Update a note for a contact.",
        "example": "update-note-by-title 'title'",
    },
    "delete-note": {
        "description": "Delete a note for a contact.",
        "example": "delete-note 'note'",
    },
}
