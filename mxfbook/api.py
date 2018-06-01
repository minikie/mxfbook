import sys
import os
from module.database import init_db, db_session
import module.models as models
import datetime

init_db()

# def login(id,pw):
#     # check user
#     models.LoginID = id
#
#     print ('login success')


def logout():
    models.LoginID = None


def get_book(name):
    book = models.MxfBook.get(name=name, user=models.LoginID)
    return book


def make_book(name):
    # if models.LoginID is None:
    #     raise Exception('Login is needed')

    instruments = '''{  }'''

    book  = models.MxfBook(name=name, user=models.LoginID, created_date=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), instruments=instruments)
    db_session.add(book)
    db_session.commit()

    return book


def get_or_make_book(name):
    book  = db_session.query(models.MxfBook).filter_by(name=name).first()
    if book is None:
        return make_book(name)
    else:
        return book


def bookinfo(args):
    if len(args) == 0:
        exit()

    book_nm = args[0]
    book = get_or_make_book(book_nm)
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