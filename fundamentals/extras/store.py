class Store:
    def __init__(self, store_name, products = []):
        self.name = store_name
        self.products = products
    def add_product(self, new_product):
        self.products.append(new_product)
    def sell_product (self, id):
        self.products[id].print_info()
        self.products.pop[id]
        print("Product removed from store.")
    def inflation(self, percent_increase):
        for product in self.products:
            product.update_price(percent_increase, True)
    def set_clearance(self, category, percent_discount):
        for product in self.products:
            if (product.category == category):
                product.update_price(percent_discount, False)
    def print_all_products(self):
        print (f"Product inventory for {self.name}:")
        for product in self.products:
            product.print_info()

class Product:
    currProductID = 0
    def __init__(self, product_name, category, price):
        self.name = product_name
        self.category = category
        self.price = price
        type(self).currProductID += 1
        self.productID = type(self).currProductID
    def update_price(self, percent_change, is_increased):
        if (is_increased):
            self.price += self.price*percent_change
        else:
            self.price -= self.price*percent_change
    def print_info(self):
        print(f"Product: {self.name}  Product ID: {self.productID}  Category: {self.category}  Price: ${self.price:.2f}")

grocery = Store("Whole Foods")
grocery.add_product(Product("Cherries", "Fruit", 3.99))
grocery.add_product(Product("Bananas", "Fruit", 1.19))
grocery.add_product(Product("Milk", "Dairy", 2.99))
grocery.add_product(Product("Cheerios", "Cereal", 3.99))
grocery.print_all_products()

grocery.inflation(.1)
grocery.set_clearance("Fruit", .2)

grocery.print_all_products()



