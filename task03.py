class User:
    def __init__(self,name:str,email:str,is_active:bool):
        self.name=name
        self.email=email
        self.is_active=is_active
    def info(self):
        if self.is_active:
            print(f'User: {self.name} email: {self.email} is_active: muvjudmas')
        else:
            print(f'User: {self.name} email: {self.email} is_active: mavjud')
use1=User("Sanjar","sanjar@gmail.com",True)
use2=User("Oybek","oybekw@gmail.com",False)
use3=User("Isroil","isroil@gmail.com",False)
use4=User("Mavlud","mavlud@gmail.com",True)
use1.info()
use2.info()
use3.info()
use4.info()