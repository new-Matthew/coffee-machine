from resources import menu
from resources import resources as res




profit = 0

def is_resource_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] >= res[item]:
            print("Desculpe não há água suficiente!, escolha outro drink ou digite off para sair!")
            return False
    return True

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
    


    
    # TODO Se existir recursos suficientes, p fazer o drink selecionado, então o programa deve fazer o user inserir moeda moedas: 1real, 50cent, 25 cent 10cent 5cent 1cent