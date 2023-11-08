# Password Manager

Video overview: <https://youtu.be/0ySJU_u5Eso>

This repository is my final project for the CS50P course. In which I implement a password mannager that works in the command line interface. This password manager supports multiple users, has the ability to create a new account or log in to an existing account, after logging in you get the opportunity to add new passwords for storage, update passwords, delete them, there is also the ability to view all passwords, and the ability to copy the password to the clipboard


## Overview of the Course
The CS50 Python course introduced me to the world of Python programming, covering everything from Python syntax and data structures to advanced concepts like object-oriented programming and web development. Throughout the course, I learned to write and debug Python code, manipulate data structures, and build web applications.The final project was a culmination of my newfound skills, demonstrating my ability to apply Python creatively to solve real-world problems. This course equipped me with a strong foundation in Python and a deep appreciation for its versatility and applicability in various domains.


## Contents of the Repository
The following files are included in this repository:

- [project.py](project.py): The password management application is contained within this file.

- [test_project.py](test_project.py): This file contains tests for functions using pytest

- [requirements.txt](requirements.txt): This file has all the requirements to run the program


## Libraries used in the project
- [Rich](https://rich.readthedocs.io/en/stable/): to make a beautiful output of data from my program;
- [Pysqlcipher3](https://github.com/rigglemania/pysqlcipher3): to encrypt the database with passwords;
- [Pyperclip](https://github.com/asweigart/pyperclip): to implement the copy to clipboard function;
- [Bcrypt](https://pypi.org/project/bcrypt/): to hash password value for more secure.
  

## Project Description

After launching the project, you will be greeted by a welcome menu that offers you the option to create a new account or log in to an already-created account.

### Creating an Account

Let's start with creating an account. After selecting this item, the program will ask the user to enter a username and password. After that, the username is converted to the name of the new database, and the password is hashed by using the "bcrypt" library for greater security. With this data, the program creates a new database for the user and encrypts the contents of the database with a password using the "pysqlcipher" library, making it impossible to know what is written in that database without knowing the password.

### Logging In

If you select the login option, you will be asked for your username and password to open the previously created database and start using the program. If everything goes successfully, the user is transferred to the main menu.

### Main Menu Functions

There are five functions in the main menu:

1. **Show Information**: After selecting it, the user will be asked for the name of the program for which they want to get information, or the user can show all available information. If the information that the user wants to see is not there, the program will issue an error.

2. **Adding Information**: With this function, the user can add new information to the database. The function will ask for all the necessary information and create a new row in the database. If you provide the name of a program that is already in the database, the user receives an error.

3. **Update Information**: The user can update the information previously provided for a certain program. It asks for the name of the program and changes all the necessary fields for them. If such a program does not exist in the database, the user will see an error.

4. **Deletion**: The user can select the program information they want to delete from the database or delete all information from it. If the user enters an application name that is not in the database, they will see an error.

5. **Password Copy**: It copies the password to the program entered by the user. If the information does not exist in the database, the user receives an error.

### Quitting the Program

Quitting the program is implemented by the command `.quit` or `.exit`. You can also use `ctrl+c` or `ctrl+d` in the program.

### Tests
In the [test_project.py](test_project.py) file, a tests of all program functions that are not used for displaying information on the screen is implemented.

## Course URL

To learn about CS50 Python course, go to the official course website on the edX platform: [CS50's Introduction to Programming with Python](https://www.edx.org/learn/python/harvard-university-cs50-s-introduction-to-programming-with-python).


## License

This repository is provided for educational and reference purposes under the MIT License.
