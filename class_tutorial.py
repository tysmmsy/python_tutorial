class Product:
    def __init__(self, id, name, quantity, price):
        self.id = id
        self.name = name
        self.quantity = quantity
        self.price = price
        self.worth = price * quantity

    def show(self):
        print(
            f"ID:{id}\t 商品:{self.name}\t 個数:{self.quantity}\t 価格:{self.price}\t 総額(価格*個数):{self.worth}\t"
        )


class Stock:
    def __init__(self):
        self.items_list = []

    def add(self, product):
        flag = False
        for i in self.items_list:
            if i.name == product.name:
                i.quantity += product.quantity
                i.worth += product.worth
                flag = True
                break
        if flag == False:
            self.items_list.append(product)
        print(f"{product.name}{product.quantity}個追加しました")

    def delete(self, product):
        flag = False
        for i in self.items_list:
            if i.name == product.name:
                flag = True
                if i.quantity >= product.quantity:
                    i.quantity -= product.quantity
                    i.worth -= product.worth
                    print(f"{product.name}{product.quantity}個減少しました")
                    break
                else:
                    print("個数が足りません")
        if flag == False:
            print(f"{product.name}が存在しません")

    def print_info(self, *target):
        print("-" * 90)
        if len(target) > 0:
            for i in target:
                flag = False
                for j in self.items_list:
                    if i == j.name:
                        flag = True
                        j.show()
                if flag == False:
                    print(f"{item.name}は存在ません")
        else:
            for i in self.items_list:
                i.show()
            total_product = len(self.items_list)
            total_worth = 0
            for item in self.items_list:
                total_worth += item.worth
            print(f"商品種類数: {total_product}\n 在庫合計数:{total_worth}")
            print("-" * 90)

    def sort_stock(self, k="quantity", r=False):
        if k == "quantity":
            sorted_stock = sorted(
                self.items_list, key=lambda x: x.quantity, reverse=r
            )
        elif k == "worth":
            sorted_stock = sorted(
                self.items_list, key=lambda x: x.worth, reverse=r
            )
        for i in sorted_stock:
            i.show()
        print("-" * 90)


# check 1
s = Stock()
s.add(Product(1001, "apple", 20, 200))
s.add(Product(1002, "pear", 5, 300))
s.delete(Product(1001, "apple", 10, 200))
s.add(Product(1003, "orange", 30, 100))
s.add(Product(1004, "banana", 25, 50))
s.delete(Product(1001, "orange", 10, 200))
s.add(Product(1005, "milk", 35, 100))
s.add(Product(1006, "ice", 50, 200))

# check 2
s.print_info()

# check 3
s.sort_stock("quantity", False)

# check 4
s.sort_stock("worth", True)
