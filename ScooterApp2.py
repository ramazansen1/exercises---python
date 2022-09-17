import time
print(("-" * 30) + "\nWelcome to Electric Scooter App!\nRide Price 0.19/min.\n" + ("-") * 30)

print("\n1-Start to Ride\n2-Finish to Ride\n3-Profile\n4-My Wallet\n5-Add Balance\n6-Contact us\n7-Quit to App\n")


first_name = "John"
surname = "xxx"
born = "18/09/1945"
e_mail = "johnxxx@gmail.com"
driving_password = "1111"

sys_user_name = "John123"
sys_password = "Abc123Abc"
sys_driving_password = "1111"
sys_security_code = "SC123"

change = 3
driving_change = 3
company_phone = "05*********"
company_mail = "scooterapp@gmail.com"
wallet_balance = 15

while True:
        user_name = input("Please Enter Your Username\t: ")
        password = input("Please Enter Your Password\t: ")
        if sys_user_name != user_name and sys_password == password:
            print("Your account is logged in!")
            time.sleep(1)
            print("Your Username is Wrong!Try again!")
            change -= 1
        elif sys_user_name == user_name and sys_password != password:
            print("Your account is logged in!")
            time.sleep(1)
            print("Your Password is Wrong!Try again!")
            change -= 1
        elif sys_user_name != user_name and sys_password != password:
            print("Your account is logged in!")
            time.sleep(1)
            print("Your Username and Password is Wrong!Try again!")
            change -= 1
            if change == 0:
                print("Your account has been suspended!")
                regeneration = input("Do you want to renew username and password?\nPress 'y/Y' to reflesh, 'n/N' to exit!\n")
                if regeneration == "y" or regeneration == "Y":
                    security_code = input("Enter the security code\t: ")
                    if sys_security_code == security_code:
                        new_user_name = input("Please Enter Your New Username\t: ")
                        new_password =  input("Please Enter Your New Password\t: ")

                        sys_user_name = new_user_name
                        sys_password = new_password
                        print("Your username and password have been successfully changed!")

                    else:
                        print("Your account has been suspended!\nPleae contact with us!")
                        break
                elif regeneration == "n" or regeneration == "N":
                    print("The page is closing!")
                    time.sleep(1)
                    print("See you!")
                    break
        else:
            print("Welcome to Scooter App!")

            while True:
                selection = input("Please Enter the Selection\t: ")
                if not 1 <= (selection.isdigit()) <= 7:
                    print("You made the wrong selection!\nPlease try again!")
                if selection == "1":
                    print("Your driving is beginning!\nPlease wait!")
                    time.sleep(1)
                    driving_password = input("Please Enter the Driving Password: ")
                    if sys_driving_password != driving_password:
                        print("Your Driving Password is wrong!\nPlease try again!")
                        driving_change -= 1
                    elif sys_driving_password == driving_password:
                        print("Have a nice ride.. :)\nDon't forget to the traffic rules!\nPlease don't forget to press 2 to end the ride!")
                elif selection == "2":
                    print("Your ride is ending.\nPlease wait!")
                    time.sleep(1)
                    d_time_h = int(input("Please enter the driving time [Hours]\t: "))
                    d_time_m = int(input("Please enter the driving time [Minutes]\t: "))
                    tMinutes = d_time_h * 60
                    tMinutes += d_time_m
                    time.sleep(1)
                    print(f"The duration of your ride {d_time_h}:{d_time_m} = {tMinutes} finished in minutes!")
                    tPrice = (0.19 * tMinutes)
                    if tPrice > wallet_balance:
                        print("Opps!Sorry,insufficient balance!\nPlease Load Balance!")
                    elif tPrice <= wallet_balance:
                        time.sleep(1)
                        print(f"{tPrice} Dolars has been withdrawn from ScooterApp wallet!\nThank you for choosing us!")
                        wallet_balance -= tPrice
                elif selection == "3":
                    # profile = "\nName = John\nSurname = Xxx\nBorn = 15/09/1985\nE-mail = johnxxx@gmail.com"
                    print(f"Your profile info;\nName = {first_name}\nSurname = {surname}\nBorn = {born}\nE-mail = {e_mail}\n")
                elif selection == "4":
                    print(f"Your wallet balance {wallet_balance} dolars.")
                elif selection == "5":
                    deposit = float(input("Enter the money to be deposit\t: "))
                    wallet_balance += deposit
                    print(f"Money has been deposit in your wallet.Your current wallet amount {wallet_balance} dolars.")
                elif selection == "6":
                    print(f"Our phone numbers = {company_phone}\nOur mail adress = {company_mail}.")
                elif selection == "7":
                    print("Application is closing!")
                    time.sleep(1)
                    print("See you!")
                    break

            # selection = input("Please Enter the Selection!\t: ")
            #
            # if not 1 <=int(selection) <= 7:
            #     print("You made the wrong selection!\nPlease try again!")
            # if selection == "1":
            #     print("Your driving is beginning!\nPlease wait!")
            #     time.sleep(1)
            #     driving_password = input("Please Enter the Driving Password: ")
            #     if sys_driving_password != driving_password:
            #         print("Your Driving Password is wrong!\nPlease try again!")
            #         driving_change -= 1
            #     elif sys_driving_password == driving_password:
            #         print(
            #             "Have a nice ride.. :)\nDon't forget to the traffic rules!\nPlease don't forget to press 3 to end the ride!")
            # elif selection == "2":
            #     print("Your ride is ending.\nPlease wait!")
            #     time.sleep(1)
            #     d_time_h = int(input("Please enter the driving time [Hours]\t: "))
            #     d_time_m = int(input("Please enter the driving time [Minutes]\t: "))
            #     tMinutes = d_time_h * 60
            #     tMinutes += d_time_m
            #     time.sleep(1)
            #     print(f"The duration of your ride {d_time_h}:{d_time_m} = {tMinutes} finished in minutes!")
            #     tPrice = (0.19 * tMinutes)
            #     if tPrice > wallet_balance:
            #         print("Opps!Sorry,insufficient balance!\nPlease Load Balance!")
            #     elif tPrice <= wallet_balance:
            #         time.sleep(1)
            #         print(f"{tPrice} Dolars has been withdrawn from ScooterApp wallet!\nThank you for choosing us!")
            #         wallet_balance -= tPrice
            # elif selection == "3":
            #     profile = "\nName = John\nSurname = McAfee\nBorn = 18/09/1945\nE-mail = johnmcafee@gmail.com"
            #     print(f"Your profile info;\n{profile}")
            # elif selection == "4":
            #     print(f"Your wallet balance {wallet_balance} dolars.")
            # elif selection == "5":
            #     deposit = float(input("Enter the money to be deposit\t: "))
            #     wallet_balance += deposit
            #     print(f"Money has been deposit in your wallet.Your current wallet amount {wallet_balance} dolars.")
            # elif selection == "6":
            #     print(f"Our phone numbers = {company_phone}\nOur mail adress = {company_mail}.")
            # elif selection == "7":
            #     print("Application is closing!")
            #     break

