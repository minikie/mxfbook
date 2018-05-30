from sqlalchemy import Column, Integer, String, Boolean, Text, Float
from module.database import Base, db_session
import datetime
import time
import json


LoginID = 'testid'


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(120), unique=True)


class InstrumentMaster(Base):
    __tablename__ = 'instmaster'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(120), unique=True)
    contents = Column(Text, unique=False)


class IRSPostion(Base):
    __tablename__ = 'irs_position'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(120))
    refdate = Column(String(12))
    bookname = Column(String(120))
    notional = Column(Float)
    indexquote = Column(Float)


class MxfBook(Base):
    __tablename__ = 'fbook'

    id = Column(Integer,  primary_key=True, autoincrement=True)
    name = Column(String(120), unique=True)
    user = Column(String(120), unique=False)
    instruments = Column(Text, unique=False)
    created_date = Column(String(120), unique=False)
    closed_date = Column(String(50), unique=False)
    is_opened = Column(Boolean, unique=False)

    def __init__(self, name=None, user=None, instruments=None, created_date=None):
        self.name = name
        self.user = user
        self.instruments = instruments
        self.created_date = created_date
        self.is_opened = True

    def __repr__(self):
        return '<Name %r>' % (self.name)

    def booking(self, inst):
        inst['booked_time'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        booked_insts = json.loads(self.instruments)

        if inst.name in booked_insts:
            raise Exception('instrument exist. name : ' + inst.name)

        booked_inst = dict()
        booked_inst['open_time'] = inst['booked_time']
        booked_inst['closed_time'] = None
        booked_inst['is_closed'] = False

        # add inst to book
        booked_insts[inst.name] = booked_inst
        self.instruments = json.dumps(booked_insts)

        # self.instruments.append(inst)
        inst_master = InstrumentMaster()
        inst_master.name=inst.name
        inst_master.contents=json.dumps(inst)

        db_session.add(inst_master)
        db_session.commit()





