class User:
    def __init__(self,username,email,is_active):
        self.username=username
        self.email=email
        self.is_active=is_active
    def info(self):
        print(f'{self.username} {self.email} {self.is_active}')
    def activate(self):
        if self.is_active!=True:
            self.is_active=True
            print(f'Foydalanuvchi faolashtirildi')
        else:
            print("Foydaluvchi bloklanmagan")
    def deactivate(self):
        if self.is_active==True:
            self.is_active=False
            print(f'Foydalanuvchi bloklandi')
        else:
            print("foydalunvchi foalemas")
user1 = User("ali98", "ali98@example.com", False)
user2 = User("nargiza23", "nargiza23@mail.uz", True)
user3 = User("sardor_bek", "sardor.dev@company.uz", False)
user4 = User("dilshod_ai", "dilshod.ai@gmail.com", True)
user5 = User("lola_flower", "lola1995@yahoo.com", False)
user6 = User("javohir_dev", "javohir.coder@uz", True)
user7 = User("shaxnoza", "shaxnoza.teacher@school.uz", True)
user8 = User("bekzod", "bekzod2023@mail.ru", False)
user9 = User("malika_art", "malika.artist@creative.uz", True)
user10 = User("botir", "botir.manager@work.uz", True)
user1.info()
user1.deactivate()
user1.info()