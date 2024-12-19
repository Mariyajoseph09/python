class Publisher:
    def __init__(self, name):
        self.name = name

    def display_publisher(self):
        print(f"Publisher: {self.name}")


class Book(Publisher):
    def __init__(self, name, title, author):

        super().__init__(name)
        self.title = title
        self.author = author

    def display_book_info(self):

        print(f"Title: {self.title}")
        print(f"Author: {self.author}")


class Python(Book):
    def __init__(self, name, title, author, price, no_of_pages):

        super().__init__(name, title, author)
        self.price = price
        self.no_of_pages = no_of_pages


    def display_python_book_info(self):

        self.display_publisher()
        self.display_book_info()
        print(f"Price: {self.price}")
        print(f"Number of Pages: {self.no_of_pages}")


python_book = Python("MARK VILLAMS", "JUNGLE BOOK", "WILLAM DHAS", 3900, 1100)


python_book.display_python_book_info()