import mxfbook as mxb
from module.database import db_session, init_db
import module.models as models
import kyobobuilder
import json
import sys

init_db()
# implementation list
# 1. booking , delete ,

# print 'Number of arguments:', len(sys.argv), 'arguments.'
# print 'Argument List:', str(sys.argv)
# Number of arguments: 4 arguments.
# Argument List: ['test.py', 'arg1', 'arg2', 'arg3']

mxb.login('minikie@naver.com', 'testpasword')
# mxb.logout()

trading_book = mxb.get_or_make_book('trading')

# trading_book.name = 'trading'

# book1.set_child(book2)
# book1.save()

builder1 = kyobobuilder.KyoboBuilder()

args = { 'inst_type': 'vanilla_swap',
         'notional': 10000,
         'side': 'pay',
         'fixed_rate': 0.035,
         'maturity_tenor': '5Y' }

inst = kyobobuilder.build_instrument(args)

trading_book.booking(inst)

## book insert


print(trading_book.instruments)

print ()

for m in db_session.query(models.InstrumentMaster).all():
    print('instrument : ' + m.name)

for b in models.MxfBook.select():
    print('book : ' + b.name)

print(json.dumps(inst))




