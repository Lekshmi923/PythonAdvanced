class Category:
    def __init__(self):
        self.category_name=input("Enter the category name: ")

    def show_category(self):
        print("Category",self.category_name)

class Product(Category):
    def __init__(self):
        super().__init__()
        self.product_name=input("Enter the product name: ")
        self.price=int(input("Enter the price of product: "))
        self.quantity=int(input("Enter the quantity of product: "))

    def total_price(self):
        self.total=self.price*self.quantity
        print("The total price is",self.total)

p=Product()
p.show_category()
p.total_price()