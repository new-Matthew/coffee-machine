from resources import menu
from resources import resources as res


is_on = True
while is_on:
    choice = input("What do you like? (espresso/latte/capuccino): ")
    if choice == "off":
        is_on = False
    