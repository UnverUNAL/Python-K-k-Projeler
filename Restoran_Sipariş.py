class MenuItem:
    def __init__(self,name,price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name} - {self.price}₺"

class Menu:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def display_menu(self):
        for item in self.items:
            print(item)

class Order:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def total_price(self):
        return sum(item.price for item in self.items)

    def display_order(self):
        print("Siparişiniz:")
        for item in self.items:
            print(item)
        print(f"Toplam: {self.total_price()}₺")

class Customer:
    def __init__(self, name):
        self.name = name
        self.order = Order()

    def place_order(self, menu_item):
        self.order.add_item(menu_item)

    def view_order(self):
        print(f"Müşteri: {self.name}")
        self.order.display_order()

class Restaurant:
    def __init__(self, name):
        self.name = name
        self.menu = Menu()
        self.customers = []

    def add_customer(self, customer):
        self.customers.append(customer)

    def take_order(self, customer_name, menu_item_name):
        customer = next((c for c in self.customers if c.name == customer_name), None)
        item = next((i for i in self.menu.items if i.name == menu_item_name), None)
        if customer and item:
            customer.place_order(item)
        else:
            print("Müşteri veya ürün bulunamadı.")

    def show_menu(self):
        self.menu.display_menu()

pizza = MenuItem("Pizza", 50)
pasta = MenuItem("Pasta", 40)
cola = MenuItem("Cola", 10)

restaurant = Restaurant("Lezzet Restoran")

restaurant.menu.add_item(pizza)
restaurant.menu.add_item(pasta)
restaurant.menu.add_item(cola)

customer1 = Customer("Ali")
restaurant.add_customer(customer1)

restaurant.show_menu()

restaurant.take_order("Ali", "Pizza")
restaurant.take_order("Ali", "Cola")

customer1.view_order()
