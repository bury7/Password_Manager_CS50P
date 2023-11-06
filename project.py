from string import punctuation, whitespace, ascii_letters
from pysqlcipher3 import dbapi2 as sqlcipher
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.text import Text
from string import digits
from rich import print
import pyperclip
import getpass
import bcrypt
import sys
import os


"""Exceptions"""
class Err_AttemptOver(Exception):
    pass

class Err_NoSavedPass(Exception):
    pass

class Err_AccAlreadyExist(Exception):
    pass

class Err_AppAlreadyExist(Exception):
    pass

class Err_AppNotExist(Exception):
    pass

class Err_User_Not_Exist(Exception):
    pass



"""Constants"""
salt = b'$2b$12$2r0TJwpYwom0vO0I2sTWOe'
comands = [".quit", ".all", ".exit"]
printable = ascii_letters + digits + punctuation
asciidigit = ascii_letters + digits

SYMBOLS_LIST = tuple([s for s in punctuation])

ATTEMPTS = 3

"""Text Constants"""
WELCOME = Panel("Welcome to the Password Manager by Bury! \nChoose one of these options: \n1) Log In \n2) Create New Account",
                title="Password Manager by Bury", expand=True)

PROMPT = "> "

ERR_ATTEMPTSOVER = Panel(Text("ERROR: ATTEMPTS OVER", style="bold red", justify="center"), border_style="red", highlight=True, expand=True, title="ERROR")

ERR_NOTCORRECT = Text("Input not correct!!", style="bold red")

ERR_PSSWDNOTMATCH = Panel(Text("ERROR: PASSWORD DON'T MATCH", style="bold red", justify="center"), border_style="red", highlight=True, expand=True, title="ERROR")

ERR_ACCALREADYEXIST = Panel(Text("ERROR: THIS ACCOUNT ALREADY EXIST", style="bold red", justify="center"), border_style="red", highlight=True, expand=True, title="ERROR")

ERR_USERNOTEXIST = Panel(Text("ERROR: THIS ACCOUNT NOT EXIST", style="bold red", justify="center"), border_style="red", highlight=True, expand=True, title="ERROR")

ERR_FATAl = Panel(Text("ERROR: FATAL ERROR", style="bold red", justify="center"), border_style="red", highlight=True, expand=True, title="ERROR")

ERR_PASSWORDINCORRECT = Panel(Text("ERROR: PASSWORD INCORRECT", style="bold red", justify="center"), border_style="red", highlight=True, expand=True, title="ERROR")

ERR_APPALREADYEXIST = Panel(Text("ERROR: APPLICATION NAME ALREADY EXIST IN DATA BASE", style="bold red", justify="center"), border_style="red", highlight=True, expand=True, title="ERROR")

ERR_APPNOTEXIST = Panel(Text("ERROR: APPLICATION NAME NOT EXIST IN DATA BASE", style="bold red", justify="center"), border_style="red", highlight=True, expand=True, title="ERROR")

ERR_NOSAVEDPASS= Panel(Text("ERROR: THERE ARE NO SAVED PASSWORDS", style="bold red", justify="center"), border_style="red", highlight=True, expand=True, title="ERROR")


EXPLAINNAME = Text('\nUsername must be 2 to 30 characters long and contain only English letters, numbers and special character "_"', style="italic grey3")

EXPLAINPSSWD = Text('\nPassword must be 12 to 100 characters long and contain only English letters, numbers and special character "!#$%&()*+,-./:;<=>?@[\]^_`{|}~"', style="italic grey3")

CREATEACCNAME = Panel(Text('To create an account, you need to enter a username and password. \nFirst, enter your username:') + EXPLAINNAME,
                title="Password Manager by Bury", expand=True)

CREATEACCPASS = Panel(Text('To create an account, you need to enter a username and password. \nNow, enter your password:') + EXPLAINPSSWD,
                title="Password Manager by Bury", expand=True)

CREATEACCPASSCONFRIM = Panel(Text('To create an account, you need to enter a username and password. \nNow, confrim your password:') + EXPLAINPSSWD,
                title="Password Manager by Bury", expand=True)


SUCC_CREATEACC = Panel(Text("SUCCESS: ACCOUNT CREATED SUCCESSFULLY", style="bold green", justify="center"), border_style="green", highlight=True, expand=True, title="SUCCESS")

SUCC_CREATEPASS = Panel(Text("SUCCESS: PASSWORD ADDED SUCCESSFULLY", style="bold green", justify="center"), border_style="green", highlight=True, expand=True, title="SUCCESS")

SUCC_UPDATE = Panel(Text("SUCCESS:INFORMATION UPDATED SUCCESSFULLY", style="bold green", justify="center"), border_style="green", highlight=True, expand=True, title="SUCCESS")

SUCC_DELETE = Panel(Text("SUCCESS:INFORMATION DELETED SUCCESSFULLY", style="bold green", justify="center"), border_style="green", highlight=True, expand=True, title="SUCCESS")

SUCC_COPY = Panel(Text("SUCCESS:PASSWORD COPIED SUCCESSFULLY", style="bold green", justify="center"), border_style="green", highlight=True, expand=True, title="SUCCESS")


LOGINNAME = Panel(Text('To log in an account, you need to enter a username and password. \nFirst, enter your username:'),
                title="Password Manager by Bury", expand=True)

LOGINPASS = Panel(Text('To log in an account, you need to enter a username and password. \nNow, enter your password:'),
                title="Password Manager by Bury", expand=True)


MENU = Panel(Text('Menu: \n1) Show passwords \n2) Add password \n3) Update password \n4) Delete password \n5) Copy password'),
                title="Password Manager by Bury", expand=True)


ADDAPPNAME = Panel(Text('Enter the name of the program for which you want to add a password'),
                title="Password Manager by Bury", expand=True)

ADDUSERNAME = Panel(Text('Enter the username for the application to add a password to'),
                title="Password Manager by Bury", expand=True)

ADDEMAIL = Panel(Text('Enter the email address for the application to add a password to') + Text('\n(Optional)', style="italic grey3"),
                title="Password Manager by Bury", expand=True)

ADDURL = Panel(Text('Enter the URL for the application to add a password to') + Text('\n(Optional)', style="italic grey3"),
                title="Password Manager by Bury", expand=True)

ADDPASSWORD = Panel(Text('Enter the password for the application to add a password to'),
                title="Password Manager by Bury", expand=True)


UPDATEAPPNAME = Panel(Text('Enter the name of the program for which you want to update info'),
                title="Password Manager by Bury", expand=True)

UPDATEUSERNAME = Panel(Text('Enter the new username for the application') + Text('\n(You can leave it blank if you are not going to change anything)', style="italic grey3"),
                title="Password Manager by Bury", expand=True)

UPDATEEMAIL = Panel(Text('Enter the new email address for the application') + Text('\n(You can leave it blank if you are not going to change anything)', style="italic grey3"),
                title="Password Manager by Bury", expand=True)

UPDATEURL = Panel(Text('Enter the new URL for the application') + Text('\n(You can leave it blank if you are not going to change anything)', style="italic grey3"),
                title="Password Manager by Bury", expand=True)

UPDATEPASSWORD = Panel(Text('Enter the new password for the application') + Text('\n(You can leave it blank if you are not going to change anything)', style="italic grey3"),
                title="Password Manager by Bury", expand=True)


DELETEAPPNAME = Panel(Text('Enter the name of the application whose information you want to delete or enter .all to delete all informations'),
                title="Password Manager by Bury", expand=True)


COPYAPPNAME = Panel(Text('Enter the name of the program from which you want to copy the password'),
                title="Password Manager by Bury", expand=True)


SHOW = Panel(Text('Enter the name of the program for which you want to see a password or enter .all to see all paswords'),
                title="Password Manager by Bury", expand=True)


BYE = Panel(Text("GOODBYE", style="bold purple", justify="center"), border_style="purple", highlight=True, expand=True)



"""The main function is responsible for handling exceptions that cause the program to exit completely."""
def main() -> None:
    clean_scrin()
    try:
        welcome()

    except (KeyboardInterrupt, EOFError):
        exit(BYE, 0)

    except Err_AttemptOver:
        exit(ERR_ATTEMPTSOVER, 1)

    except Err_AccAlreadyExist:
        exit(ERR_ACCALREADYEXIST, 1)

    except Err_User_Not_Exist:
        exit(ERR_USERNOTEXIST, 1)

    except Exception:
          exit(ERR_FATAl, 2)



"""The welcome function is responsible for displaying the welcome screen for the user."""
def welcome() -> None:
    print(WELCOME)
    choice = check_input(condition=["1", "2"], length_max=1)
    clean_scrin()

    if choice == "1":
        log_in()

    if choice == "2":
        create_acc()


"""The log_in function is responsible for displaying the login screen for the user and processing the login
and password for logging into the password manager.

Raises
    User_Not_Exist: Raise when user data base don't exist
"""
def log_in() -> None:
    global username
    global password

    print(LOGINNAME)
    username = check_input(condition=asciidigit+"_", length_min=2, length_max=30, explain=EXPLAINNAME)

    if not os.path.exists(username + ".db"):
        raise Err_User_Not_Exist

    clean_scrin()
    print(LOGINPASS)
    password = bcrypt.hashpw(check_input(condition=printable, length_min=12, explain=EXPLAINPSSWD, psswd=True).encode('utf-8'), salt)

    password = password.decode("utf-8")
    username = username + ".db"

    clean_scrin()
    try:
        log_in_db(username, password)
    except sqlcipher.DatabaseError:
         print(ERR_PASSWORDINCORRECT)
         sys.exit(1)
    else:
        while True:
            menu()


"""The create_acc function is responsible for displaying the account creation screen for the user
and processing the login and password for creating an account in the password manager."""
def create_acc() -> None:
    global username
    global password

    print(CREATEACCNAME)
    username = check_input(condition=asciidigit+"_", length_min=2, length_max=30, explain=EXPLAINNAME)
    clean_scrin()

    while True:
        print(CREATEACCPASS)
        password = bcrypt.hashpw(check_input(condition=printable, length_min=12, explain=EXPLAINPSSWD, psswd=True).encode('utf-8'), salt)
    
        clean_scrin()
        print(CREATEACCPASSCONFRIM)
        if bcrypt.checkpw(check_input(condition=printable, length_min=12, explain=EXPLAINPSSWD, psswd=True).encode('utf-8'), password):
            break

        else:
            clean_scrin()
            print(ERR_PSSWDNOTMATCH)
            continue

    password = password.decode("utf-8")
    username = username + ".db"

    if creaete_acc_db(username, password):
        clean_scrin()
        print(SUCC_CREATEACC)
        main()


"""The menu function is responsible for displaying the menu screen to the user
and handling exceptions that return the user to the menu."""
def menu() -> None:
    print(MENU)
    choice = check_input(condition="12345", length_max=1)

    try:
        if choice == "1":
            show_scrin()

        elif choice == "2":
            add_scrin()

        elif choice == "3":
            update_scrin()

        elif choice == "4":
            delete_scrin()

        elif choice == "5":
            copy_scrin()

    except Err_AppNotExist:
        clean_scrin()
        print(ERR_APPNOTEXIST)

    except Err_AppAlreadyExist:
        clean_scrin()
        print(ERR_APPALREADYEXIST)

    except Err_NoSavedPass:
        clean_scrin()
        print(ERR_NOSAVEDPASS)


"""The show_scrin function is responsible for displaying the password show screen to the user
and handles the show function to output information to the user."""
def show_scrin() -> None:
    global username
    global password

    clean_scrin()
    print(SHOW)

    while True:
        app_name = check_input(condition=printable, length_max=500).lower()
        if results := show(username, password, app_name):
            clean_scrin()
            console = Console()
            table = create_table(results)
            console.print(table)
            break


"""The show function queries the database to display the requested passwords.

    Args:
        filename: Name of databse
        passphrase: Password to database
        app_name: Name of application from which  want to receive information
    Returns:
        List of tuples with infromation from database
    Raises:
        Err_NoSavedPass: Raise when no information to return
"""
def show(filename: str, passphrase: str, app_name: str) -> list:
    conn = sqlcipher.connect(filename)
    c = conn.cursor()
    c.execute(f"PRAGMA key = '{passphrase}';")
    c.execute("PRAGMA cipher_compatibility = 3")

    if app_name == ".all":
        c.execute("SELECT * FROM users_data")
    else:
        c.execute("SELECT * FROM users_data WHERE app_name=?", (app_name,))

    results = c.fetchall()

    if results is None or len(results) == 0:
        raise Err_NoSavedPass

    conn.commit()
    c.close()
    conn.close()

    return results


"""The create_table function is responsible for creating the table for printing.

    Args:
        s: List of data to be converted into a table
    Returns:
        The table for printing
"""
def create_table(s: list) -> Table:
    table = Table(expand=True)
    table.add_column("Application Name")
    table.add_column("Username")
    table.add_column("Email")
    table.add_column("URL")
    table.add_column("Password")
    for i in s:
        table.add_row(*list(i))
    return table


"""The add_scrin function is responsible for displaying the add screen to the user
and controls the add function to add information to the database.

Raises:
    Err_AppAlreadyExist: Raise when application already exist in database
"""
def add_scrin() -> None:
    global username
    global password

    clean_scrin()
    print(ADDAPPNAME)

    while True:
        app_name = check_input(condition=printable, length_max=500).lower()
        if check_exist(username, password, app_name):
            raise Err_AppAlreadyExist
        username_, email, url, password_ = get_info()
        if add(username, password, app_name, username_, email, url, password_):
            clean_scrin()
            print(SUCC_CREATEPASS)
            break


"""The add function queries the database to add information to database.

    Args:
        filename: Name of databse
        passphrase: Password to database
        app_name: Name of application
        username: Username in the application
        email: email in the application
        url: url to the application
        password: password  in the application
    Returns:
        True
"""
def add(filename: str, passphrase: str, app_name: str, username: str, email: str, url: str, password: str) -> bool:
    conn = sqlcipher.connect(filename)
    c = conn.cursor()
    c.execute(f"PRAGMA key = '{passphrase}';")
    c.execute("PRAGMA cipher_compatibility = 3")

    c.execute("INSERT INTO users_data (app_name, username, email, url, password) VALUES (?, ?, ?, ?, ?)", (app_name, username, email, url, password))

    conn.commit()
    c.close()
    conn.close()
    return True


"""The update_scrin function is responsible for displaying the update screen to the user
and controls the update function to update information in the database.

Raises:
    Err_AppNotExist: Raise when application don't exist in database
"""
def update_scrin() -> None:
    global username
    global password

    clean_scrin()
    print(UPDATEAPPNAME)

    while True:
        app_name = check_input(condition=printable, length_max=500).lower()
        if not check_exist(username, password, app_name):
            raise Err_AppNotExist
        username_, email, url, password_ = get_info_update()
        if update(username, password, app_name, username_, email, url, password_):
            clean_scrin()
            print(SUCC_UPDATE)
            break


"""The update function queries the database to update information in database.

    Args:
        filename: Name of databse
        passphrase: Password to database
        app_name: Name of application
        username: Username in the application
        email: email in the application
        url: url to the application
        password: password  in the application
    Returns:
        True
"""
def update(filename: str, passphrase: str, app_name: str, username: str, email: str, url: str, password: str) -> bool:
    conn = sqlcipher.connect(filename)
    c = conn.cursor()
    c.execute(f"PRAGMA key = '{passphrase}';")
    c.execute("PRAGMA cipher_compatibility = 3")

    if username != "":
        c.execute("UPDATE users_data SET username=? WHERE app_name=?", (username, app_name))
    if email != "":
        c.execute("UPDATE users_data SET email=? WHERE app_name=?", (email, app_name))
    if url != "":
        c.execute("UPDATE users_data SET url=? WHERE app_name=?", (url, app_name))
    if password != "":
        c.execute("UPDATE users_data SET password=? WHERE app_name=?", (password, app_name))

    conn.commit()
    c.close()
    conn.close()
    return True


"""The delete_scrin function is responsible for displaying the delete screen to the user
and controls the delete function to delete information from the database."""
def delete_scrin() -> None:
    global username
    global password

    clean_scrin()
    print(DELETEAPPNAME)

    while True:
        app_name = check_input(condition=printable, length_max=500).lower()
        if delete(username, password, app_name):
            clean_scrin()
            print(SUCC_DELETE)
            break


"""The delete function queries the database to delete information from database.

    Args:
        filename: Name of databse
        passphrase: Password to database
        app_name: Name of application
    Returns:
        True
    Raises:
        Err_AppNotExist: Raise when no information to delete
"""
def delete(filename: str, passphrase: str, app_name: str) -> bool:
    conn = sqlcipher.connect(filename)
    c = conn.cursor()
    c.execute(f"PRAGMA key = '{passphrase}';")
    c.execute("PRAGMA cipher_compatibility = 3")

    if app_name == ".all":
        c.execute("DELETE FROM users_data")
    else:
        if check_exist(filename, passphrase, app_name):
            c.execute("DELETE FROM users_data WHERE app_name=?", (app_name,))
        else:
            raise Err_AppNotExist

    conn.commit()
    c.close()
    conn.close()
    return True


"""The check_exist function queries the database to find out if such application is in the database.

    Args:
        filename: Name of databse
        passphrase: Password to database
        app_name: Name of application
    Returns:
        True or False
"""
def check_exist(filename: str, passphrase: str, app_name: str) -> bool:
    conn = sqlcipher.connect(filename)
    c = conn.cursor()
    c.execute(f"PRAGMA key = '{passphrase}';")
    c.execute("PRAGMA cipher_compatibility = 3")

    c.execute("SELECT * FROM users_data WHERE app_name=?", (app_name,))

    result = c.fetchone()
    if result is None:
        return False

    conn.commit()
    c.close()
    conn.close()
    return True


"""The copy_scrin function is responsible for displaying the copy screen to the user
and controls the copy function to copy password from the database.

Raises:
    Err_AppNotExist: Raise when application don't exist in database
"""
def copy_scrin() -> None:
    global username
    global password

    clean_scrin()
    print(COPYAPPNAME)

    while True:
        app_name = check_input(condition=printable, length_max=500).lower()
        if not check_exist(username, password, app_name):
            raise Err_AppNotExist
        pyperclip.copy(take_pass(username, password, app_name))
        clean_scrin
        print(SUCC_COPY)
        break


"""The take function queries the database to get password information for a specific application.

    Args:
        filename: Name of databse
        passphrase: Password to database
        app_name: Name of application
    Returns:
        application password
"""
def take_pass(filename: str, passphrase: str, app_name: str) -> str:
    conn = sqlcipher.connect(filename)
    c = conn.cursor()
    c.execute(f"PRAGMA key = '{passphrase}';")
    c.execute("PRAGMA cipher_compatibility = 3")

    c.execute("SELECT password FROM users_data WHERE app_name=?", (app_name,))

    result = c.fetchone()

    conn.commit()
    c.close()
    conn.close()
    return result[0]


"""The get_info function prompts the user for application information.

    Returns:
        application username, email, URL, password in the application
"""
def get_info() -> str:
    clean_scrin()
    print(ADDUSERNAME)
    username_ = check_input(condition=printable, length_max=500)

    clean_scrin()
    print(ADDEMAIL)
    email = check_input( condition=printable+whitespace, length_min=0, length_max=500)

    clean_scrin()
    print(ADDURL)
    url = check_input(condition=printable+whitespace, length_min=0, length_max=500)

    clean_scrin()
    print(ADDPASSWORD)
    password_ = check_input(condition=printable, length_max=500, psswd=True)

    clean_scrin()

    return username_, email, url, password_


"""The get_info_update function prompts the user for application information.
   The same as get_info, but removes the restriction and gives the opportunity not to
   enter anything in the username and password fields.

    Returns:
        application username, email, URL, password in the application
"""
def get_info_update() -> str:
    clean_scrin()
    print(UPDATEUSERNAME)
    username_ = check_input(condition=printable, length_min=0, length_max=500)

    clean_scrin()
    print(UPDATEEMAIL)
    email = check_input(condition=printable+whitespace, length_min=0, length_max=500)

    clean_scrin()
    print(UPDATEURL)
    url = check_input(condition=printable+whitespace, length_min=0, length_max=500)

    clean_scrin()
    print(UPDATEPASSWORD)
    password_ = check_input(condition=printable, length_min=0, length_max=500, psswd=True)

    clean_scrin()

    return username_, email, url, password_


"""The create_acc_db function creates a new database for the user.

    Args:
        filename: Name of databse
        passphrase: Password to database
    Returns:
        True
    Raises:
        Err_AccAlreadyExist: Raise when database with this name already exist
"""
def creaete_acc_db(filename: str, passphrase: str) -> bool:
    if os.path.exists(filename):
        raise Err_AccAlreadyExist
    else:
        conn = sqlcipher.connect(filename)
        c = conn.cursor()
        c.execute(f"PRAGMA key = '{passphrase}';")
        c.execute("PRAGMA cipher_compatibility = 3")

        c.execute("""CREATE TABLE users_data(
                  app_name TEXT NOT NULL PRIMARY KEY,
                  username TEXT NOT NULL,
                  email TEXT,
                  url TEXT,
                  password INT NOT NULL);""")

        conn.commit()
        c.close()
        conn.close()
        return True


"""The log_in_db function checks if a database with that name exists.

    Args:
        filename: Name of databse
        passphrase: Password to database
    Returns:
        True
    Raises:
        sqlcipher.DatabaseError: Raise when can't find database
"""
def log_in_db(filename: str, passphrase: str) -> bool:
    conn = sqlcipher.connect(filename)
    c = conn.cursor()
    c.execute(f"PRAGMA key = '{passphrase}';")
    c.execute("PRAGMA cipher_c2ompatibility = 3")

    c.execute("SELECT app_name FROM users_data;")

    conn.commit()
    c.close()
    conn.close()
    return True


"""The check_input function validates user input.

    Args:
        condition: a condition that an input must satisfy to pass validation
        length_min: min length of input
        lenght_max: max length of input
        explain: the explanation that is output on failure
        psswd: To use getpass or not
    Returns:
        Users input
    Raises:
        Err_AttemptOver : Raise when the attempts run out
"""
def check_input(condition: list = [], length_min: int = 1, length_max: int = 100, explain: str = "", psswd: bool = False) -> str:
    for _ in range(ATTEMPTS):

        if psswd:
            print(PROMPT, end="")
            inpt = getpass.getpass("").strip()
        else:
            inpt = input(PROMPT).strip()

        if check_input_help(inpt, condition=condition, length_min=length_min, length_max=length_max):
            print(ERR_NOTCORRECT, explain)
            continue
        else:
            return inpt
        
    raise Err_AttemptOver


"""The check_input function help to validates user input.

    Args:
        inpt: users iput
        condition: a condition that an input must satisfy to pass validation
        length_min: min length of input
        lenght_max: max length of input
    Returns:
        True or False
"""
def check_input_help(inpt: str, condition: list = [], length_min: int = 1, length_max: int = 100,) -> bool:
    if inpt == ".quit" or inpt == ".exit":
        raise EOFError

    if len(inpt) < length_min:
        return True

    if len(inpt) > length_max:
        return True

    if inpt.endswith(SYMBOLS_LIST):
        return True

    for i in inpt:
        if i not in condition:
            return True

    if inpt.startswith(".") and inpt not in comands:
        return True

    return False


"""Cleaning the screen"""
def clean_scrin() -> None:
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


"""
The exit function  exit program with message and exit code.

    Args:
        message: the message with which the program exits
        exit_code: the exit code with which the program exits
"""
def exit(message: str, exit_code: int) -> None:
    clean_scrin()
    print(message)
    sys.exit(exit_code)
    
    

"""Calls main"""
if __name__ == "__main__":
    main()
