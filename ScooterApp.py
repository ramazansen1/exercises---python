import time
print(("-" * 30) + "\nWelcome to Electric Scooter App!\nRide Price 0.19/min.\n" + ("-") * 30)

print("\n1-Login\n2-Start to Ride\n3-Finish to Ride\n4-Profile\n5-My Wallet\n6-Add Balance\n7-Contact us\n8-Quit to App\n")

first_name = "John"
surname = "McAfee"
born = "18/09/1945"
e_mail = "johnmcafee@gmail.com"
driving_password = "1111"

sys_user_name = "John123"
sys_email = "abcjohnabc@gmail.com"
sys_password = "Abc123Abc"
sys_driving_password = "1111"
change = 3
driving_change = 3
company_phone = "05*********"
company_mail = "scooterapp@gmail.com"
wallet_balance = 15

while True:
    selection = input("Please Enter the Selection!\t: ")
    while True:
        if not 1<=int(selection)<=8:
            print("You made the wrong selection!\nPlease try again!")
            break
        elif selection == "1":
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
            else:
                print("Welcome to Scooter App!")
                break
        elif selection == "2":
            print("Your driving is beginning!\nPlease wait!")
            time.sleep(1)
            driving_password = input("Please Enter the Driving Password: ")
            if sys_driving_password != driving_password:
                print("Your Driving Password is wrong!\nPlease try again!")
                driving_change -= 1
            elif sys_driving_password == driving_password:
                print("Have a nice ride.. :)\nDon't forget to the traffic rules!\nPlease don't forget to press 3 to end the ride!")
                break
        elif selection == "3":
            print("Your ride is ending.\nPlease wait!")
            time.sleep(1)
            d_time_h = int(input("Please enter the driving time [Hours]\t: "))
            d_time_m = int(input("Please enter the driving time [Minutes]\t: "))
            tMinutes =d_time_h * 60
            tMinutes += d_time_m
            time.sleep(1)
            print(f"The duration of your ride {d_time_h}:{d_time_m} = {tMinutes} finished in minutes!")
            tPrice = (0.19 * tMinutes)
            if tPrice > wallet_balance:
                print("Opps!Sorry,insufficient balance!\nPlease Load Balance!")
            elif tPrice <= wallet_balance:
                time.sleep(1)
                print(f"{tPrice} Dolars has been withdrawn from ScooterApp wallet!\nThank you for choosing us!")
                wallet_balance -=tPrice
                break
        elif selection == "4":
            profile = "\nName = John\nSurname = McAfee\nBorn = 18/09/1945\nE-mail = johnmcafee@gmail.com"
            print(f"Your profile info;\n{profile}")
            break
        elif selection == "5":
            print(f"Your wallet balance {wallet_balance} dolars.")
            break
        elif selection == "6":
            deposit = float(input("Enter the money to be deposit\t: "))
            wallet_balance += deposit
            print(f"Money has been deposit in your wallet.Your current wallet amount {wallet_balance} dolars.")
            break
        elif selection == "7":
            print(f"Our phone numbers = {company_phone}\nOur mail adress = {company_mail}.")
            break
        elif selection == "8":
            print("Application is closing!")
            break









