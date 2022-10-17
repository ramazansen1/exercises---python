print("-" * 30)

print("""
        Welcome to Site,

        1- with Username Login
        2- with E-mail Login
        3- quit
""")

print("-" * 30)

# Text Info =
# [
#     sys_username,admin
#     sys_password,admin
#     sys_email,admin@mail.com
# ]

# Comment lines are used to get ideas during the solution phase.
# list = []

registerInfo = dict()
def read_from_file():
    with open("info.txt") as file:
        for line in file:
            line_elems = line.replace("\n", "").split(",")
            # print(line_elems[0])
            registerInfo[(line_elems[0])] = line_elems[1]
            # registerInfo = {
            #     line_elems[0]: line_elems[1]
            # }
            # print(mydict)
            # list.append(line_elems)

# registerInfo = dict(list)
# print(registerInfo)

def emailLogin():
    while True:
        email = input("Enter your email adress: ")
        password = input("Enter your password: ")
        #check email or password
        if registerInfo["sys_email"] == email:
            if registerInfo["sys_password"] == password:
                print(f"Login succesfull, welcome {email}")
                break
            else:
                print("Password is incorrect, please try again.")
        else:
            print("Invalid E-mail!")
read_from_file()

def usernameLogin():
    while True:
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        # check username or password
        if registerInfo["sys_username"] == username:
            if registerInfo["sys_password"] == password:
                print(f"Login succesfull, welcome {username}.")
                break
            else:
                print("Password is incorrect, please try again.")

        else:
            print("Username and password are incorrect, please try again.")
read_from_file()

while True:
    select = input("Do you want to login with username or by e-mail: ").lower()
    if select in ["q", "quit"]:
        print("Login cancelled, see you!")
        break
    elif select == "1":
        print("You selected login with username")
        usernameLogin()
        break
    elif select == "2":
        print("You selected login with email")
        emailLogin()
        break
    else:
        print("Invalid select!")
