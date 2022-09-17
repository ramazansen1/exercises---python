import random

def generate_name():
    first_names = ["Cristiano","Lionel","Michael","Max","Charles","Lewis"]
    last_names = ["Ronaldo","Messi","Schumacher","Verstappen","Leclerc","Hamilton"]
    return "{} {}".format(random.choice(first_names),random.choice(last_names))

for i in range(5):
    print(generate_name())

