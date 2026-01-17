MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

# coin values
penny = 0.01
nickel = 0.05
dime = 0.1
quarter = 0.25
money=5

# TODO:2 Turn off the Coffee Machine by entering “off” to the prompt


# TODO 5 Process coins



    # TODO 6 Check transaction successful?
def transaction(cof_type):
    global money
    charge = MENU[cof_type]["cost"]
    total_money=total_money1

    if total_money >= charge:
        change = round(total_money - charge,2)
        money=money-change+charge
        return change

    else:
        print("Sorry There's not enough money. Money refunded")
        return False



rewater = resources["water"]
refill_coffee = resources["coffee"]
# TODO:1 Gather Inputs from user

Coffee_Machine = True
while Coffee_Machine:
    cof_type = input('"What would you like? (espresso/latte/cappuccino):”')


    if cof_type == 'off':
        exit()
    if cof_type == "report":
        print(resources)
        break

    wat = MENU[cof_type]["ingredients"]["water"]
    cof = int(MENU[cof_type]["ingredients"]["coffee"])
    # Money Things
    dimes = int(input('How many dimes?:'))
    quarters = int(input('How many quarter?:'))
    nickels = int(input('How many nickel?:'))
    pennies = int(input('How many penny?:'))

    total_money1: float = dimes * dime + quarters * quarter + nickels * nickel + pennies * penny

    change=transaction(cof_type)
    # TODO:3 Print Report
    if cof_type == "repo":
        print(resources)



    # TODO:4 check resources sufficient
    elif cof_type == "espresso" or cof_type == "latte" or cof_type == "cappuccino":
        if resources["water"] >= wat and resources["coffee"] >= cof:
            # TODO:7 Make Coffee
            resources["water"] = rewater - wat
            resources["coffee"] = refill_coffee - cof

            print(f'Here is {change} of change')
            print(f'Here is your {cof_type} ☕ Enjoy!')

        else:
            print("Resources are not sufficient")
            print(f"Here's your {total_money1} refunded")
            break


    else:
        print("Invalid input")





