#######################################################################################
from datetime import date
from helpers import generate_id
#######################################################################################
class Book:
    def __init__(self, title, subtitle, authors, publisher, published_year, pages, price):
        self.id = generate_id(12)
        self.title = title
        self.subtitle = subtitle
        self.authors = authors
        self.publisher = publisher
        self.published_year = published_year
        self.age = date.today().year - self.published_year
        self.pages = pages
        self.price = price

    def __str__(self):
        return f"""Book_#{self.id}_Details:
    ------------------------------------
    Title: {self.title}
    Subtitle: {self.subtitle}
    Authors: {', '.join(self.authors)}
    Publisher: {self.publisher}
    Published Year: {self.published_year}
    Pages: {self.pages}
    Price: {self.price}
    ------------------------------------
    """

    def __repr__(self):
        return f"{self.title}, {self.subtitle}, is authored by {', '.join(self.authors)} and published by {self.publisher} in {self.published_year} and contains {self.pages} pages and costs {self.price}"
