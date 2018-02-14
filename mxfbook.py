import instrument as inst
import models
import datetime
import json

def login(id,pw):
    # check user
    models.LoginID = id

    print 'login success'


def logout():
    models.LoginID = None


def is_exist(name):
    try:
        book = models.MxfBook.get(name=name)
        return True
    except models.DoesNotExist:
        return False


def get_or_make_book(name):
    try:
        return models.MxfBook.get(name=name)
    except models.DoesNotExist:
        return make_book(name)


def make_book(name):
    if models.LoginID is None:
        raise Exception('Login is needed')

    book = models.MxfBook.create(name=name,
                                 user=models.LoginID,
                                 created_date=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                                 instruments='''{  }''')
    return book


def get_book(name):
    book = models.MxfBook.get(name=name, user=models.LoginID)
    return book

