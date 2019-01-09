import sqlite3
import win32com.client
import winpaths
import json
import os

conn = None
applicationName = 'test'
settings = None


def initialize(appname):
    global settings
    with open(os.path.join(winpaths.get_appdata(), 'Montrix', 'MxExcelAddIn', 'settings', 'settings.json')) as f:
        settings = json.load(f)

    db_filie = os.path.join(settings['GeneralOptionCategory_']['RepositoryDirectory_'], appname, 'BlobCache', 'userblobs.db')
    print db_filie

    global conn
    conn = sqlite3.connect(db_filie)


def load_workspace_meta_json(ws_name):
    #res  = b'{"name": "John Smith", "hometown": {"name": "New York", "id": 123}}'

    sql = "SELECT Key, TypeName, Value FROM CacheElement WHERE TypeName='MxExcelAddInUI.WorkspaceKeyManager+WorkSapce' and KEY=:key"
    param = { 'key':  ws_name }
    cursor = conn.cursor()
    cursor.execute(sql, param)
    name, ws_meta = cursor.fetchone()

    return ws_meta.encode("utf-8")


def load_variable_meta_json(ws_name, var_name):
    sql = "SELECT Key, TypeName, Value FROM CacheElement WHERE TypeName='metadata' and KEY=:key"
    param = {'key':  ws_name + '.' + var_name}
    cursor = conn.cursor()
    cursor.execute(sql, param)
    key, type_name, value = cursor.fetchone()
    print value
    return value.encode("utf-8")


# http://www.numericalexpert.com/blog/sqlite_blob_time/
def load_variable_value(ws_name, var_name):
    sql = "SELECT Key, TypeName, Value FROM CacheElement WHERE TypeName='valuedata' and KEY=:key"
    param = { 'key':  ws_name + "#" + var_name }
    cursor = conn.cursor()
    cursor.execute(sql, param)
    name, data = cursor.fetchone()

    return data.encode("utf-8")


initialize('mytest')
load_variable_meta_json('ws', 'newVar')