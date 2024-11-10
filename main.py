import store
import products

# Setup initial stock of inventory
product_list = [
    products.Product("MacBook Air M2", price=1450, quantity=100),
    products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
    products.Product("Google Pixel 7", price=500, quantity=250)
]

# Initialize the store with the product list
best_buy = store.Store(product_list)

def show_products(store):
    products = store.get_all_products()
    print("-------------------------")
    for product in products:
        product.show()
    print("---------------------")

def make_order(store):
    products = store.get_all_products()
    ordered_list = []

    while True:
        show_products(store)
        print("When you want to finish order, enter empty text.")
        product_nos = input("Which product # do you want?")
        quantity = input("What amount do you want?")
        print("When you want to finish order, enter empty text.")
        if product_nos == "" and quantity == "":
           break
        ordered_list.append((products[int(product_nos)],int(quantity)))


def start(store):
    """Main function to start the user interface."""
    while True:
        print("\nWelcome to Best Buy!")
        print("1. List all products in store")
        print("2. Show total amount in store")
        print("3. Make an order")
        print("4. Quit")

        try:
            choice = int(input("Enter your choice: "))
            if choice == 1:
                show_products(store)
            elif choice == 2:
                print(f"Total of {store.get_total_quantity()} in a store")
            elif choice == 3:
                make_order(store)
            elif choice == 4:
                print("Thank you for visiting the store. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    start(best_buy)
