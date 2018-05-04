from psycopg2 import connect
from threading import get_ident


class PostgreSQL:
    def __init__(self, config, initial_connect=True):
        self.conn = None
        self.cursor = None

        self.connDict = {}
        self.curDict = {}

        self.host = config.get('host')
        self.port = config.get('post')
        self.db = config.get('db')
        self.user = config.get('user')
        self.pw = config.get('pw')

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

        cur.execute("SELECT table_name FROM information_schema.tables WHERE table_name = '%s';" % table_name)
        data = cur.fetchall()
        return bool(data)
