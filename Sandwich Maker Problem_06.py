# Dictionary containing all food information
sandwich = {
    "Bread": {
        "Wholemeal": 1.00,
        "White": 0.80,
        "Cheesy White": 1.20,
        "Gluten Free": 1.40,
    },
    "Meat": {
        "Chicken": 2.69,
        "Beef": 3.00,
        "Salami": 4.00,
        "Vegan Slice": 3.30
    },
    "Garnish": {
        "Onion": 1.69,
        "Tomato": 1.00,
        "Lettuce": 2.00,
        "Cheese": 2.50
    }
}


# allows program to be run again on command
def main():
    def sandwich_selection(category):
        # counter for while loop
        counter = 0
        # Prints each category separately
        print(f"\navailable {category} options: ")

        # loops through option and its correspondant price for each category separately
        for choice, price in sandwich[category].items():
            print(f"{choice}: ${price}")

        # loops until all three components have been successfully picked
        while counter < 3:
            choice = input(f"Select your {category}: ").strip()
            if choice in sandwich[category]:
                counter += 1
                return choice
            # if choice not in the category loops again
            else:
                print("Invalid choice. Please try again.")

    # function to add cost of options together
    def price_adder(bread_choice, meat_choice, garnish_choice):
        total_price = sandwich["Bread"][bread_choice] + sandwich["Meat"][meat_choice] + sandwich["Garnish"][
            garnish_choice]
        return total_price

    # gets user to confirm order
    def confirm_order():
        confirmation = input(
            "Would you like to change your order (Yes or No)?: ").capitalize()
        if confirmation == "Yes":
            print("Okay new selection")
            main()
            print("Thank you for ordering")
        elif confirmation == "No":
            print("Thank you for ordering")
        else:
            print("please enter yes or no")
            confirm_order()

    # User choices for each category
    bread_choice = sandwich_selection("Bread")
    meat_choice = sandwich_selection("Meat")
    garnish_choice = sandwich_selection("Garnish")

    # total price of burger
    total_burger_price = price_adder(bread_choice, meat_choice, garnish_choice)

    # Shows the user their options and how much it costs
    print(f"The price for your sandwich ({bread_choice} Bread, {meat_choice}, {garnish_choice}) is: ")
    print(f"${total_burger_price}")
    confirm_order()


main()
