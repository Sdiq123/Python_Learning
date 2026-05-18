class Library:
    def __init__(self):
        self.noBooks = 0
        self.books = []

    def addBook(self, book):
        self.books.append(book)
        self.noBooks = len(self.books)

    def showInfo(self):
        print(f"The Library has {self.noBooks} books are ")
        for book in self.books:
            print(book)

l1 = Library()
l1.addBook("Harry Potter 1")
l1.addBook("Harry Potter 2")
l1.addBook("Harry Potter 3")
l1.showInfo()