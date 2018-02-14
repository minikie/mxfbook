import mxfbook as mxb
import kyobobuilder
import json
import models


# implementation list
# 1. booking , delete ,

mxb.login('minikie@naver.com', 'testpasword')
# mxb.logout()

# book1 = mxb.make_book()
# book2 = mxb.make_book()

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


print trading_book.instruments

for m in models.InstrumentMaster.select():
    print 'instrument : ' + m.name

for b in models.MxfBook.select():
    print 'book : ' + b.name

print json.dumps(inst)




