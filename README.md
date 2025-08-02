# openfoodfacts-mysql-loader
This project allows you to import product data from [Open Food Facts](https://it.openfoodfacts.org) into a MySQL database.  
The data is first extracted from a `.jsonl` file and saved in `.txt` format using a filtering process, then loaded into a structured MySQL table.

# Features
- Parses and filters Open Food Facts data from a `.txt` file (exported from `.jsonl`)
- Extracts nutritional values and other fields
- Filters only products from specified countries (e.g., `Italy`)
- Skips entries with missing or incomplete nutritional information
- Inserts product data into a MySQL database

# Products list file .txt
The input file is a `.txt` file where each line represents a product.
Each value in the line is separated by a vertical bar (|), and the position of each value corresponds to a specific column in the following order:
product name, brand, categories, energy (kcal/100g), proteins (g/100g), fat (g/100g), carbohydrates (g/100g).

Example line in `.txt`:

Vellutata dolce Datterino di Sicilia|Cirio|plant-based-foods-and-beverages,plant-based-foods,fruits-and-vegetables-based-foods,vegetables-based-foods,tomatoes-and-their-products,tomato-pulps|56|1.8|0.2|9.7

# Requirements 
- Install Python and mysql-connector-python library
- Install MySQL

# Download JSONL data, read and import 
- Go to https://it.openfoodfacts.org/data
- Go to the JSONL Data Export section and download the compressed .gz file (> 9GB)
- Open the folder where you saved the .jsonl file (for example, desktop/openfoodfacts folder)
- Download the files "loadJSON.py" and "loadProductsIntoDb.py" from this repository
- Run "loadJSON.py" and wait for products.txt file to be created
- Run "loadProductsIntoDb.py" and wait until it complete the import data into the MySQL table
