# import datetime
# import time
# import json
#
# db = SqliteExtDatabase('c:\my_database.db')
# LoginID = None
#
# class BaseModel(Model):
#     class Meta:
#         database = db
#
#
# class InstrumentMaster(BaseModel):
#     name = CharField()
#     contents = TextField()
#
#
# class MxfBook(BaseModel):
#
#     name = CharField()
#     user = CharField()
#     instruments = TextField()
#     created_date = CharField()
#     closed_date = CharField(null=True)
#     is_opened = BooleanField(default=True, null=True)
#
#     def commit(self):
#         pass
#
#     def booking(self, inst):
#         inst['booked_time'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#
#         booked_insts = json.loads(self.instruments)
#
#         if inst.name in booked_insts:
#             raise Exception('instrument exist. name : ' + inst.name)
#
#         booked_inst = dict()
#         booked_inst['open_time'] = inst['booked_time']
#         booked_inst['closed_time'] = None
#         booked_inst['is_closed'] = False
#
#         # add inst to book
#         booked_insts[inst.name] = booked_inst
#         self.instruments = json.dumps(booked_insts)
#         self.save()
#
#         # self.instruments.append(inst)
#         inst_master = InstrumentMaster()
#         inst_master.name=inst.name
#         inst_master.contents=json.dumps(inst)
#         inst_master.save()
#
#
# class User(BaseModel):
#     username = CharField(unique=True)
#
#
# db.connect()
# # db.drop_tables([InstrumentMaster, MxfBook, User])
# # db.create_tables([InstrumentMaster, MxfBook, User])
