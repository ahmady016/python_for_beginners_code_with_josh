########################################################################################
from helpers import generate_id
########################################################################################
class Order:
    def __init__(self, store, customer, purchase_date):
        ### regular fields
        self.id = generate_id(8)
        self.store = store
        self.customer = customer
        self.purchase_date = purchase_date
        self.order_items = {}
        ### backing fields for getters and setters
        ### (computed properties when adding or updating or removing items)
        self.__total_cost = 0.0
        self.__average_cost = 0.0

    @property
    def total_cost(self):
        return self.__total_cost
        # return sum(item["total_price"] for item in self.order_items.values()) if len(self) > 0 else 0
    @total_cost.setter
    def total_cost(self, value):
        self.__total_cost = value

    @property
    def average_cost(self):
        return round(self.__average_cost, 2)
        # return round(self._total_cost / len(self), 2) if len(self) > 0 else 0
    @average_cost.setter
    def average_cost(self, value):
        self.__average_cost = value

    def has_items(self):
        return len(self.order_items) > 0
    def get_item_info(self, product_id):
        item = self.order_items.get(product_id)
        return f"""
        Product: {item["product"].name}
        Quantity: {item["quantity"]}
        Unit Price: {item["unit_price"]}
        Total Price: {item["total_price"]}
    _________________"""
    def get_items_info(self):
        if len(self) > 0:
            return "\n".join([self.get_item_info(product_id) for product_id in self.order_items.keys()])
        else:
            return "No items in this order"

    def add_item(self, product, quantity=1, unit_price=0.0):
        total_price = quantity * unit_price
        self.order_items[product.id] = {
            "product": product,
            "quantity": quantity,
            "unit_price": unit_price,
            "total_price": total_price
        }
        self.total_cost += total_price
        self.average_cost = self.total_cost / len(self)

    def update_item(self, product_id, quantity=0, unit_price=0.0):
        if product_id in self.order_items:
            quantity = quantity if quantity else self.order_items[product_id]["quantity"]
            unit_price = unit_price if unit_price else self.order_items[product_id]["unit_price"]
            old_total_price = self.order_items[product_id]["total_price"]
            new_total_price = quantity * unit_price
            self.order_items[product_id]["quantity"] += quantity
            self.order_items[product_id]["unit_price"] = unit_price
            self.order_items[product_id]["total_price"] = new_total_price
            self.total_cost += new_total_price - old_total_price
            self.average_cost = self.total_cost / len(self)

    def remove_item(self, product_id):
        if product_id in self.order_items:
            self.total_cost -= self.order_items[product_id]["total_price"]
            self.average_cost = self.total_cost / len(self)
            del self.order_items[product_id]

    def __getitem__(self, product_id):
        return self.order_items[product_id]
    def __setitem__(self, product_id, product, quantity=1, unit_price=0.0):
        if product_id not in self.order_items:
            self.order_items[product_id] = self.add_item(product, quantity, unit_price)
        else:
            self.update_item(product_id, quantity, unit_price)
    def __delitem__(self, product_id):
        del self.order_items[product_id]

    def __len__(self):
        return len(self.order_items)
    def __bool__(self):
        return len(self.order_items) > 0
    def __contains__(self, product_id):
        return product_id in self.order_items

    def __iter__(self):
        return iter(self.order_items.values())
    def __next__(self):
        return next(self.order_items.values())
    def __reversed__(self):
        return reversed(self.order_items.values())

    def __str__(self):
        return f"""__________________________
    Order ID: {self.id}
    Store: {self.store.name}
    Customer: {self.customer.full_name}
    Purchase Date: {self.purchase_date}
    Items ({len(self)}): {self.get_items_info()}
    Total Cost: {self.total_cost}
___________________________"""

    def __repr__(self):
        return f"Order({self.id}, {self.store.name}, {self.customer.full_name}, {self.purchase_date}), {len(self)} items, total: {self.total_cost}, average: {self.average_cost}"
