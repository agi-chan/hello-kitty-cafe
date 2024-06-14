# Hello Kitty Café

```
⠀⠀⠀⠀⢀⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⣠⠾⠛⠶⣄⢀⣠⣤⠴⢦⡀⠀⠀⠀⠀
⠀⠀⠀⢠⡿⠉⠉⠉⠛⠶⠶⠖⠒⠒⣾⠋⠀⢀⣀⣙⣯⡁⠀⠀⠀⣿⠀⠀⠀⠀
⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⢸⡏⠀⠀⢯⣼⠋⠉⠙⢶⠞⠛⠻⣆⠀⠀⠀
⠀⠀⠀⢸⣧⠆⠀⠀⠀⠀⠀⠀⠀⠀⠻⣦⣤⡤⢿⡀⠀⢀⣼⣷⠀⠀⣽⠀⠀⠀
⠀⠀⠀⣼⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠙⢏⡉⠁⣠⡾⣇⠀⠀⠀
⠀⠀⢰⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠋⠉⠀⢻⡀⠀⠀
⣀⣠⣼⣧⣤⠀⠀⠀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡀⠀⠀⠐⠖⢻⡟⠓⠒    < a demonstration of basic Python principles and SQL database management
⠀⠀⠈⣷⣀⡀⠀⠘⠿⠇⠀⠀⠀⢀⣀⣀⠀⠀⠀⠀⠿⠟⠀⠀⠀⠲⣾⠦⢤⠀
⠀⠀⠋⠙⣧⣀⡀⠀⠀⠀⠀⠀⠀⠘⠦⠼⠃⠀⠀⠀⠀⠀⠀⠀⢤⣼⣏⠀⠀⠀
⠀⠀⢀⠴⠚⠻⢧⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⠞⠉⠉⠓⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠈⠉⠛⠛⠶⠶⠶⣶⣤⣴⡶⠶⠶⠟⠛⠉⠀⠀⠀⠀⠀⠀⠀
```

This Python script manages product, order, and courier information in a MySQL database for an imaginary "Hello Kitty" café.

__Client requirements__: Code should handle bad input, be readable with comments, and include functionalities like menus, lists, orders, and couriers stored as dictionaries. It should have unit tests (!) and use text files, CSV, or MySQL for data persistence. The GitHub repo needs a complete README and have frequent commits.


## Features

- Connects to a MySQL database using credentials stored in a .env file (note: you'll need to create a .env file with your database details as shown below).
- CRUD (Create, Read, Update, Delete) operations for products, orders, and couriers.
- Colourful and themed text menus for UI/UX.
- Error handling for database connection and user input.

## Requirements

- Python: Ensure you have Python installed on your machine.
- MySQL: A MySQL database server (I used Docker) should be running.
- pymysql library (install using _pip install pymysql_)
- colorama library (install using _pip install colorama_)
- python-dotenv library (install using _pip install python-dotenv_)

## Setup

Create a MySQL database and tables for products, orders, and couriers:

```
CREATE DATABASE hello_kitty_cafe;

USE hello_kitty_cafe;

CREATE TABLE products (
    id INT AUTO_INCREMENT PRIMARY KEY,
    item VARCHAR(255) NOT NULL,
    price DECIMAL(10, 2) NOT NULL
);

CREATE TABLE orders (
    id INT AUTO_INCREMENT PRIMARY KEY,
    customer_name VARCHAR(255) NOT NULL,
    customer_address TEXT NOT NULL,
    customer_phone VARCHAR(20) NOT NULL,
    status VARCHAR(50) NOT NULL
);

CREATE TABLE couriers (
    id INT AUTO_INCREMENT PRIMARY KEY,
    courier_name VARCHAR(255) NOT NULL
);
```

Create a .env file in the same directory as the script with the following variables:

```
DB_HOST=host (localhost)
DB_USER=username (root)
DB_PASSWORD=password (password)
DB_NAME=database_name (hello_kitty_cafe)
```

## Running the Script

Open a terminal in the directory containing the script and .env file.
Run the script using _python app.py_.

## Usage

The script presents a colour-formatted menu with options to manage products, orders, and couriers. Each section has further options for CRUD operations. Use the corresponding numbers to navigate through the menus.

## Disclaimer

This script is for educational purposes only. It demonstrates basic database interaction with Python and should be further secured and enhanced for production use.