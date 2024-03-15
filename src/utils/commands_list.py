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
    "exit": {
        "description": "Exit the program.",
        "example": None,
    },
    "close": {
        "description": "Close the program.",
        "example": None,
    },
    "all": {
        "description": "Show all contacts.",
        "example": None,
    },
    "add-contact": {
        "description": "Add a new contact with a name and phone number.",
        "example": "add-contact 'John Doe' '0501234455'",
    },
    "find": {
        "description": "Find a contact by name or phone number.",
        "example": "find 'John' | find 1231234444",
    },
    "add-phone": {
        "description": "Add a phone number to an existing contact.",
        "example": "add-phone 'John Doe' '0501234455'",
    },
    "edit-phone": {
        "description": "Edit an existing phone number for a contact.",
        "example": "edit-phone 'John Doe' '0501234455' '0501234355'",
    },
    "delete-phone": {
        "description": "Delete a phone number from a contact.",
        "example": "delete-phone 'John Doe' '0501234455'",
    },
    "show-phone": {
        "description": "Show all phone numbers for a contact.",
        "example": "show-phone 'name'",
    },
    "add-email": {
        "description": "Add an email address to a contact.",
        "example": "add-email 'John Doe' 'john@doe.com'",
    },
    "edit-email": {
        "description": "Edit the email address of a contact.",
        "example": "edit-email 'John Doe' 'john@doe.com'",
    },
    "delete-email": {
        "description": "Delete the email address of a contact.",
        "example": "delete-email 'John Doe'",
    },
    "add-address": {
        "description": "Add a physical address to a contact.",
        "example": "add-address 'John Doe' 'address here'",
    },
    "edit-address": {
        "description": "Edit the physical address of a contact.",
        "example": "edit-address 'John Doe' 'new address here'",
    },
    "delete-address": {
        "description": "Delete the physical address of a contact.",
        "example": "delete-address 'John Doe'",
    },
    "add-birthday": {
        "description": "Add a birthday to a contact.",
        "example": "add-birthday 'John' '20.01.1990'",
    },
    "update-birthday": {
        "description": "Update the birthday of a contact.",
        "example": "update-birthday 'John' '20.01.1990'",
    },
    "show-birthday": {
        "description": "Show the birthday of a contact.",
        "example": "show-birthday 'John'",
    },
    "show-birthdays": {
        "description": "Show upcoming birthdays.",
        "example": "show-birthdays",
    },
    "find-birthdays": {
        "description": "Find birthdays within a specified number of days.",
        "example": "find-birthdays 5",
    },
    "update-contact": {
        "description": "Update contact information.",
        "example": "update-contact 'John Doe'",
    },
    "delete-contact": {
        "description": "Delete a contact.",
        "example": "delete-contact 'John'",
    },
    "add-note": {
        "description": "Add a note to a contact.",
        "example": "add-note 'John'",
    },
    "update-note": {
        "description": "Update a note for a contact.",
        "example": "edit-note 'John'",
    },
    "find-notes-by-tag": {
        "description": "Find notes by tag.",
        "example": "find-notes-by-tag 'tag'",
    },
    "find-notes": {
        "description": "Find notes by search text.",
        "example": "find-notes 'search text'",
    },
    "delete-note": {
        "description": "Delete a note for a contact.",
        "example": "delete-note 'John'",
    },
    "rename": {
        "description": "Rename a contact.",
        "example": "rename 'John' 'Jack'",
    },
}
