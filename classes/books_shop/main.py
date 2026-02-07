# build a simple book shop app using oop as:
# ------------------------------------------
# create a book class with title, subtitle, publisher, published_year, authors, pages and price
# create a book shop class with name, location and a list of books
# create a book shop manager class with a list of book shops
# create a function to add a book to a book shop
# create a function to add multiple books to a book shop
# create a function to remove a book from a book shop
# create a function to print all books info in a book shop
# create a function to calculate the total price of all books in a book shop
# create a function to calculate the average price of all books in a book shop
# create a function to calculate the total number of pages in a book shop
# create a function to calculate the average number of pages in a book shop
# create a function to calculate the total number of books in a book shop
# create a function to calculate the total number of authors in a book shop
# create a function to calculate the total number of publishers in a book shop
# create a function to calculate the total number of book shops
# create a function to print a book shop info as name, location, number of books, total price, average price, total pages, average pages, total authors, total publishers
#######################################################################################
from random import randint
import json

from book import Book
from book_shop import BookShop
#######################################################################################
# read books data from json file and create a list of books
#######################################################################################
with open('books.json', 'r') as books_file:
    books_data = json.load(books_file)
books = []
for item in books_data:
    if item['language'] == "en":
        the_book = Book(
            item['title'],
            item['title']*2  if 'subtitle' not in item else item['subtitle'],
            [] if 'authors' not in item else item['authors'],
            "Unknown Publisher" if 'publisher' not in item else item['publisher'],
            randint(1950, 2020) if 'publishedDate' not in item else int(item['publishedDate'][:4]),
            randint(100, 1500) if 'pageCount' not in item else int(item['pageCount']),
            randint(10, 250)
        )
        books.append(the_book)
#######################################################################################
print("###############################")
print("Book Shop Manager")
print("###############################")
#######################################################################################
# create 3 BookShops and add random books to each one
######################################################################################
strand = BookShop("The Strand Bookstore", "New York City, USA")
strand.add_books(books=books[0:randint(75, 150)])

city_lights = BookShop("City Lights Bookstore", "San Francisco, CA - USA")
city_lights.add_books(books=books[150:randint(200, 300)])

elliott = BookShop("Elliott Bay Book Company", "Seattle, WA, USA")
elliott.add_books(books=books[300:randint(400, 440)])
print("-------------------------------")
#######################################################################################
# print some info about The Strand Bookstore
#######################################################################################
print("The Strand Bookstore")
print("-------------------------------")
print(f"Total number of books: {len(strand)}")
print(f"Total price of books: ${strand.total_books_price:.2f}")
print(f"Average price of books: ${strand.average_books_price:.2f}")
print(f"Total number of pages: {strand.total_books_pages}")
print(f"Average number of pages: {strand.average_books_pages}")
print(f"Total number of authors: {strand.authors_count}")
print(f"Total number of publishers: {strand.publishers_count}")
print("-------------------------------")
#######################################################################################
# print some info about City Lights Bookstore
#######################################################################################
print("City Lights Bookstore")
print("-------------------------------")
print(f"Total number of books: {len(city_lights)}")
print(f"Total price of books: ${city_lights.total_books_price:.2f}")
print(f"Average price of books: ${city_lights.average_books_price:.2f}")
print(f"Total number of pages: {city_lights.total_books_pages}")
print(f"Average number of pages: {city_lights.average_books_pages}")
print(f"Total number of authors: {city_lights.authors_count}")
print(f"Total number of publishers: {city_lights.publishers_count}")
print("-------------------------------")
#######################################################################################
# print some info about Elliott Bay Book Company
#######################################################################################
print("Elliott Bay Book Company")
print("-------------------------------")
print(f"Total number of books: {len(elliott)}")
print(f"Total price of books: ${elliott.total_books_price:.2f}")
print(f"Average price of books: ${elliott.average_books_price:.2f}")
print(f"Total number of pages: {elliott.total_books_pages}")
print(f"Average number of pages: {elliott.average_books_pages}")
print(f"Total number of authors: {elliott.authors_count}")
print(f"Total number of publishers: {elliott.publishers_count}")
print("-------------------------------")
#######################################################################################
# print some info about The 3 Book Shop Group
#######################################################################################
book_shop_group = strand + city_lights + elliott
print("The 3 Book Shop Group")
print("-------------------------------")
print(f"Total number of books: {len(book_shop_group)}")
print(f"Total price of books: ${book_shop_group.total_books_price:.2f}")
print(f"Average price of books: ${book_shop_group.average_books_price:.2f}")
print(f"Total number of pages: {book_shop_group.total_books_pages}")
print(f"Average number of pages: {book_shop_group.average_books_pages}")
print("-------------------------------")
#######################################################################################
# print some info about Packt Publishing Ltd
#######################################################################################
strand_packt_books = strand.get_publisher_books("Packt Publishing Ltd")
city_lights_packt_books = city_lights.get_publisher_books("Packt Publishing Ltd")
elliott_packt_books = elliott.get_publisher_books("Packt Publishing Ltd")
packt_books = strand_packt_books + city_lights_packt_books + elliott_packt_books
print(f"{len(packt_books)} Books by Publisher: Packt Publishing Ltd")
print("-------------------------------")
print(f"{len(strand_packt_books)} in The Strand Bookstore")
print(f"{len(city_lights_packt_books)} in City Lights Bookstore")
print(f"{len(elliott_packt_books)} in Elliott Bay Book Company")
print("-------------------------------")
print("\n".join([book.title for book in packt_books]))
print("-------------------------------")
#######################################################################################
