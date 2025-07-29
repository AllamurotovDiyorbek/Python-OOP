class Product:
    def __init__(self,name,price,category,in_stock:bool):
        self.name=name,
        self.price=price,
        self.category=category,
        self.in_stock=in_stock
    def check_stock(self):
        if self.in_stock:
            print(f'{self.name} omborda bor')
        else:
            print(f'{self.name} omborda yoq')
prduc1=Product(name="Iphone14",category='199',price='$900',in_stock=True)
prduc2=Product(name="Iphone4",category='199',price='$900',in_stock=False)
prduc3=Product(name="Iphone1",category='199',price='$900',in_stock=False)
prduc1.check_stock()
prduc2.check_stock()
prduc3.check_stock()