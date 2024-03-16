# Personal Assistant Diia

## Description

Personal Assistant Bot is a command-line tool designed to assist you in organizing your contacts and notes efficiently. With this application, you can easily manage your contact information, including phone numbers, birthdays, email addresses, and physical addresses. You have the flexibility to add, edit, and delete contacts as needed. Additionally, you can create notes and categorize them by titles and tags for better organization. The tool allows you to edit or delete notes, and you can even search for them based on titles and tags. One of the key features of this application is its ability to store all your data locally on your machine, ensuring that your information remains secure and accessible whenever you need it.

## Installation

1. git clone https://github.com/Dobryotec/project-python-team-6.git

2. pip install .

3. The bot is started by the command `bot_run`. 


### 🗂️ General Commands
| Command        | Description                          | 
| -------------- | ------------------------------------ |
| `help`         | Show available commands              |  
| `hello`        | Greet the user                       |  
| `exit`, `close`         | Close the program                     |    
                   

### 👤 Contact Management
| Command          | Description                                | Example                                      |
| ---------------- | ------------------------------------------ | -------------------------------------------- |
| `all-contacts`    | Show all contacts      | `all-contacts`        |
| `add-contact`           | Add a new contact with a name and phone number.     | `add-contact John 0501234455`          |
| `find-contact` | Find a contact by name or email.               | `find-contact John`                  |
| `delete-contact` | Delete a contact                           | `delete-contact John`                      |


### 📞 Phone Management
| Command          | Description                                | Example                                      |
| ---------------- | ------------------------------------------ | -------------------------------------------- |
| `change-phone`      | Change the phone number for a contact   | `change-phone John 0501234455 0671111111`          |
| `show-phone`     | Show all phone numbers for a contact        | `show-phone John` |                          

### 📬 Address Management
| Command          | Description                                | Example                                      |
| ---------------- | ------------------------------------------ | -------------------------------------------- |
| `add-address`    | Add a physical address to a contact        | `add-address John 'address here'`                       |
| `show-address`   | Show the address of a contact              | `show-address John`                        |

### 📧 Email Management
| Command          | Description                                | Example                                      |
| ---------------- | ------------------------------------------ | -------------------------------------------- |
| `add-email`      | Add an email address to a contact          | `add-email John 'email here'`        |
| `change-email`     | Change the email address of a contact        | `change-email John 'new email'`                       
| `show-email`     | Show the email address of a contact        | `show-email John`                          |

### 🎂 Birthday Management
| Command          | Description                                | Example                                      |
| ---------------- | ------------------------------------------ | -------------------------------------------- |
| `add-birthday`   | Add a birthday to a contact                | `add-birthday John 20.01.1990`        
| `show-birthday`  | Show the birthday of a contact             | `show-birthday John`                       |
| `birthdays` | Show upcoming birthdays                     | `birthdays`                          

### 📝 Notes commands
| Command        | Description                            | Example                                      |
| -------------- | -------------------------------------- | -------------------------------------------- |                                          
| `add-note`     | Add a note               | `add-note`                            |
| `update-note-by-title`    | Update a note   | `update-note-by-title`                           |
| `delete-note`  | Delete a note from your notes          | `delete-note`                         |
| `find-note-by-tag`    | Find note by tag         | `find-note-by-tag `                        |
| `find-note`     | Find a note by title                | `find-note`
| `show-notes`     | Show all notes      | `show-notes`

## Technologies Used

Personal Assistant Diia is built using the following technologies:

- [Python](https://www.python.org/): The programming language used for the backend logic.
- [tabulate](https://pypi.org/project/tabulate/): Python library for rendering tables in the command-line interface.
- [prompt_toolkit](https://python-prompt-toolkit.readthedocs.io/en/latest/): Python library for building powerful interactive command-line applications.

These technologies were chosen for their robustness, ease of use, and suitability for building command-line applications.



