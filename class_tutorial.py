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
        print(f"{name}{quantity}個追加しました")

    def delete(self, product):
        flag = False
        for i in self.items_list:
            if i.name == product.name:
                flag = True
                if i.quantity >= product.quantity:
                    i.quantity -= product.quantity
                    i.worth -= product.worth
                    print(f"{name}{quantity}個減少しました")
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
                    print(f"{name}は存在ません")
        else:
            for i in self.items_list:
                i.show()
            total_product = len(self.items_list)
            total_worth = 0
            for item in self.items_list:
                total_worth += item.worth
            print(f"商品種類数: {product}\n 在庫合計数:{worth}")
            print("-" * 90)
