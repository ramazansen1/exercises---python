print("-" * 30)

print("""
        Welcome to Site,

        1- with Username Login
        2- with E-mail Login

           Quit('quit', 'q', 'Q')
""")

print("-" * 30)

register = {
    'sys_userName': 'admin',
    'sys_password': 'admin',
    'sys_email': 'admin@rambo.com'
}

def emailLogin(register):
    while True:
        email = input("Enter your email adress: ")
        password = input("Enter your password: ")

        if register['sys_email'] == email:
            if register['sys_password'] == password:
                print(f"Login succesfull, welcome {register['sys_email']}")
                break
            else:
                print("Password is incorrect, please try again.")
            break
        else:
            print("Invalid E-mail!")

def login(register):
    while True:
        userName = input("Enter your username: ")
        password = input("Enter your password: ")

        if register['sys_userName'] == userName:
            if register['sys_password'] == password:
                print(f"Login succesfull, welcome {register['sys_userName']}.")
                break
            else:
                print("Password is incorrect, please try again.")

        else:
            print("Username and password are incorrect, please try again.")
def changeUserName(register):
    while True:
        new_userName = input("Enter your new username: ")
        forbiddenChar = ["ğ", "Ğ", "ü", "Ü", "İ", "ş", "Ş", "ö", "Ö", "ç", "Ç"]
        for char in new_userName:
            if char in forbiddenChar:
                print(f"Forbidden characters cannot be used in the username.\n{forbiddenChar}")
                break
        else:
            register['sys_userName'] = new_userName
            print(f"Your username has been successfully changed.\nUsername:{register['sys_userName']}")
            break
def changeEmail(register):
    while True:
        new_email = input("Enter your new e-mail: ")
        forbiddenChar = ["ğ", "Ğ", "ü", "Ü", "İ", "ş", "Ş", "ö", "Ö", "ç", "Ç"]
        for char in new_email:
            if char in forbiddenChar:
                print(f"Forbidden characters cannot be used in the username.\n{forbiddenChar}")
                break
        else:
            register['sys_email'] = new_email
            print(f"Your email has been successfully changed.\nEmail:{register['sys_email']}")
            break
def changePassword(register):
    while True:
        new_password = input("Enter your new password: ")
        forbiddenChar = ["ğ", "Ğ", "ü", "Ü", "İ", "ş", "Ş", "ö", "Ö", "ç", "Ç"]
        if len(new_password) in range(3, 8):
            for char in new_password:
                if char in forbiddenChar:
                    print(f"Forbidden characters cannot be used in the password.\n{forbiddenChar}")
                    break
            else:
                register['sys_password'] = new_password
                print(f"Your password hass been successfully changed.\nPassword:{register['sys_password']}")
                break
        else:
            print("Your password cannot be less than 3 characters and no more 8 characters.")

while True:
    select = input("Do you want to login with username or by e-mail: ")
    if select == "q" or select == "quit" or select == "Q" or select == "Quit":
        print("Your login has been canceled!")
        break
    elif select == "1":
        login(register)
        print("""
                1- Change username
                2- Change password
                
                Log Out('quit', 'q', 'Q')
        """)
        operation = input("What would you like to do: ")
        if operation == "q":
            print("Log out")
            break
        elif operation == "1":
            changeUserName(register)
        elif operation == "2":
            changePassword(register)
        else:
            print("Invalid select!")
    elif select == "2":
        emailLogin(register)
        print("""
               1- Change password
               2- Change email

               Log Out('quit', 'q', 'Q')
               """)
        operation_1 = input("What would you like to do: ")
        if operation_1 == "q":
            print("Log out!")
            break
        elif operation_1 == "1":
            changePassword(register)
        elif operation1 == "2":
            changeEmail(register)
        else:
            print("Invalid select!")
    else:
        print("Invalid select!")
