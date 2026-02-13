########################################################################################
import math
from helpers import generate_id
########################################################################################
class Store:
    def __init__(self, name, location):
        self.id = generate_id(8)
        self.name = name
        self.location = location

        self.products = {}
        self.orders = {}

    def get_order(self, order_id):
        if order_id in self.orders:
            return self.orders[order_id]
    def get_orders(self):
        if len(self.orders) == 0:
            return []
        return self.orders.values()
    def get_customer_orders(self, customer_id):
        if len(self.orders) == 0:
            return []
        return [order for order in self.orders.values() if order.customer.id == customer_id]

    def add_order(self, order):
        self.orders[order.id] = order
    def remove_order(self, order_id):
        del self.orders[order_id]
    def add_orders(self, orders):
        for order in orders:
            self.add_order(order)

    def add_product(self, product, quantity=1, unit_price=0.0):
        self.products[product.id] = {"product": product, "quantity": quantity, "unit_price": unit_price}
    def update_product(self, product_id, quantity=0, unit_price=0.0):
        if product_id in self.products:
            quantity = quantity if quantity else self.products[product_id]["quantity"]
            unit_price = unit_price if unit_price else self.products[product_id]["unit_price"]
            self.products[product_id]["quantity"] += quantity
            self.products[product_id]["unit_price"] = unit_price

    def get_product_info(self, product_id):
        if product_id in self.products:
            product_info = self.products[product_id]
            return f"""
            Product: {product_info["product"].name}
            Quantity: {product_info["quantity"]}
            Unit Price: {product_info["unit_price"]}
        _____________________"""
    def get_all_products_info(self):
        if len(self) == 0:
            return []
        return "\n".join([self.get_product_info(product_id) for product_id in self.products])
    def get_out_of_stock_products_info(self):
        if len (self) == 0:
            return []
        return "\n".join([self.get_product_info(product_id) for product_id in self.products if self.products[product_id]["quantity"] == 0])
    def get_in_stock_products_info(self):
        if len (self) == 0:
            return []
        return "\n".join([self.get_product_info(product_id) for product_id in self.products if self.products[product_id]["quantity"] > 0])
    def get_category_products_info(self, category):
        if len (self) == 0:
            return []
        return "\n".join([self.get_product_info(product_id) for product_id in self.products if self.products[product_id]["product"].category == category])

    def get_all_products(self):
        if len (self) == 0:
            return []
        return self.products.values()
    def get_out_of_stock_products(self):
        if len (self) == 0:
            return []
        return [product_info for product_info in self.products.values() if product_info["quantity"] == 0]
    def get_in_stock_products(self):
        if len (self) == 0:
            return []
        return [product_info for product_info in self.products.values() if product_info["quantity"] > 0]
    def get_products_by_category(self, category):
        if len (self) == 0:
            return []
        return [product_info for product_info in self.products.values() if product_info["product"].category == category]

    def __getitem__(self, product_id):
        return self.products[product_id]
    def __setitem__(self, product_id, product, quantity=1, unit_price=0.0):
        if product_id not in self.products:
            self.products[product_id] = self.add_product(product, quantity, unit_price)
        else:
            self.update_product(product_id, quantity, unit_price)
    def __delitem__(self, product_id):
        del self.products[product_id]

    def __len__(self):
        return len(self.products)
    def __bool__(self):
        return len(self.products) > 0
    def __contains__(self, product_id):
        return product_id in self.products

    def __iter__(self):
        return iter(self.products.values())
    def __next__(self):
        return next(self.products.values())
    def __reversed__(self):
        return reversed(self.products.values())

    def __add__(self, other):
        if not isinstance(other, Store):
            print("Can only add Stores")
        newStore = Store(f"{self.name} & {other.name}", f"{self.location} & {other.location}")
        union_products_keys = set(self.products.keys()) | set(other.products.keys())
        for product_id in union_products_keys:
            if product_id in self.products and product_id in other.products:
                newStore[product_id] = {
                    "product": self[product_id]["product"],
                    "quantity": self[product_id]["quantity"] + other[product_id]["quantity"],
                    "unit_price": math.max(self[product_id]["unit_price"], other[product_id]["unit_price"])
                }
            elif product_id in self.products:
                newStore[product_id] = {**self[product_id]}
            else:
                newStore[product_id] = {**other[product_id]}
        return newStore

    def __str__(self):
        return f"{self.name} Store is located in {self.location} and has {len(self)} products"
    def __repr__(self):
        return self.__str__()
