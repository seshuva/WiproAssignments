import os
import xml.etree.ElementTree as ET
from xml.dom import minidom

# File path for storing product data
PRODUCT_FILE = 'products.xml'


def load_product_data():
    if os.path.exists(PRODUCT_FILE):
        tree = ET.parse(PRODUCT_FILE)
        return tree.getroot()
    return ET.Element('products')


def save_product_data(products):
    tree = ET.ElementTree(products)
    tree.write(PRODUCT_FILE, encoding='utf-8', xml_declaration=True)


def add_product(product):
    products = load_product_data()
    product_elem = ET.SubElement(products, 'product')
    for key, value in product.items():
        child = ET.SubElement(product_elem, key)
        child.text = str(value)
    save_product_data(products)


def update_product(product_id, updated_info):
    products = load_product_data()
    for product in products.findall('product'):
        if product.find('id').text == str(product_id):
            for key, value in updated_info.items():
                product.find(key).text = str(value)
            save_product_data(products)
            return
    print(f"Product with ID {product_id} not found.")


def delete_product(product_id):
    products = load_product_data()
    for product in products.findall('product'):
        if product.find('id').text == str(product_id):
            products.remove(product)
            save_product_data(products)
            return
    print(f"Product with ID {product_id} not found.")


def get_product(product_id):
    products = load_product_data()
    for product in products.findall('product'):
        if product.find('id').text == str(product_id):
            return {child.tag: child.text for child in product}
    print(f"Product with ID {product_id} not found.")
    return None


def export_products_as_xml(file_path):
    products = load_product_data()
    xml_str = minidom.parseString(ET.tostring(products)).toprettyxml(indent="   ")
    with open(file_path, 'w') as file:
        file.write(xml_str)


# Example usage:
if __name__ == "__main__":
    # Adding products
    add_product({"id": 1, "name": "Laptop", "category": "Electronics", "price": 1000})
    add_product({"id": 2, "name": "Smartphone", "category": "Electronics", "price": 500})

    # Updating a product
    update_product(1, {"name": "Gaming Laptop", "price": 1500})

    # Deleting a product
    delete_product(2)

    # Retrieving a product
    product = get_product(1)
    if product:
        print(product)

    # Exporting products as XML
    export_products_as_xml('exported_products.xml')
