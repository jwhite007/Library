#! /usr/bin/env python

from string import ascii_uppercase


class Library(object):
    """docstring for Library"""
    def __init__(self):
        self.shelves = []

    def add(self, shelf):
        if shelf not in self.shelves:
            self.shelves.append(shelf)

    def show(self):
        print "Shelf:".ljust(20), "Title:".ljust(20), "Author:".ljust(20)
        for i in self.shelves:
            y = i[6]
            for x in eval("shelf{0}.books".format(y)):
                print i.ljust(20), x[0].ljust(20), x[1].ljust(20)


class Shelf(object):
    """docstring for Shelf"""
    def __init__(self):
        self.books = []

    def add(self, book):
        self.books.append(book)

    def rem(self, title):
        for i in self.books:
            if title not in i:
                pass
            else:
                self.books.pop(self.books.index(i))
                break
        else:
            print "Can't checkout {0}{1}{2}{0} Book is not in Library".format('"', title, '.')

    def show(self):
        print "".ljust(20), "Title:".ljust(20), "Author:".ljust(20)
        for i in sorted(self.books[:]):
            print "".ljust(20), i[0].ljust(20), i[1].ljust(20)


class Book(object):
    """docstring for book"""
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.title_author = (self.title, self.author)

    def enshelf(self):
        x = self.author[0]
        eval("shelf{0}.add(self.title_author)".format(x))

    def unshelf(self):
        x = self.author[0]
        eval("shelf{0}.rem(self.title)".format(x))

    def show(self):
        print "".ljust(20), "Title:".ljust(20), "Author:".ljust(20)
        print "".ljust(20), self.title.ljust(20), self.author.ljust(20)

Library1 = Library()
alpha = list(ascii_uppercase)
for i in alpha:
    exec("shelf{0} = Shelf()".format(i))
    x = "shelf {0}".format(i)
    Library1.add(x)

A = Book("Dune", "Herbert, Frank")
B = Book("Iberia", "Michener, James A")
C = Book("Jitterbug Perfume", "Robbins, Tom")
D = Book("Iberia", "Michener, James A")
E = Book("Alaska", "Michener, James A")
F = Book("Jitterbug Perfume", "Robbins, Tom")
G = Book("Centennial", "Michener, James A")

A.enshelf()
B.enshelf()
C.enshelf()
D.enshelf()
E.enshelf()
F.enshelf()

library1 = Library()
print
print "\033[4mShowing Library Status\033[0m" "\n"
Library1.show()
print "\n" * 2
print "\033[4mChecking {0}{1}{0} out of the Library\033[0m".format('"', A.title), "\n" * 3
A.unshelf()
print "\033[4mShowing Library Status after Checkout of {0}{1}{0}\033[0m".format('"', A.title), "\n"
Library1.show()
print "\n" * 2
print "\033[4mChecking {0}{1}{0} out of the Library\033[0m".format('"', G.title), "\n"
G.unshelf()
print "\n" * 2
print "\033[4mShowing Shelf M\033[0m" "\n"
shelfM.show()
print "\n" * 2
print "\033[4mShowing Book A\033[0m" "\n"
A.show()
