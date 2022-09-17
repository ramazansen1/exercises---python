print("-"*30)
print("1- Celsius to fahrenheit")
print("2- Fahrenheit to celsius")
print("-"*30)

choice = input ("Your choice (1/2): ")

if choice == "1" :
    print("\n# Celsius to Fahrenheit")
    celsius = float(input("Degree to convert: "))
    fahrenheit = (celsius * 1.8) + 32
    print(f"{celsius} degree celsius is equal to {fahrenheit} degree Fahrenheit.")
elif choice == "2":
    print("\n# Fahrenheit to Celsius")
    fahrenheit = float(input("Degree to convert: "))
    celsius = (fahrenheit - 32) / 1.8
    print(f"{fahrenheit} degree fahrenheit is equal to {celsius} degree celsius.")
else:
    print("Sorry!, You took a wrong action. ")
