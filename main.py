from faker import Faker
import random
import json

from conf import model as MODEL


# def pk(start=1): #рабочий
#     pk_gen = (i for i in range(1, 100))
#     return next(pk_gen)
def book_gen(pk=1):
    while True:
        yield {
            "model": MODEL,
            "pk": pk,
            "fields": {
                "title": title(),
                "year": year(),
                "pages": pages(),
                "isbn13": isbn(),
                "rating": rating(),
                "price": price(),
                "author": author()
            }
        }
        pk += 1
    return


def title():
    n = random.randint(1,5)
#    with open('books.txt', 'r', encoding='utf-8') as books:
#    books.readline(n)
    return n


def year():
    return random.randint(900, 2021)


def pages():
    return random.randint(1, 999999)


def isbn():
    fake = Faker()
    return fake.isbn10()


def rating():
    return random.randint(0, 5)


def price():
    return random.uniform(1, 999999)


def author():
    i = random.randint(1, 3)
    authors = []
    fake = Faker()
    for _ in range(i):
        authors.append( fake.name())
    return authors


# def main(): #рабочий
#
#     return {
#         "model": MODEL,
#         "pk": pk(),
#         "fields": {
#             "title": title(),
#             "year": year(),
#             "pages": pages(),
#             "isbn13": isbn(),
#             "rating": rating(),
#             "price": price(),
#             "author": author()
#
#         }
#     }


def main():
    book_generator = book_gen()
    list_books = []
    for _ in range(100):
        list_books.append(next(book_generator))
    return list_books


if __name__ == "__main__":
    print(json.dumps(main(), indent=4)) #рабочий
#    print(main())
