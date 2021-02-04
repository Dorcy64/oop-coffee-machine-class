from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

storage = CoffeeMaker()
menu_item = Menu()
money = MoneyMachine()

menu_items = menu_item.get_items()
while 1 > 0:
    question = input(f"What would you like? ({menu_items}) : ").lower()

    if question == "report":
        storage.report()
        money.report()
    elif question == "off":
        break
    elif question in menu_items:
        if storage.is_resource_sufficient(menu_item.find_drink(question)):
            product = menu_item.find_drink(question)
            product_cost = product.cost
            if money.make_payment(product_cost):
                storage.make_coffee(menu_item.find_drink(question))

    else:
        print("Invalid entry please choose from the 3 choices")