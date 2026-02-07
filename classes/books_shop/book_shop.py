##############################################################################
from helpers import generate_id
################################################################################
class BookShop:
    ### object constructor
    def __init__(self, name, location):
        ### object properties
        self.id = generate_id(12)
        self.name = name
        self.location = location
        self.books = {}

    ### object string representation
    def __str__(self):
        return f"{self.name} Book Shop is located in {self.location} and owns {len(self)} books"
    def __repr__(self):
        return self.__str__()

    ### object comparison operations
    def __bool__(self):
        return bool(self.books)
    def __eq__(self, other):
        if not isinstance(other, BookShop):
            return False
        return (
            self.books_count == other.books_count and
            self.total_books_pages == other.total_books_pages and
            self.total_books_price == other.total_books_price
        )
    def __ne__(self, other):
        if not isinstance(other, BookShop):
            return True
        return (
            self.books_count != other.books_count or
            self.total_books_pages != other.total_books_pages or
            self.total_books_price != other.total_books_price
        )
    def __contains__(self, book_id):
        return book_id in self.books.keys()

    ### object arithmetic operations
    def __add__(self, other):
        if not isinstance(other, BookShop):
            print("Can only add BookShops")
        newBookShop = BookShop(f"{self.name } & {other.name}", f"{self.location} & {other.location}")
        newBookShop.books = {**self.books, **other.books}
        return newBookShop
    def __sub__(self, other):
        if not isinstance(other, BookShop):
            print("Can only subtract BookShops")
        newBookShop = BookShop(self.name, self.location)
        newBookShop.books = {book_id: book for book_id, book in self.books.items() if book_id not in other.books}
        return newBookShop

    ### object iteration operations [like list]
    def __len__(self):
        return len(self.books.values())
    def __iter__(self):
        return iter(self.books.values())
    def __next__(self):
        return next(self.books.values())
    def __reversed__(self):
        return reversed(self.books.values())

    ### object indexing operations [like dictionary]
    def __getitem__(self, book_id):
        if book_id in self:
            return self.books[book_id]
        print(f"Book with Id ({book_id}) does not exist")
    def __delitem__(self, book_id):
        if book_id in self:
            del self.books[book_id]
        print(f"Book with Id ({book_id}) does not exist")
    def __setitem__(self, book_id, book):
        self.books[book_id] = book

    ### object methods that depend on indexing
    def get_book(self, book_id):
        if book_id in self:
            return self[book_id]
        print(f"Book with Id ({book_id}) does not exist")

    def get_books(self):
        if self:
            return [book for book in self]
        print(f"{self.name} Book Shop has no books")
        return []
    def get_authors(self):
        if self:
            return list(set([author for book in self for author in book.authors]))
        print(f"{self.name} Book Shop has no books")
        return []
    def get_publishers(self):
        if self:
            return list(set([book.publisher for book in self]))
        print(f"{self.name} Book Shop has no books")
        return []

    ### computed properties
    @property
    def books_count(self):
        return len(self)
    @property
    def authors_count(self):
        return len(self.get_authors())
    @property
    def publishers_count(self):
        return len(self.get_publishers())
    @property
    def total_books_price(self):
        if self:
            return sum([book.price for book in self])
        print(f"{self.name} Book Shop has no books")
        return 0
    @property
    def average_books_price(self):
        if self:
            return round(sum([book.price for book in self]) / len(self), 2)
        print(f"{self.name} Book Shop has no books")
        return 0
    @property
    def total_books_pages(self):
        if self:
            return sum([book.pages for book in self])
        print(f"{self.name} Book Shop has no books")
        return 0
    @property
    def average_books_pages(self):
        if self:
            return round(sum([book.pages for book in self]) / len(self), 2)
        print(f"{self.name} Book Shop has no books")
        return 0

    def get_author_books(self, author):
        if self:
            return [book for book in self if author in book.authors]
        print(f"{self.name} Book Shop has no books")
        return []
    def get_publisher_books(self, publisher):
        if self:
            return [book for book in self if book.publisher == publisher]
        print(f"{self.name} Book Shop has no books")
        return []

    def get_books_in_year(self, year):
        if self:
            return [book for book in self if book.published_year == year]
        print(f"{self.name} Book Shop has no books")
        return []
    def get_books_in_period(self, start_year, end_year):
        if self:
            return [book for book in self if start_year <= book.published_year <= end_year]
        print(f"{self.name} Book Shop has no books")
        return []

    def add_book(self, book):
        if book.id not in self:
            self[book.id] = book
        print(f"Book with Id ({book.id}) already exists")

    def remove_book(self, book_id):
        if book_id in self:
            del self[book_id]
        print(f"Book with Id ({book_id}) does not exist")

    def add_books(self, books):
        for book in books:
            self[book.id] = book
        print(f"Added {len(books)} books to {self.name} Book Shop")
        print("-------------------------------")
