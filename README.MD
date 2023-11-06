    
    # Password Manager by Bury
    #### Video Demo:  <URL HERE>
    #### Description:
        In my project, I made a password manager that works in the command line interface. I have a large number of accounts 
    and it is very difficult to remember the passwords for each of them, also because I used simple passwords on some of these accounts, they were hacked. So I decided to write my own password manager that would store all passwords in a secure form on my local machine.

        Python was used as the main programming language, and I used an encrypted sqlite3 database to store data.

        I used the following libraries in my project:
    Rich: to make a beautiful output of data from my program;
    Pysqlcipher3: to encrypt the database with passwords;
    Pyperclip: to implement the copy to clipboard function;
    bcrypt: to hash password value for more secure.

        Now more details about the project and how it is implemented:
        After launching the project, you will be greeted by a welcome menu that offers you to create a new account or log in to 
    an already created account.
        Let's start with creating an account, after selecting this item, the program will ask the user to enter a username and 
    password. After that, the username is converted to the name of the new database, and the password is hashed for greater 
    security. With this data, the program creates a new database for the user and returns them to the welcome screen.
        Now, if you select the user login option, you will be asked again for your username and password in order to open the 
    previously created database and start using the program. If everything went successfully, the user is transferred to 
    the main menu.
        There are five functions in the main menu, now more about each:
        The first function is information show. After selecting it, the user will be asked for the name of the program for
    which he wants to get information, or the user can show all available information.If the information that the user 
    wants to see is not there, the program will issue an error.
        The second function is adding, with the help of which the user can add new information to the database. The function 
    will ask for all the necessary information and create a new row in the database. If you provide the name of a program 
    hat is already in the database, the user receives an error.
        The third update function, the user can update the information previously provided to a certain program, the function 
    asks for the name of the program and changes all the necessary fields for them. Thus, if such a program does not exist 
    in the database, the user will see an error.
        The fourth function is the deletion function, the user can select the program information about which he wants to 
    delete from the database, or delete all information from it. If the user enters an application name that is not in the 
    database, they will see an error.
        The fifth function implements the password copy function, it copies the password to the program entered by the user, if
    the information does not exist in the database, the user receives an error.
        Quitting the program is implemented by the command .quit or .exit, you can also use ctrl+c or ctrl+d, the program
    processes these requests and says goodbye to the user.

        During installation, problems may occur, to solve them, you need to perform additional actions that require pyperclip 
    and pysqlcipher3 modules.

    pyperclip:
    https://pypi.org/project/pyperclip/

    On Windows, no additional modules are needed.

    On Mac, this module makes use of the pbcopy and pbpaste commands, which should come with the os.

    On Linux, this module makes use of the xclip or xsel commands, which should come with the os. Otherwise run “sudo apt-get install xclip” or “sudo apt-get install xsel” (Note: xsel does not always seem to work.)
    Otherwise on Linux, you will need the gtk or PyQt4 modules installed.
    
    pysqlcipher3:
    https://github.com/rigglemania/pysqlcipher3

    32 Bit Windows Setup Instructions (using Visual Studio)
    Install Visual Studio 2015: if you do not have a paid license, the Community Edition will work fine. Make sure to select all the C++ options during the installation process.
    Install OpenSSL: you can either download the source and build locally or install a prebuilt OpenSSL binary from https://slproweb.com/products/Win32OpenSSL.html (use the latest version)
    Confirm that the OPENSSL_CONF environment variable is set properly: this should not be root OpenSSL path (ex: C:\openssl-Win32), but instead should be the path to the config file (ex: C:\openssl-Win32\bin\openssl.cfg)
    Copy the OpenSSL folder (C:\openssl-Win32\include\openssl) to the VC include directory (ex: C:\Program Files (x86)\Microsoft Visual Studio 14.0\VC\include): confirm the following path exists (\VC\include\openssl\aes.h)
    Install the latest version of Python 3 (32-bit): if you have Python 64-bit installed, you may have to uninstall it before installing Python 32-bit.
    Use the SQL Cipher 3 amalgamation: if needed, directions for building SQL Cipher can be found on the following tutorial: http://www.jerryrw.com/howtocompile.ph
    Follow the general instructions for building the amalgamation

    64 Bit Windows Setup Instructions (using Visual Studio)
    Follow the same instructions as above except for the following:
    Make sure that you are using OpenSSL-Win64
    Set the PATH to the Win64 environment
    Copy the OpenSSL folder
    Build the amalgamation and install with the latest Python x64

    
    On Linux
    sudo apt-get install libsqlcipher-dev

    Thanks for your attention, I hope you like my app.
