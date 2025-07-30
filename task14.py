class Student:
      def __init__(self,name,age):
            self.name=name
            self.age=age
      def show_info(self):
            print(f"{self.name}, {self.age}")
st1=Student("Diyor",17)
st2=Student("Sardor",12)
st3=Student("Jamshid",13)
st4=Student("Ilhom",17)
st5=Student("Mahmud",18)
sts=[st1,st2,st3,st4,st5]
mx=0
for i in sts:
      if i.age>mx:
            mx=i.age
print(mx)