
from src.bot_commands import *

commands_l = {
    "help": {
        "function": "help",
        "example": None,
    },
    "hello": {
        "function": None,
        "example": None,
    },
    "exit": {
        "function": None,
        "example": None,
    },
    "close": {
        "function": None,
        "example": None,
    },
    "all": {
        "function": "show_all",
        "example": None,
    },
    "add-contact": {
        "function": "add_contact",
        "example": "add-contact 'John Doe' '0501234455'",
    },
    "find": {
        "function": "find_contact",
        "example": "find 'John' | find 1231234444",
    },
    "add-phone": {
        "function": "add_phone",
        "example": "add-phone 'John Doe' '0501234455'",
    },
    "edit-phone": {
        "function": "edit_phone",
        "example": "edit-phone 'John Doe' '0501234455' '0501234355'",
    },
    "delete-phone": {
        "function": "delete_phone",
        "example": "delete-phone 'John Doe' '0501234455'",
    },
    "show-phone": {
        "function": "show_phones",
        "example": "show-phone 'name'",
    },
    "add-email": {
        "function": "add_email",
        "example": "add-email 'John Doe' 'john@doe.com'",
    },
    "edit-email": {
        "function": "edit_email",
        "example": "edit-email 'John Doe' 'john@doe.com'",
    },
    "delete-email": {
        "function": "delete_email",
        "example": "delete-email 'John Doe'",
    },
    "add-address": {
        "function": "add_address",
        "example": "add-address 'John Doe' 'address here'",
    },
    "edit-address": {
        "function": "add_address",
        "example": "edit-address 'John Doe' 'new address here'",
    },
    "delete-address": {
        "function": "delete_address",
        "example": "delete-address 'John Doe'",
    },
    "add-birthday": {
        "function": "add_birthday",
        "example": "add-birthday 'John' '20.01.1990'",
    },
    "update-birthday": {
        "function": "add_birthday",
        "example": "update-birthday 'John' '20.01.1990'",
    },
    "show-birthday": {
        "function": "show_birthday",
        "example": "show-birthday 'John'",
    },
    "show-birthdays": {
        "function": "show_birthdays",
        "example": "show-birthdays",
    },
    "find-birthdays": {
        "function": "find_birthdays",
        "example": "find-birthdays 5",
    },
    "update-contact": {
        "function": "update_contact",
        "example": "update-contact 'John Doe'",
    },
    "delete-contact": {
        "function": "delete_contact",
        "example": "delete-contact 'John'",
    },
    "add-note": {
        "function": "add_note",
        "example": "add-note 'John'",
    },
    "update-note": {
        "function": "edit_note",
        "example": "edit-note 'John'",
    },
    "find-notes-by-tag": {
        "function": "find_note_by_tag",
        "example": "find-notes-by-tag 'tag'",
    },
    "find-notes": {
        "function": "find_notes",
        "example": "find-notes 'search text'",
    },
    "delete-note": {
        "function": "delete_note",
        "example": "delete-note 'John'",
    },
    "rename": {
        "function": "rename",
        "example": "rename 'John' 'Jack'",
    },
}



