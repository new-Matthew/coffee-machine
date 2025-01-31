from resources import menu
from resources import resources as res

profit = 0
is_on = True
while is_on:
    choice = input("What do you like? (espresso/latte/capuccino): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"water: {res["water"]}ml")
        print(f"milk: {res["milk"]}ml")
        print(f"coffee: {res["coffee"]}g")
        print(f"Money: ${profit}")
    