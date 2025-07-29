class Product:
    def __init__(self,name,price:int,category,in_stock:bool):
        self.name=name
        self.price=price
        self.category=category
        self.in_stock=in_stock
    def show_products(self):
        print(f'Name: {self.name} Narxi: {self.price} categoryasi: {self.category} Mavjudligi: {self.in_stock}')
pq1=Product('Olma',5000,'meva',True)
pq2=Product('Pankeyk',6000,'muzqaymoq',False)
pq1.show_products()
pq2.show_products()
