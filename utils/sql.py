import sqlite3

import datetime


import json


class SqlAppend(object):

    def __init__(self):
        self.conn = sqlite3.connect(':memory:')
        self.curs = self.conn.cursor()

    def table_create(self, table_name):
        self.curs.execute(f'CREATE TABLE {table_name}(id INTEGER PRIMARY KEY, name STRING,'
                          f'test text STRING)')
        self.conn.commit()
        self.conn.close()
        return None

if __name__ == '__main__':

    sql_append = SqlAppend()


    # curs = conn.cursor()
    #
    # curs.execute(
    #     'CREATE TABLE persons(id INTEGER PRIMARY KEY AUTOINCREMENT, name STRING,'
    #     'test text STRING NOT NULL)')
    #
    # curs.execute(
    #     'CREATE TABLE text(name STRING PRIMARY KEY, text STRING)')
    #
    #
    # conn.commit()
    #
    # a = 'test'
    #
    # curs.execute(f'INSERT INTO persons(name, test) values("{a}", "test")')
    # curs.execute('INSERT INTO persons(name, test) values("REOTO", "test")')
    # curs.execute('INSERT INTO persons(name, test) values("KAI", "test")')
    #
    #
    # conn.commit()
    #
    # curs.execute('SELECT DISTINCT * FROM persons ORDER BY id DESC')
    #
    # f = curs.fetchall()
    #
    # conn.close()
    #
    # print(f)
    #
    #
    # for i in range(len(f)):
    #     print(list(f[i]))






