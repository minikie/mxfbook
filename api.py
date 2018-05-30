import sys
import os
import mxfbook as mxb
from module.database import db_session, init_db
import json

init_db()


def bookinfo(args):
    if len(args) == 0:
        exit()

    book_nm = args[0]
    book = mxb.get_or_make_book(book_nm)
    print('bookinfo is called : ' + book_nm)


def booklist(args):
    print('booklist is called')


def instinfo(args):
    print('instinfo is called')


def login(args):
    print('login is called')


def main(func_nm, args):
    if func_nm == 'bookinfo':
        bookinfo(args)
    elif func_nm == 'booklist':
        booklist(args)
    elif func_nm == 'instinfo':
        instinfo(args)
    elif func_nm == 'login':
        login(args)
    else:
        print('invalid call : ' + func_nm)


if __name__ == '__main__':
    sys.stdout = open(os.devnull, "w")

    if len(sys.argv) < 2:
        exit('argument empty')

    func_nm = sys.argv[1]

    main(func_nm, sys.argv[1:])