class Student:
    def __init__(self,name,age,grade):
        self.name=name
        self.age=age
        self.grade=grade
    def display_info(self):
        print(f'Student: {self.name} Age: {self.age} Grade: {self.grade}')
st1=Student("Diyorbek","17","11-sinf")
st2=Student("Ali","12","5-sinf")
st3=Student("Suxrob","15","9-sinf")
print("Studnets info")
st1.display_info()
st2.display_info()
st3.display_info()