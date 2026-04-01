# PRODUCT STORE
class Product:
    count = 0 # to store the count of products

    def __init__(self, name, price):
        self.name = name
        self.price = price
        Product.count += 1

    def get_info(self):
        print(f"price of {self.name} is {self.price}")

    @classmethod
    def get_count(cls):
        print(f"Count of product is {cls.count}")

    @staticmethod
    def cal_discount(price, discount):
        print(f"discpunted Price is  {price - (price * discount / 100)}")


p1 = Product("phone", 10_000)
p1 = Product("laptop", 85_000)

p1.cal_discount(p1.price, 12)

Product.get_count()


