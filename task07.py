class Movie:
    def __init__(self,title,genre,duration:int,rating:float):
        self.title=title
        self.genre=genre
        self.duration=duration
        self.rating=rating
    def show_task(self):
        print(f'"{self.title} -- {self.genre} janridagi film   Reytingi: {self.rating}/{self.duration}."')
film1 = Movie("Shaytanat", "Qo'rqinchli", 138, 8.7)
film2 = Movie("Dovdirash", "Drama", 125, 9.1)
film3 = Movie("Qasoskorlar: Intiho", "Fantastik", 181, 8.4)
film4 = Movie("O'rgimchak-odam: Uyga yo'l yo'q", "Fantastik", 148, 8.6)
film5 = Movie("Forrest Gump", "Drama", 142, 8.8)
film6 = Movie("Leon", "Jangari", 133, 8.5)
film7 = Movie("Insepsion", "Fantastik", 148, 8.8)
film8 = Movie("Qora shahzoda", "Jangari", 132, 7.9)
film9 = Movie("Titanik", "Romantika", 195, 7.8)
film10 = Movie("Qochoq", "Triller", 130, 8.1)
kino=[film1,film2,film3,film4,film5,film6,film7,film8,film9,film10]
for i in kino:
    i.show_task()