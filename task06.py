class Student:
    def __init__(self,name,age,grade):
        self.name=name
        self.age=age
        self.grade=grade
    def info(self):
        print(f'{self.name}, {self.age} yosh, {self.grade}-sinf')
st1=Student('Ali',17,11)
st2=Student('Ziyod',11,4)
st3=Student('Vali',12,5)
st4=Student('Xurshid',13,6)
st5=Student('Sami',14,7)
sts=[st1,st2,st3,st4,st5]
for i in sts:
    i.info()
