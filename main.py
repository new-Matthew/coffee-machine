from resources import menu
from resources import resources as res

profit = 0

def is_resource_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] >= res[item]:
            print("Desculpe não há água suficiente!, escolha outro drink ou digite off para sair!")
            return False
    return True

def process_coins():
    print("Por favor insira as moedas!")
    total = int(input("Quantas moedas de 1 centavos deseja inserir?"))
    total += int(input("Quantas moedas de 0.50 centavos deseja inserir?") * 0.5)
    total += int(input("Quantas moedas de 0.25 centavos deseja inserir?") * 0.25)
    total += int(input("Quantas moedas de 0.10 centavos deseja inserir?") * 0.10)
    total += int(input("Quantas moedas de 0.05 centavos deseja inserir?") * 0.05)
    return total

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
    else:
        drink = menu[choice]
        is_resource_sufficient(drink["ingredients"])
        payment = process_coins()
        print(payment)