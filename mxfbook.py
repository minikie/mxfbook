import instrument as inst
import module.models as models
from module.database import db_session
import datetime
import json

def login(id,pw):
    # check user
    models.LoginID = id

    print ('login success')


def logout():
    models.LoginID = None


def get_or_make_book(name):
    book  = db_session.query(models.MxfBook).filter_by(name=name).first()
    if book is None:
        return make_book(name)
    else:
        return book


def make_book(name):
    if models.LoginID is None:
        raise Exception('Login is needed')

    instruments = '''{  }'''

    book  = models.MxfBook(name=name, user=models.LoginID, created_date=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),instruments=instruments)
    db_session.add(book)
    db_session.commit()

    return book


def get_book(name):
    book = models.MxfBook.get(name=name, user=models.LoginID)
    return book

