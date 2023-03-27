import json

def print_product_names_from_json_file(path):
    # Open the JSON file using the path and read mode with the 'utf-8' codec
    with open(path, 'r', encoding='utf-8') as file:
        # Load the contents of the file using the json.load() method
        json_data = json.load(file)

    # Extract the product list from the parsed JSON data
    products = json_data['props']['pageProps']['initialState']['products']['list']

    # Loop through each product in the list and print its rank and name
    for product in products:
        rank = product['item']['rank']
        name = product['item']['productTitle']
        print(str(rank) + '/' + name)

path = r'C:\Users\Data2\OneDrive\바탕 화면\윤\코드\test.json'

print(len([i for i in print_product_names_from_json_file(path)]))


