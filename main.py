from faker import Faker
import random
import json

from conf import model as MODEL


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


def title():
    with open('books.txt', 'r', encoding='utf-8',) as books:
        l_books = books.readlines()
        l_books = [l_b.rstrip() for l_b in l_books]
        return random.choice(l_books)


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
        authors.append(fake.name())
    return authors


def main(out_file: str):
    book_generator = book_gen()
    list_books = []
    for _ in range(100):
        list_books.append(next(book_generator))
    with open(out_file, 'w') as outp:
        json.dump(list_books, outp, indent=4, ensure_ascii=False)
#    return list_books


if __name__ == "__main__":
    out_file = "Book_list.json"
    main(out_file)
    with open("Book_list.json") as bl:
        for line in bl:
            print(line, end='')
#    print(json.dumps(main(), indent=4, ensure_ascii=False))

