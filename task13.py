class Book:
    def __init__(self,title,author,is_read):
        self.title=title
        self.author=author
        self.is_read=is_read
    def mark_as_read():
        if self.is_read==False:
            self.is_read=False
            print("o`qildi deb belgilandi.")
        else:
            print("O`qilgan ekan.")
    def status(self):
        if self.is_read==False:
            print("O`qilmagan")
        else:
            print("O`qilgan")
bk1=Book('Temur tuzuklari',"Amir Temur",False)
bk2=Book('Diqqat','Kel Nyuport', False)
bk3=Book("1 Dollarlik Muvafiqiyat","Silvester Stollone",False)
bk4=Book("Mexrobdan Chayon","Abdulla Qodiriy",False)
bk1.mark_as_read()
bk2.mark_as_read()
bk1.status()
bk2.status()
bk3.status()
bk4.status()