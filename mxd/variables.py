import numpy as np
import json
import database as db
from io import StringIO
from collections import namedtuple


def _json_object_hook(d): return namedtuple('X', d.keys())(*d.values())
def json2obj(data): return json.loads(data, object_hook=_json_object_hook)


class Workspace:
    def __init__(self, ws_name):
        self.meta_ = json2obj(db.load_workspace_meta_json(ws_name))

    def name(self):
        return self.meta_.name


class Variable:
    def __init__(self, ws_name, var_name):
        self.meta_ = json2obj(db.load_variable_meta_json(ws_name, var_name))

    def type(self):
        return self.meta_.type

    # lazy load : double or string or npz binary
    # data = np.genfromtxt(s, dtype=[('myint','i8'),('myfloat','f8'),
    # ... ('mystring','S5')], delimiter=",")
    def value(self):
        res = db.load_variable_value(self.meta_.name, self.meta_.name)

        if self.meta_.var_type == 'default':
            return np.genfromtxt(StringIO(res),delimiter=",")
        elif self.meta_.var_type == 'double':
            return np.genfromtxt(StringIO(res),delimiter=",")
        else:
            return 'load fail'


class DefaultVariable(Variable):
    def __init__(self):
        Variable.__init__(self)

    def value(self):
        pass