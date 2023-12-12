from user_management import UserManager
from product_management import ProductManager
from order_management import OrderManager

def main():
    user_manager = UserManager()
    product_manager = ProductManager()
    order_manager = OrderManager()

    # Авторизация пользователя
    user_manager.login("username", "password")

    # Добавление продукта
    product_manager.add_product("Laptop", 1000, "Powerful laptop with high-end specifications")

    # Создание заказа
    order_manager.create_order(user_manager.get_logged_in_user())
    order_manager.add_product_to_order("Laptop", 2)

    # Вывод корзины пользователя
    order_manager.display_cart()

    # Оформление заказа
    order_manager.checkout()

if name == "__main__":
    main()
from database import Database

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

class UserManager:
    def __init__(self):
        self.database = Database()
        self.logged_in_user = None

    def register(self, username, password):
        # Регистрация нового пользователя
        user = User(username, password)
        self.database.save_user(user)

    def login(self, username, password):
        # Авторизация пользователя
        user = self.database.get_user(username)
        if user and user.password == password:
            self.logged_in_user = user
            print(f"User {username} logged in successfully.")
        else:
            print("Invalid credentials.")

    def get_logged_in_user(self):
        return self.logged_in_user
from database import Database

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

class UserManager:
    def __init__(self):
        self.database = Database()
        self.logged_in_user = None

    def register(self, username, password):
        # Регистрация нового пользователя
        user = User(username, password)
        self.database.save_user(user)

    def login(self, username, password):
        # Авторизация пользователя
        user = self.database.get_user(username)
        if user and user.password == password:
            self.logged_in_user = user
            print(f"User {username} logged in successfully.")
        else:
            print("Invalid credentials.")

    def get_logged_in_user(self):
        return self.logged_in_user
from database import Database

class Product:
    def __init__(self, name, price, description):
        self.name = name
        self.price = price
        self.description = description

class ProductManager:
    def __init__(self):
        self.database = Database()

    def add_product(self, name, price, description):
        # Добавление нового продукта
        product = Product(name, price, description)
        self.database.save_product(product)
from database import Database

class Order:
    def __init__(self, user):
        self.user = user
        self.products = []

    def add_product(self, product, quantity):
        # Добавление продукта в заказ
        self.products.append({"product": product, "quantity": quantity})

    def display_cart(self):
        # Вывод содержимого корзины
        print("Shopping Cart:")
        for item in self.products:
            print(f"{item['product'].name} - Quantity: {item['quantity']}")

    def checkout(self):
        # Оформление заказа
        total_price = sum(item['product'].price * item['quantity'] for item in self.products)
        print(f"Total Price: {total_price}")
        # Другие действия при оформлении заказа

class OrderManager:
    def __init__(self):
        self.database = Database()
        self.current_order = None

    def create_order(self, user):
        # Создание нового заказа
        self.current_order = Order(user)

    def add_product_to_order(self, product_name, quantity):
        # Добавление продукта в текущий заказ
        product = self.database.get_product(product_name)
        if product:
            self.current_order.add_product(product, quantity)
        else:
            print(f"Product {product_name} not found.")

    def display_cart(self):
        # Вывод корзины текущего заказа
        if self.current_order:
            self.current_order.display_cart()
        else:
            print("No active order.")

    def checkout(self):
        # Оформление текущего заказа
        if self.current_order:
            self.current_order.checkout()
            # Дополнительные действия после оформления заказа
            self.current_order = None
        else:
            print("No active order.")
class Database:
    def __init__(self):
        self.users = []
        self.products = []

    def save_user(self, user):
        # Сохранение пользователя в базе данных
        self.users.append(user)

    def get_user(self, username):
        # Получение пользователя из базы данных
        for user in self.users:
            if user.username == username:
                return user
        return None

    def save_product(self, product):
        # Сохранение продукта в базе данных
        self.products.append(product)

    def get_product(self, product_name):
        # Получение продукта из базы данных
        for product in self.products:
            if product.name == product_name:
                return product
        return None