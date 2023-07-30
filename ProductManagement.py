import hashlib

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = self._encrypt_password(password)

    def _encrypt_password(self, password):
        return hashlib.sha256(password.encode()).hexdigest()

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class ProductManager:
    def __init__(self):
        self.products = []
        self.users = {}

    def register_user(self, username, password):
        if username not in self.users:
            self.users[username] = User(username, password)
            print("Registration successful! Please log in.")
        else:
            print("Username already exists. Please choose a different username.")

    def login(self, username, password):
        if username in self.users:
            user = self.users[username]
            if user.password == hashlib.sha256(password.encode()).hexdigest():
                print(f"Welcome, {username}!")
                return True
        print("Invalid username or password. Please try again.")
        return False

    def add_product(self, name, price):
        product = Product(name, price)
        self.products.append(product)
        print(f"{name} added to the product list.")

    def delete_product(self, name):
        for product in self.products:
            if product.name == name:
                self.products.remove(product)
                print(f"{name} removed from the product list.")
                break
        else:
            print(f"{name} not found in the product list.")

    def view_products(self):
        if self.products:
            print("Product List:")
            for product in self.products:
                print(f"{product.name} - ${product.price}")
        else:
            print("No products available.")

# Create an instance of ProductManager
product_manager = ProductManager()

while True:
    print("""
--- Product Management App ---
1. Register
2. Login
3. Add Product
4. Delete Product
5. View Products
6. Exit
""")
    choice = input("Enter your choice: ")

    if choice == "1":
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        product_manager.register_user(username, password)

    elif choice == "2":
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        if product_manager.login(username, password):
            # Show product management options after successful login
            while True:
                print("""
--- Product Management Options ---
1. Add Product
2. Delete Product
3. View Products
4. Logout
""")
                user_choice = input("Enter your choice: ")

                if user_choice == "1":
                    name = input("Enter product name: ")
                    price = float(input("Enter product price: "))
                    product_manager.add_product(name, price)

                elif user_choice == "2":
                    name = input("Enter product name to delete: ")
                    product_manager.delete_product(name)

                elif user_choice == "3":
                    product_manager.view_products()

                elif user_choice == "4":
                    print("Logging out...")
                    break

                else:
                    print("Invalid choice. Please try again.")

    elif choice == "3":
        print("Please log in to manage products.")

    elif choice == "4":
        print("Please log in to manage products.")

    elif choice == "5":
        print("Please log in to view products.")

    elif choice == "6":
        print("Exiting the Product Management App...")
        break

    else:
        print("Invalid choice. Please try again.")
