import sqlite3
import win32com.client
import winpaths
import json
import os

conn = None
applicationName = 'test'
settings = None


def initialize(appname):
    settings = json.load(os.path.join(winpaths.get_appdata(), 'Montrix', 'MxExcelAddIn'))

    db_filie = os.path.join(settings['repository'], 'BlobCache',appname,'userblobs.db')
    conn = sqlite3.connect(db_filie)


def load_workspace_meta_json(ws_name):
    #res  = b'{"name": "John Smith", "hometown": {"name": "New York", "id": 123}}'

    sql = "SELECT NAME, DATA FROM TABLE1 WHERE KEY=:key"
    param = { 'key':  ws_name }
    cursor = conn.cursor()
    cursor.execute(sql, param)
    name, ws_meta  = cursor.fetchone()

    return ws_meta.encode("utf-8")


def load_variable_meta_json(ws_name, var_name):
    sql = "SELECT NAME, DATA FROM TABLE1 WHERE KEY=:key"
    param = { 'key':  ws_name }
    cursor = conn.cursor()
    cursor.execute(sql, param)
    name, var_meta  = cursor.fetchone()

    return var_meta.encode("utf-8")

# http://www.numericalexpert.com/blog/sqlite_blob_time/
def load_variable_value(ws_name, var_name):
    sql = "SELECT NAME, DATA FROM TABLE1 WHERE KEY=:key"
    param = { 'key':  ws_name + "#" + var_name }
    cursor = conn.cursor()
    cursor.execute(sql, param)
    name, data  = cursor.fetchone()

    return data.encode("utf-8")


