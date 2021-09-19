# TODO Import Coffee data
# Import menu data from the data file

from Data import MENU, resources

# Declare a dictionary variable that will contain the resources remaining after each drink order

machine_resources = {}

machine_resources["water"] = resources["water"]
machine_resources["milk"] = resources["milk"]
machine_resources["coffee"] = resources["coffee"]
machine_resources["money"] = 0


# Function for extracting the resource values
def resource_availability(water, milk, coffee):
    """Determines if there are enough resources to make the drink. Returns true if there
    are and False if they are not"""
    if water < machine_resources["water"] and milk < machine_resources["milk"] and coffee < machine_resources["coffee"]:
        return True
    else:
        return False

# Function for calculating what resources are left after the drink is made
def resource_balance():
    """Subtracts the resources used by the drink from the total and returns the values left"""
    return machine_resources["water"] - drink_water, machine_resources["milk"] - drink_milk, \
           machine_resources["coffee"] - drink_coffee


# Function to calculate the total amount paid from the number of each type of coin entered
def total_currency(quarter, dime, nickle, penny):
    return (quarter * 0.25) + (dime * 0.1) + (nickle * 0.05) + (penny * 0.01)

# Function to determine how much chang is required
def change_given(amount_paid, price):
    return amount_paid - price


# TODO Print What would you like? (espresso/latte/cappuccino)

while True:
    coffee_choice = input("What would you like? (espresso/latte/cappuccino)").lower()

    # TODO To report on the resources (water, milk, coffee, money) available
    # Display report if report is entered in as the choice

    if coffee_choice == "report":
        print(f"Water: {machine_resources['water']}ml")
        print(f"Milk: {machine_resources['milk']}ml")
        print(f"Water: {machine_resources['coffee']}g")
        print(f"Money: ${machine_resources['money']}")

    else:
    # Resource details for the chosen drink are examined

        drink_water = MENU[coffee_choice]["ingredients"]["water"]


        if "milk" in MENU[coffee_choice]["ingredients"]:
            drink_milk = MENU[coffee_choice]["ingredients"]["milk"]

        else:
            drink_milk = 0

        drink_coffee = MENU[coffee_choice]["ingredients"]["coffee"]

    # TODO Ensure there are enough resources to make the drink
    # Determine if the drink choice can be made

        if resource_availability(drink_water, drink_milk, drink_coffee):
            # TODO Ask the customer to insert coins (quarters, dimes, nickles and pennies)
            print("Please insert coins")
            quarters = int(input("How many Quarters?"))
            dimes = int(input("How many Dimes?"))
            nickles = int(input("How many Nickles?"))
            pennies = int(input("How many Pennies?"))

            total_payment = total_currency(quarters, dimes, nickles, pennies)

            print(f"Total Payment is ${total_payment}")

    # TODO Ensure the customer has inserted enough money and provide change if required
            if total_payment >= MENU[coffee_choice]["cost"]:
                print(f"Here is your {coffee_choice}. Enjoy!")
                change = change_given(total_payment, MENU[coffee_choice]["cost"])
                print(f"Here is ${change:.2f} in change")
                machine_resources["money"] += MENU[coffee_choice]["cost"]


    # TODO Whatever is ordered the ingredients are subtracted from the available resources
    # Update the balance of the resources
                machine_resources["water"], machine_resources["milk"], machine_resources["coffee"] = resource_balance()
                print(f"Water balance is {machine_resources['water']}")
                print(f"Milk balance is {machine_resources['milk']}")
                print(f"Water balance is {machine_resources['coffee']}")

            else:
                print("Sorry that's not enough money. Money refunded")
        else:
                print("Sorry there is not enough water.")










