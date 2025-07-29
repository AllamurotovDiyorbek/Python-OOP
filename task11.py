class Blok:
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
bq1=Blok('Temur tuzuklari',"Amir Temur",False)
bq2=Blok('Diqqat','Kel Nyuport', True)
bq1.mark_as_read()
