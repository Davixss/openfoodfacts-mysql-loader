# =================================================================================
#  File: loadProductsIntoDb.py
#  Description: Script to load formatted txt food products data into MySQL database
#  Author: Davide Giuseppe Allegra
#  Source: https://it.openfoodfacts.org
#  License: For educational or non-commercial use. Attribution required.
# =================================================================================

import mysql.connector

# File configuration
FILE_NAME_PRODUCTS = 'products.txt'

# MySQL configuration
DB_HOST = 'localhost'
DB_USER = 'root'
DB_PASSWORD = 'CHANGE_THIS_SET_YOUR_DB_PASS'
DB_DATABASE = 'CHANGE_THIS_SET_YOUR_DB_NAME'
DB_TABLE_NAME_PRODUCTS = 'tb_products'


conn = mysql.connector.connect(
    host=DB_HOST,
    user=DB_USER,
    password=DB_PASSWORD,
    database=DB_DATABASE
)
cursor = conn.cursor()

create_query = f"""
    CREATE TABLE IF NOT EXISTS {DB_TABLE_NAME_PRODUCTS} (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255),
        brand VARCHAR(255),
        categories TEXT,
        calories FLOAT,
        proteins FLOAT,
        fat FLOAT,
        carbohydrates FLOAT
    )
"""
cursor.execute(create_query)


# Read the file containing all the products 
# Format: name|brand|categories|calories|proteins|fat|carbohydrates
with open(FILE_NAME_PRODUCTS, 'r', encoding='utf-8') as file:
    for i, line in enumerate(file):
        line = line.strip()
        if not line:
            continue

        try:
            parts = line.split('|')
            if len(parts) != 7:
                print(f">> Row {i+1} not valid: {line}")
                continue

            name, brand, categories, calories, proteins, fat, carbohydrates = parts

            insert_query = f"""
                INSERT INTO {DB_TABLE_NAME_PRODUCTS} 
                (name, brand, categories, calories, proteins, fat, carbohydrates) 
                VALUES
                (%s, %s, %s, %s, %s, %s, %s)
            """
            values = (
                name.strip(), brand.strip(), categories.strip(),
                float(calories), float(proteins), float(fat), float(carbohydrates)
            )

            cursor.execute(insert_query, values)

        except Exception as e:
            print(f">> Error in row {i+1}: {e}")


conn.commit()
cursor.close()
conn.close()

print(">> Completed")