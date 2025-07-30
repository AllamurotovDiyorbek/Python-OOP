class Product:
      def __init__(self,name,price,category):
            self.name=name
            self.price=price
            self.category=category
      def info(self):
            print(f'{self.name} {self.price}')
pr1=Product("olma",10_000,'meva')
pr2=Product("behi",14_000,'meva')
pr3=Product("Snikers",8_000,'shoklad')
pr4=Product("Fanta",15_000,'ichimlik')
pr5=Product("Dinay",10_000,'ichimlik')
pr6=Product("Twiks",14_000,'shokolad')
products=[pr1,pr2,pr3,pr4,pr5,pr6]
c=0
for i in products:
      if i.price>c:
            c=i.price
            d=i
d.info()