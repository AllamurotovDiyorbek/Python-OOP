class Product:
      def __init__(self,name,price,in_stock):
            self.name=name
            self.price=price
            self.in_stock=in_stock
      def show_info(self):
            print(self.name,self.price,self.in_stock)
pr1=Product("olma",5_00,False)
pr2=Product("Behi",2_00,True)
pr3=Product("Non",1_00,True)
pr4=Product("Tarvuz",7_00,True)
pr5=Product("Shaftoli",3_00,False)
sts=[pr1,pr2,pr3,pr4,pr5]
c=0
for i in sts:
      if i.in_stock==True:
            c+=i.price
print(f'Ombordagi mahsulotlar narxi: {c} so`m')