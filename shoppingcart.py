# Function to add an item to the cart
def add_to_cart(cart, item, price):
    cart[item] = price
    print(f"{item} added to cart.")

# Function to remove an item from the cart
def remove_from_cart(cart, item):
    if item in cart:
        del cart[item]
        print(f"{item} removed from cart.")
    else:
        print(f"{item} is not in the cart.")

# Function to calculate the total price of items in the cart
def calculate_total(cart):
    total = sum(cart.values())
    return total

# Function to display items in the cart
def display_cart(cart):
    if not cart:
        print("Cart is empty.")
    else:
        print("Items in the cart:")
        for item, price in cart.items():
            print(f"- {item}: ${price:.2f}")

# Main program
if __name__ == "__main__":
    cart = {}  # Initialize an empty dictionary for the cart

    while True:
        print("\nMENU:")
        print("1. Add item to cart")
        print("2. Remove item from cart")
        print("3. Calculate total price")
        print("4. Display cart")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            item = input("Enter item name: ")
            price = float(input("Enter item price: "))
            add_to_cart(cart, item, price)

        elif choice == "2":
            item = input("Enter item name to remove: ")
            remove_from_cart(cart, item)

        elif choice == "3":
            total = calculate_total(cart)
            print(f"Total price of items in cart: ${total:.2f}")

        elif choice == "4":
            display_cart(cart)

        elif choice == "5":
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 5.")
