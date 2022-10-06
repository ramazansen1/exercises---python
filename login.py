print("-"*30)

print("""
        Welcome to Site,
        
        1- Login
        2- Forgot username
        3- Forgot password
        
           Quit('quit', 'q', 'Q')
""")

print("-"*30)

register = {
    'sys_userName': 'admin',
    'sys_password': 'admin',
}

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
    selection = input("Enter your selection: ")
    if selection == "Quit" or selection == "quit" or selection == "Q" or selection == "q":
        print("Logged out")
        break
    elif not "1" <= selection <= "3":
        print("Wrong selection, try again!")
    elif selection == "1":
        login(register)
    elif selection == "2":
        changeUserName(register)
    else:
        changePassword(register)