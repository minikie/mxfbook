import database as db
from variables import *


def get_variable(ws_name, var_name):
    v = db.load_variable_meta_json(ws_name, var_name)
    #print v[2]
    meta = json2obj(str(v[2]))
    return Variable(ws_name, var_name, meta)


def get_all_variables(**args):
    ws_name = args['workspace']
    #print ws_name
    v_data = db.load_variables_in_workspace(ws_name)

    return [Variable(v[0], v[1], json2obj(str(v[2]))) for v in v_data]



# # usage
# ws_name1 = 'ws'
# var_name1 = get_variable('ws1', 'var_name1')

