from setuptools import setup, find_namespace_packages


setup(
    name="personal_assistant_diia",
    version="1.0.0",
    description="""Personal Assistant Bot is a command-line tool designed to assist you in organizing your contacts 
                     and notes efficiently. With this application, you can easily manage your contact information, 
                     including phone numbers, birthdays, email addresses, and physical addresses. You have the flexibility 
                     to add, edit, and delete contacts as needed. Additionally, you can create notes and categorize them by 
                     titles and tags for better organization. The tool allows you to edit or delete notes, and you can even 
                     sort them based on the date they were added or by their tags. One of the key features of this application
                     is its ability to store all your data locally on your machine, ensuring that your information 
                     remains secure and accessible whenever you need it""",
    url="https://github.com/Dobryotec/project-python-team-6",
    author="python-team-6",
    author_email="",
    license="MIT",
    packages=find_namespace_packages(),
    install_requires=["tabulate", "prompt_toolkit"],
    entry_points={"console_scripts": ["bot_run = src.main:main"]},
)
