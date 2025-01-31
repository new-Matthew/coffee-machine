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
    total = float(input("Quantas moedas de 1 real deseja inserir? "))
    total += float(input("Quantas moedas de 0.50 centavos deseja inserir? ")) * 0.5
    total += float(input("Quantas moedas de 0.25 centavos deseja inserir? ")) * 0.25
    total += float(input("Quantas moedas de 0.10 centavos deseja inserir? ")) * 0.10
    total += float(input("Quantas moedas de 0.05 centavos deseja inserir? ")) * 0.05
    return total

def is_transaction_successful(money_received, drink_cost):
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"aqui está seu troco: R${change}. ")
        global profit
        profit += drink_cost
        return True
    else:
        print("Desculpe você não tem dinheiro suficiente. Dinheiro reembolsado!")
        return False

is_on = True
while is_on:
    choice = input("O que você prefere? (espresso/matte/capuccino): ")
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
        is_transaction_successful(payment, drink["cost"] )