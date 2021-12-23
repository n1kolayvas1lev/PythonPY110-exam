from faker import Faker
import random
import json

from conf import model as MODEL


def book_gen(pk: int = 1) -> dict:
    """Генератор словаря-описания и счётчика.
    Возвращает dict.
    """
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


def title() -> str:
    """Получение названия книги из файла.
    Название избавляется от непечатаемых символов.
    Возвращает str.
    """
    with open('books.txt', 'r', encoding='utf-8',) as books:
        l_books = books.readlines()
        l_books = [l_b.rstrip() for l_b in l_books]
        return random.choice(l_books)


def year() -> int:
    """Генератор года выпуска книги. Возвращает int."""
    return random.randint(900, 2021)


def pages() -> int:
    """Генератор количества страниц. Возвращает int."""
    return random.randint(1, 999999)


def isbn() -> Faker:
    """Генератор ISBN. Возвращает объект Faker."""
    fake = Faker()
    return fake.isbn10()


def rating() -> int:
    """Генератор рейтинга книги. Возвращает int."""
    return random.randint(0, 5)


def price() -> float:
    """Генератор ценника. Возвращает float."""
    return random.uniform(1, 999999)


def author() -> list:
    """Генератор списка авторов:
    i -- случайное значение от 1 до 3, задаёт количество случайных имён;
    fake.name() -- случайное имя
    authors(i, fake name) -> list, список авторов
    """
    i = random.randint(1, 3)
    fake = Faker()
    authors = [fake.name() for _ in range(i)]

    # for _ in range(i):
    #     authors.append(fake.name())
    return authors


def main(output_file: str) -> None:
    """Создание файла списка словарей:
    cnt -- количество книг запрашивается у пользователя;
    book_generator -- итератор возвращающий словарь с содержимым и счётчик;
    list_books -- список книг, записываемый в файл
    """
    cnt = int(input('Сколько нужно книг? '))
    book_generator = book_gen()
    list_books = [next(book_generator) for _ in range(cnt)]
    # for _ in range(100):
    #     list_books.append(next(book_generator))
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
