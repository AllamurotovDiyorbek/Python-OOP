class Book:
    def __init__(self,title,author,is_read):
        self.title=title
        self.author=author
        self.isread=is_read
    def  mark_as_read(self):
        if self.isread!=True:
            self.isread=True
            print("Kitob o‘qilgan deb belgilandi")
    def status(self):
        if self.isread!=True:   
            print("O`qilmagan")
        else:
            print("O`qilgan")
bk1=Book('Temur tuzuklari',"Amir Temur",False)
bk2=Book('Diqqat','Kel Nyuport', False)
bk3=Book("1 Dollarlik Muvafiqiyat","Silvester Stollone",False)
bk4=Book("Mexrobdan Chayon","Abdulla Qodiriy",False)
bk5=Book("Kecha va kunduz","Abdulhamid Cho`lpon",False)
bk1.mark_as_read()
bk5.mark_as_read()
books=[bk1,bk2,bk3,bk4,bk5]
for i in books:
    i.status()
for i in books:
    if i.isread==True:
        print(i.title)
