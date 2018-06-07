import sys
import os
from mxfbook.module.database import init_db, db_session
import mxfbook.module.models as models
import mxfbook.module.message as message
import datetime
import json

init_db()

# def login(id,pw):
#     # check user
#     models.LoginID = id
#
#     print ('login success')


def logout():
    models.LoginID = None


def get_book(name):
    book = db_session.query(models.MxfBook).filter_by(name=name).first()

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
    book = get_book(name)
    if book is None:
        return make_book(name)
    else:
        return book


def makebook(name):
    book = get_book(name)
    if book is None:
        return make_book(name).to_json()
    else:
        return 'book : ' + name + ' exist'


def removebook(book_nm):
    book = db_session.query(models.MxfBook).filter_by(name=book_nm).first()
    if book is None:
        return message.noExistBook(book_nm)

    db_session.delete(book)
    db_session.commit()
    return 'book : ' + book_nm + ' is removed'


def bookinfo(book_nm):
    book = get_book(book_nm)
    if book is None:
        return message.noExistBook(book_nm)
    return book.to_json()


def booklist():
    books = db_session.query(models.MxfBook).all()

    b = []
    for book in books:
        #b.append(json.dumps(book.to_json()))
        b.append(book.to_json())

    return b


def instinfo(inst_nm):
    inst = db_session.query(models.InstrumentMaster).filter_by(name=inst_nm).first()

    return inst.contents


def bookinginst(inst_nm, book_nm, contents):
    book = get_book(book_nm)
    if book is None:
        return message.noExistBook(book_nm)

    inst = models.InstrumentMaster(name=inst_nm, contents=contents)

    if inst is not None:
        return message.noInstrumentExistInBook(inst_nm, book_nm)

    db_session.add(inst)
    db_session.commit()


def removeinst(inst_nm):
    inst = db_session.query(models.InstrumentMaster).filter_by(name=inst_nm).first()
    if inst is None:
        return message.noExistInst(inst_nm)

    db_session.delete(inst)
    db_session.commit()
    return 'inst : ' + inst_nm + ' is removed'


def moveinst(inst_nm, origin_book_nm, target_book_nm):
    origin_book = db_session.query(models.InstrumentMaster).filter_by(name=origin_book_nm).first()
    if origin_book is None:
        return message.noExistBook(origin_book)

    origin_instruments = json.loads(origin_book.instruments)

    if origin_instruments.has_key(inst_nm):
        inst = origin_instruments.pop(inst_nm)

        target_book = db_session.query(models.InstrumentMaster).filter_by(name=target_book_nm).first()
        if target_book is None:
            return message.noExistBook(target_book)

        target_instruments = json.loads(target_book.instruments)

        if target_instruments.has_key(inst_nm):
            return message.instrumentExistInBook(inst_nm, target_book_nm)

        target_instruments[inst_nm] = inst

        target_book.instruments = target_instruments
        db_session.commit()
    else:
        return message.noInstrumentExistInBook(inst_nm, origin_book_nm)



def login(args):
    return  'login is called'


def main(func_nm, args):
    #exit(_main(func_nm, args))
    print (_main(func_nm, args))


def _main(func_nm, args):
    if func_nm == 'bookinfo':
        return bookinfo(args)
    elif func_nm == 'booklist':
        return booklist(args)
    elif func_nm == 'instinfo':
        return instinfo(args)
    elif func_nm == 'login':
        return login(args)
    else:
        return 'invalid call : ' + func_nm


if __name__ == '__main__':
    sys.stdout = open(os.devnull, "w")

    if len(sys.argv) < 2:
        exit('argument empty')

    func_nm = sys.argv[1]

    main(func_nm, sys.argv[1:])