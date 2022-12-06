class Product:
    def __init__(self, id, name, quantity, price):
        self.id = id
        self.name = name
        self.quantity = quantity
        self.price = price
        self.worth = price * quantity

    def show(self):
        print(
            f"ID:{id}\t 商品:{name}\t 個数:{quantity}\t 価格:{price}\t 総額(価格*個数):{worth}\t"
        )
