import os
import sys
import pymysql
from colorama import Fore
from dotenv import load_dotenv

# Load environment variables from .env file

load_dotenv()

DB_HOST = os.getenv('DB_HOST')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_NAME = os.getenv('DB_NAME')

# Connect to the MySQL database

try:
    connection = pymysql.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME
    )
except pymysql.MySQLError as e:
    print(f"Error connecting to database: {e}") # you can demonstrate this works by changing the details in the .env file
    sys.exit(1) #exits with "1" error code - to show something went wrong with $?

# Clear screen function

def clear():
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')

# Defining SQL functions that read/write - data/storage layer (?)

def read_products():
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT item, price FROM products") 
            products = cursor.fetchall()
        return [{"item": product[0], "price": product[1]} for product in products]
    except Exception as e:
        print(f"Error reading products: {e}")
        return []

def write_products(products):
    try:
        with connection.cursor() as cursor:
            for product in products:
                cursor.execute(
                    "INSERT INTO products (item, price) VALUES (%s, %s)",
                    (product['item'], product['price'])
                )
        connection.commit()
    except Exception as e:
        print(f"Error writing products: {e}")

def read_orders():
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM orders")
            orders = cursor.fetchall()
        return [{"customer_name": order[1], "customer_address": order[2], "customer_phone": order[3], "status": order[4]} for order in orders]
    except Exception as e:
        print(f"Error reading orders: {e}")
        return []

def write_orders(orders):
    try:
        with connection.cursor() as cursor:
            for order in orders:
                cursor.execute(
                    "INSERT INTO orders (customer_name, customer_address, customer_phone, status) VALUES (%s, %s, %s, %s)",
                    (order['customer_name'], order['customer_address'], order['customer_phone'], order['status'])
                )
        connection.commit()
    except Exception as e:
        print(f"Error writing orders: {e}")

def read_couriers():
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT courier_name FROM couriers")
            couriers = cursor.fetchall()
        return [{"courier_name": courier[0]} for courier in couriers]
    except Exception as e:
        print(f"Error reading couriers: {e}")
        return []

def write_couriers(couriers):
    try:
        with connection.cursor() as cursor:
            for courier in couriers:
                cursor.execute(
                    "INSERT INTO couriers (courier_name) VALUES (%s)",
                    (courier['courier_name'],)
                )
        connection.commit()
    except Exception as e:
        print(f"Error writing couriers: {e}")

# Defining menu screen functions

def print_main_menu():
    print(f"{Fore.LIGHTMAGENTA_EX}⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡶⠶⢦⣄⠀⠀⠀⠀⠀⣴⠟⠛⢧⣠⣶⣿⠻⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠁⡟⠦⠌⠛⠉⠉⠉⢹⠇⢠⣶⣼⣷⣞⢙⣧⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣤⠃⠀⠀⠀⠀⠀⠀⣿⠀⠈⢻⡃⠀⢸⡿⡄⠈⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⠁⠀⠀⠀⠀⠀⠀⠀⠘⠷⠖⠛⠛⠛⢿⡗⢋⣴⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠛⢻⡀⢀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡶⠾⣷⠆⠀⠁⣤⡀⠀⠀⠀⠀⠀⠀⠀⢀⣤⡀⠀⠐⢺⡟⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⢿⡦⠀⠀⠛⠃⠀⠀⢠⢶⣄⠀⠀⠈⠛⠀⠀⠀⣺⠓⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⣼⢧⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡿⣖⡀⣀⣀⡀⠀⠈⠉⠉⠀⠀⣀⣀⣀⠀⣲⣯⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠶⡆\n⢻⡈⠻⣦⣀⣀⣀⣀⣀⠀⠀⠀⠁⣴⠟⠉⠁⠀⠉⠛⢦⡀⢀⡴⠛⠉⠁⠈⠙⠻⣄⠀⠁⣀⣠⣤⣤⣤⣤⡤⠖⠋⣸⠇\n⡿⠳⣤⣀⡀⠀⠀⠉⠉⠉⠳⢦⣼⠃⠀⠀⠀⠀⠀⠀⠀⠿⠋⠀⠀⠀⠀⠀⠀⠀⠹⣦⡞⠉⠀⠀⠀⠀⠀⢀⣠⠶⢻⡆\n`⠻⣦⣀⠀⠀⠀⡴⠶⢦⡀⠀⠈⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⡴⠚⠳⡄⠈⢉⣀⣠⡾⠁\n⠀⠸⣍⣉⣁⡀⣇⠀⠀⠑⠀⢠⡿⣆⠀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⢷⡀⠀⠓⠀⢀⡇⢤⣈⣭⠿⠁⠀\n⠀⠀⠀⠙⠷⠤⠿⠶⠦⠶⠞⠋⠘⢻⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡼⠃⠈⠻⠦⠴⠖⠻⠶⠶⠛⠁⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⠻⢦⣄⠀⠀⠀⠀⠀⠀⠀⠀⣠⡴⠛⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠶⣄⡀⢀⣤⠶⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n\nWelcome to the Hello Kitty cafe.\n｡･ﾟﾟ･(＞_＜)･ﾟﾟ･｡.˚₊‧꒰ა 𓂋 ໒꒱ ♥︎")
    print(f"{Fore.LIGHTMAGENTA_EX}\n~Main menu~")
    print("1. Products menu")
    print("2. Orders menu")
    print("3. Courier menu")
    print(f"0. Exit\n{Fore.WHITE}")

def print_product_menu():
    print(f"\n{Fore.CYAN}~Product Menu~")
    print("1. View products")
    print("2. Add product")
    print("3. Update product")
    print("4. Delete product")
    print(f"0. Return to main menu\n{Fore.WHITE}")

def print_order_menu():
    print(f"\n{Fore.RED}~Order Menu~")
    print("1. View orders")
    print("2. Add order")
    print("3. Update order status")
    print("4. Update order")
    print("5. Delete order")
    print(f"0. Return to main menu\n{Fore.WHITE}")

def print_courier_menu():
    print(f"\n{Fore.YELLOW}~Courier Menu~")
    print("1. View couriers")
    print("2. Add courier")
    print("3. Update courier")
    print("4. Delete courier")
    print(f"0. Return to main menu\n{Fore.WHITE}")

# run main application

while True:
    print_main_menu()
    try:
        main_menu_choice = int(input("Enter your choice: "))
    except ValueError:
        clear()
        print("Please enter a valid integer.\n")
        continue
    if main_menu_choice not in [0, 1, 2, 3]:
        clear()
        print("Invalid choice. Please choose from the available options.\n")
        continue

    if main_menu_choice == 0:
        break

    if main_menu_choice == 1:
        clear()
        while True:
            print_product_menu()
            try:
                product_menu_choice = int(input("Enter your choice: "))
            except ValueError:
                clear()
                print("Please enter a valid integer.")
                continue
            if product_menu_choice not in [0, 1, 2, 3, 4]:
                clear()
                print("Invalid choice. Please choose from the available options")
                continue

            if product_menu_choice == 0:
                clear()
                break

            if product_menu_choice == 1:
                clear()
                print("\nProducts List:")
                products = read_products()
                for product in products:
                    print(f"Name: {product['item']}, Price: {product['price']}")

            elif product_menu_choice == 2:
                clear()
                new_product_name = input("Enter product name: ")
                new_product_price = input("Enter price of product: ")
                products = read_products()
                new_product = {"item": new_product_name, "price": new_product_price}
                products.append(new_product)
                write_products(products)
                clear()
                print(f"Product '{new_product_name}' added for {new_product_price}.")
                print("\nNew product list:")
                for product in products:
                    print(product)

            elif product_menu_choice == 3:
                clear()
                products = read_products()
                print("Products List:")
                for index, product in enumerate(products):
                    print(f"{index}: Name: {product['item']}, Price: {product['price']}")
                product_index = int(input("Enter product index to update: "))
                new_product_name = input("Enter new product name: ")
                new_product_price = input("Enter new product price: ")
                if new_product_name:
                    products[product_index]['item'] = new_product_name
                if new_product_price:
                    products[product_index]['price'] = new_product_price
                write_products(products)
                print("Product updated.")

            elif product_menu_choice == 4:
                clear()
                products = read_products()
                print("Products List:")
                for index, product in enumerate(products):
                    print(f"{index}: {product}")
                product_index = int(input("Enter product index to delete: "))
                products.pop(product_index)
                write_products(products)
                print("Product deleted.")

    elif main_menu_choice == 2:
        clear()
        while True:
            print_order_menu()
            try:
                order_menu_choice = int(input("Enter your choice: "))
            except ValueError:
                clear()
                print("Please enter a valid integer.")
                continue
            if order_menu_choice not in [0, 1, 2, 3, 4, 5]:
                clear()
                print("Invalid choice. Please choose from the available options.")
                continue

            if order_menu_choice == 0:
                clear()
                break

            if order_menu_choice == 1:
                clear()
                print("Orders List:")
                for order in read_orders():
                    print(order)

            elif order_menu_choice == 2:
                customer_name = input("Enter customer name: ")
                customer_address = input("Enter customer address: ")
                customer_phone = input("Enter customer phone number: ")
                order = {
                    "customer_name": customer_name,
                    "customer_address": customer_address,
                    "customer_phone": customer_phone,
                    "status": "preparing"
                }
                orders = read_orders()
                orders.append(order)
                write_orders(orders)
                print("Order added.")

            elif order_menu_choice == 3:
                orders = read_orders()
                print("\nOrders List:")
                for index, order in enumerate(orders):
                    print(f"{index}: {order}")
                order_index = int(input("\nEnter order index to update status: "))
                print("\nOrder Status List:")
                print("0: preparing")
                print("1: shipped")
                print("2: delivered")
                status_index = int(input("Enter updated status: "))
                status_list = ["preparing", "shipped", "delivered"]
                orders[order_index]["status"] = status_list[status_index]
                write_orders(orders)
                print("Order status updated.")

            elif order_menu_choice == 4:
                orders = read_orders()
                print("\nOrders List:")
                for index, order in enumerate(orders):
                    print(f"{index}: {order}")
                order_index = int(input("\nEnter order index to update: "))
                for key in orders[order_index]:
                    new_value = input(f"Enter new value for {key} (leave blank to keep current value): ")
                    if new_value:
                        orders[order_index][key] = new_value
                write_orders(orders)
                print("Order updated.")

            elif order_menu_choice == 5:
                orders = read_orders()
                print("Orders List:")
                for index, order in enumerate(orders):
                    print(f"{index}: {order}")
                order_index = int(input("Enter index to delete: "))
                orders.pop(order_index)
                write_orders(orders)
                print("Order deleted.")

    elif main_menu_choice == 3:
        clear()
        while True:
            print_courier_menu()
            try:
                courier_menu_choice = int(input("Enter your choice: "))
            except ValueError:
                clear()
                print("Please enter a valid integer.")
                continue
            if courier_menu_choice not in [0, 1, 2, 3, 4]:
                clear()
                print("Invalid choice. Please choose from the available options.")
                continue

            if courier_menu_choice == 0:
                clear()
                break

            if courier_menu_choice == 1:
                clear()
                print("\nCouriers List:")
                couriers = read_couriers()
                for courier in couriers:
                    print(courier)

            elif courier_menu_choice == 2:
                clear()
                new_courier_name = {"courier_name": input("Enter courier name: ")}
                couriers = read_couriers()
                couriers.append(new_courier_name)
                write_couriers(couriers)
                clear()
                print(f"Courier '{new_courier_name}' added.")
                print("\nNew couriers list:")
                for courier in couriers:
                    print(courier)

            elif courier_menu_choice == 3:
                clear()
                couriers = read_couriers()
                print("Couriers List:")
                for index, courier in enumerate(couriers):
                    print(f"{index}: {courier}")
                courier_index = int(input("Enter courier index to update: "))
                new_courier_name = input("Enter new courier name: ")
                if new_courier_name:
                    couriers[courier_index] = new_courier_name
                    write_couriers(couriers)
                    print("Courier updated.")

            elif courier_menu_choice == 4:
                clear()
                couriers = read_couriers()
                print("Couriers List:")
                for index, courier in enumerate(couriers):
                    print(f"{index}: {courier}")
                courier_index = int(input("Enter courier index to delete: "))
                couriers.pop(courier_index)
                write_couriers(couriers)
                print("Courier deleted.")

print(f"{Fore.LIGHTMAGENTA_EX} Goodbye! (´｡• ω •｡`) ⋆｡°✩ ⋆⁺｡˚⋆˙‧₊✩₊‧˙⋆˚｡⁺⋆ ✩°｡⋆.・゜゜・゜゜・．｡･ﾟﾟ･             ･ﾟﾟ･｡")