import pymysql
import notica_common.const
from .singleton import Singleton

class MysqlConnector(Singleton):
    def __init__(self):
        try:
            const = notica_common.const.Const.get_instance()
            self.conn = pymysql.connect(host=const.MIERUKA_HOST, user=const.MIERUKA_USER,
                                passwd=const.MIERUKA_PASSWORD, db=const.MIERUKA_DB, connect_timeout=5)
        except pymysql.MySQLError as e:
            self.conn = None
        except Exception as e:
            self.conn = None

    def is_connected(self):
        return True if self.conn else False
    