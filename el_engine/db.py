from psycopg2 import connect
from threading import get_ident
from .exceptions import DBEngineNotFound


def engineSelect(engine):
    if engine in globals().keys():
        return globals()[engine]
    else:
        raise DBEngineNotFound


class PostgreSQL:
    def __init__(self, initial_connect=True, **kwargs):
        self.__dict__ = kwargs

        self.conn = None
        self.cursor = None

        self.connDict = {}
        self.curDict = {}

        if initial_connect:
            self.getConn()
            self.getCursor()

    def getConn(self):
        self.conn = connect(
            host=self.host,
            port=self.port,
            user=self.user,
            password=self.pw,
            database=self.db
        )

        self.conn.autocommit = True
        return self.conn

    def getCursor(self):
        thread_id = get_ident().__int__()

        if thread_id not in self.connDict.keys():
            self.connDict[thread_id] = self.getConn()

        if thread_id not in self.curDict.keys():
            self.curDict[thread_id] = self.connDict[thread_id].cursor()

        return self.curDict[thread_id]

    def execute(self, query):
        return self.getConn().execute(query)

    def checkTable(self, table_name):
        conn = self.getConn()
        cur = conn.cursor()

        cur.execute("SELECT table_name FROM information_schema.tables WHERE table_name = '{}';".format(table_name))
        data = cur.fetchall()
        return bool(data)
