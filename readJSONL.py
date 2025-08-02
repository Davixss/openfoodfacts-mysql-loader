# ================================================================================
#  File: readJSONL.py
#  Description: Script to extract food products data from OpenFoodFacts JSONL file
#  Author: Davide Giuseppe Allegra
#  Source: https://it.openfoodfacts.org
#  License: For educational or non-commercial use. Attribution required.
# ================================================================================

import json

# File configuration
FILE_NAME_PRODUCTS_JSONL = 'openfoodfacts-products.jsonl'
FILE_NAME_PRODUCTS_CREATED = 'products.txt'
READ_MAX_LIMIT = False
READ_MAX_LIMIT_PRODUCTS = 100
READ_NATIONS = ['italy'] # Set [] to all nations

# Global variables
n_products = 0
unique_categories = set()


with open(FILE_NAME_PRODUCTS_JSONL, 'r', encoding='utf-8') as openfood_file:
    with open(FILE_NAME_PRODUCTS_CREATED, 'w', encoding='utf-8') as output_file:
        for i, line in enumerate(openfood_file):
            try:
                data = json.loads(line.strip())

                # Check required fields
                if not isinstance(data.get('countries_tags'), list) or \
                   not isinstance(data.get('brands'), str) or \
                   not isinstance(data.get('categories_hierarchy'), list):
                    continue

                if READ_NATIONS:
                    if not any(f'en:{nation.lower()}' in data.get('countries_tags', []) for nation in READ_NATIONS):
                        continue

                # Extract data
                name = data.get('product_name', f'product_{i+1}')
                brand = data['brands']
                nutriments = data.get('nutriments', {})
                raw_categories = data['categories_hierarchy']
                categories_en = [cat.replace('en:', '') for cat in raw_categories if isinstance(cat, str) and cat.startswith('en:')]

                calories = nutriments.get('energy-kcal_100g', 0)
                proteins = nutriments.get('proteins_100g', 0)
                fat = nutriments.get('fat_100g', 0)
                carbohydrates = nutriments.get('carbohydrates_100g', 0)

                # Skip the product if some data missing
                if brand.strip() == '':
                    continue

                if not categories_en:
                    continue

                if calories==0 and proteins==0 and fat==0 and carbohydrates==0:
                    continue

                categories = ','.join(categories_en)

                # Write in format: name|brand|category|calories|proteins|fat|carbohydrates
                output_line = f"{name}|{brand}|{categories}|{calories}|{proteins}|{fat}|{carbohydrates}\n"
                output_file.write(output_line)
                n_products += 1

                if READ_MAX_LIMIT and (n_products >= READ_MAX_LIMIT_PRODUCTS):
                    break

            except (json.JSONDecodeError, TypeError) as e:
                print(f"! Error at line {i+1}: {e}")


print(f">> Products found: {n_products}")