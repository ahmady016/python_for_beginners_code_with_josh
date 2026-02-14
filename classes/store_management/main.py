# build a simple store management system that:
# ----------------------------------------------------------------------------------
# contains a customer, product, store and order classes
# the customer class has first name, last name, address, birth year and gender
# the product class has name, description and category
# the store class has name, location and list of products as dictionary
# the products dictionary has product id as key and the value contains
# product object, unit price and quantity
# allow admin to get a list of all products in the store
# allow admin to get a list of all out of stock products in the store [quantity = 0]
# allow admin to get a list of all in stock products in the store [quantity > 0]
# allow admin to get a list of all products in the store by specific category
# the order class has customer, store, purchase date and list of order items
# each order item has product, quantity and unit price
# then calculate the total cost of each item and the total cost of the order
######################################################################################
# test the store management system:
# ------------------------------------------------------------------------------------
# create 3 customers
# create 12 products
# create 2 stores
# add 6 products to each store with random quantity and unit price
# add 3 orders with random customer, product, quantity and unit price to each store
# get a list of all products in the store
# get a list of all out of stock products in the store
# get a list of all in stock products in the store
# get a list of all products in the store by specific category
# get a list of all orders in the store
# get a list of all orders in the store by specific customer
######################################################################################
from random import randint, choice, choices
from helpers import get_random_date_between, get_zero_formatted_number
from customer import Customer
from product import Product
from store import Store
from order import Order
######################################################################################
print("############################")
print("store management system test started")
print("############################")
######################################################################################
PRODUCT_CATEGORIES = ["food", "clothing", "electronics", "books", "toys"]
######################################################################################
# create 3 customers
ahmed = Customer("ahmed", "mohamed", "cairo", 1990, "male")
sayed = Customer("sayed", "mohamed", "cairo", 1990, "male")
eman = Customer("eman", "mohamed", "cairo", 1990, "female")
######################################################################################
# create 20 products
products = [
    Product(
        f"product #{get_zero_formatted_number(i, 2)}",
        f"description of product #{get_zero_formatted_number(i, 2)}",
        choice(PRODUCT_CATEGORIES)
    )
    for i in range(1, 21)
]
######################################################################################
# create 2 stores
raya_store = Store("Raya store", "cairo")
zen_store = Store("Zen store", "fayoum")
######################################################################################
# add 10 products to each store with random quantity and unit price
for product in products[:10]:
    raya_store.add_product(product, randint(0, 50), randint(10, 1000))
for product in products[10:]:
    zen_store.add_product(product, randint(0, 50), randint(10, 1000))
######################################################################################
# add 3 orders with random customer, product, quantity and unit price to each store
for store in [raya_store, zen_store]:
    for customer in [ahmed, sayed, eman]:
        order = Order(store, customer, get_random_date_between("01-01-2024", "31-12-2025"))
        store_products = [productInfo["product"] for productInfo in store.products.values()]
        for product in choices(store_products, k=randint(3, 7)):
            order.add_item(product, randint(1, 10), randint(10, 1000))
        store.add_order(order)
######################################################################################
# get a list of all products in the store
print("all products in the raya store")
print("-------------------------")
print(raya_store.get_all_products_info())
######################################################################################
# get a list of all out of stock products in the store
print("all out of stock products in the raya store")
print("-------------------------")
print(raya_store.get_out_of_stock_products_info())
######################################################################################
# get a list of all in stock products in the store
print("all in stock products in the raya store")
print("-------------------------")
print(raya_store.get_in_stock_products_info())
######################################################################################
# get a list of all products in the store by specific category
print("all toys products in the raya store")
print("-------------------------")
print(raya_store.get_category_products_info("toys"))
######################################################################################
# get a list of all orders in the raya store
print("all orders in the raya store")
print("-------------------------")
for order in raya_store.get_orders():
    print(order)
######################################################################################
# get a list of all orders in the store by specific customer
print("all orders for sayed in the raya store")
print("-------------------------")
for order in raya_store.get_customer_orders(sayed.id):
    print(order)
######################################################################################
# get a list of all orders in the zen store
print("all orders in the zen store")
print("-------------------------")
for order in zen_store.get_orders():
    print(order)
######################################################################################
# get a list of all orders in the zen store by specific customer
print("all orders for ahmed in the zen store")
print("-------------------------")
for order in raya_store.get_customer_orders(ahmed.id):
    print(order)
######################################################################################
print("############################")
print("store management system test finished")
print("############################")
######################################################################################
