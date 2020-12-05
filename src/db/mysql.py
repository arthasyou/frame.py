import pymysql
import datetime
from config.database import mysql as cfg
from loguru import logger
from utility import sqlfmt

__all__: ['m']

class Mysql():
    def __init__(self):
        self.__connect()
    
    def __connect(self):
        connection = pymysql.connect(
            host=cfg['host'],
            port=cfg['port'],
            user=cfg['username'],
            password=cfg['password'],
            db=cfg['database'],
            charset=cfg['charset'],
            cursorclass=pymysql.cursors.DictCursor
        )
        self.__connection = connection
    
    def __close(self):
        self.__connection.close()
    
    def reconnect(self):
        self.__close()
        self.__connect()
    
    def __get_cursor(self):
        return self.__connection.cursor()
    
    def fetch(self, query):
        cursor = self.__get_cursor()
        try:
            cursor.execute(query)
            return ('ok', cursor.fetchall())
        except Exception as e:
            logger.error("mysql fetch error: {}", e)
            return ('fail', e)
        finally:
            cursor.close()
    
    def execute(self, query):
        cursor = self.__get_cursor()
        try:
            cursor.execute(query)
            self.__connection.commit()
            return 'ok'
        except Exception as e:
            self.__connection.rollback()
            logger.error("mysql execute error: {}", e)
            return ('fail', e)
        finally:
            cursor.close()

    def select(self, table, items='*'):
        return sqlfmt.select(items, table)

    def insert(self, table, items):
        return sqlfmt.insert(table, items)
    
    def replace(self, table, items):
        return sqlfmt.replace(table, items)

    def update(self, table, items):
        return sqlfmt.update(table, items)
    
    def delete(self, table):
        return sqlfmt.deltet(table)
    
    def where(self, conditions):
        return sqlfmt.where(conditions)
    
    def whereOr(self, conditions):
        return sqlfmt.whereOr(conditions)

    def subAnd(self, conditions):
        return sqlfmt.subAnd(conditions)
    
    def subOr(self, conditions):
        return sqlfmt.subOr(conditions)

    def order(self, key):
        return sqlfmt.order(key)
    
    def orderDesc(self, key):
        return sqlfmt.orderDesc(key)
    
    def limit(self, page, column):
        return sqlfmt.limit(page, column)

m = Mysql()