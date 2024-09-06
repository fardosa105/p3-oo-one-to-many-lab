class Author:
    pass
    authors = []

    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str):
            self._name = name
        else:
            raise Exception("name is invalid")

    def contracts(self):
        pass

    def books(self):
        pass

    def sign_contract(book, date, royalties):
        pass

    def total_royalties(self):
        pass


class Book:
    pass
    books = []

    def __init__(self, title):
        self.title = title

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        if isinstance(title, str):
            self._title = title
        else:
            raise Exception("title is invalid")


class Contract:
    pass
    contracts = []

    def __init__(self, author, book, date, royalties):
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties

    @classmethod
    def contracts_by_date(cls, date):
        pass

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, author):
        if isinstance(author, (Author)):
            self._author = author
        else:
            raise Exception("author is invalid")

    @property
    def book(self):
        return self._book

    @book.setter
    def book(self, book):
        if isinstance(book, (Book)):
            self._book = book
        else:
            raise Exception("book is invalid")

    @property
    def date(self):
        return self.date

    @date.setter
    def date(self, date):
        if isinstance(date, str):
            self.date = date
        else:
            raise Exception("date is invalid")

    @property
    def royalties(self):
        return self.royalties

    @royalties.setter
    def royalties(self, royalties):
        if isinstance(royalties, int):
            self.royalties = royalties
        else:
            raise Exception("royalties is invalid")