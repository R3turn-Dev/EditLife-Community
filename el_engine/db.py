from psycopg2 import connect
from threading import get_ident
from .exceptions import DBEngineNotFound
from .settings import SettingManager as SettingMan

_setting = SettingMan().get()
engine = _setting.Preferences['DB_Engine']
profile = _setting.Engine[engine]


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

    def getMemberCount(self):
        try:
            conn = self.getConn()
            cur = conn.cursor()

            cur.execute("SELECT count(*) FROM users;")
            data = cur.fetchall()

            return [False, data[0][0]]
        except Exception as ex:
            return [ex, None]

    def getBoards(self, selects="*", sort="index"):
        try:
            conn = self.getConn()
            cur = conn.cursor()

            cur.execute("SELECT {} FROM boards ORDER BY {};".format(selects, sort))
            data = cur.fetchall()

            return [False, [x[0] for x in data]]
        except Exception as ex:
            return [ex, None]

    def getArticles(self, selects="*", board="커뮤니티", sort="no DESC"):
        try:
            conn = self.getConn()
            cur = conn.cursor()

            cur.execute("SELECT {} FROM articles WHERE board = '{}' ORDER BY {};".format(selects, board, sort))
            data = cur.fetchall()

            return [False, data]
        except Exception as ex:
            return [ex, None]

    def loginAccount(self, id, pw):
        try:
            conn = self.getConn()
            cur = conn.cursor()

            cur.execute("SELECT users.nickname, users.email_verified FROM users WHERE id = '{}' and password = '{}';".format(id, pw))
            data = cur.fetchall()

            return [False, data]
        except Exception as ex:
            return [ex, None]
