from json import dump, load, dumps, loads


class SettingManager:
    def __init__(self, path="./sub/settings.json"):
        self.setting = Setting()

        self.filename = path
        self.file = None

        self.load()

    def load(self):
        self.file = open(self.filename, "r")
        self.setting = Setting(**load(self.file))

    def save(self):
        dump(self.setting.__dict__, open(self.filename, "w"), indent=2)  # PyCharm Default: 2 indent

    def get(self):
        return self.setting


class Setting:
    def __repr__(self):
        return repr(self.__dict__)

    def __str__(self):
        return str(self.__dict__)

    def __init__(self, **kwargs):
        """
        :param org: Original Set of Dictionary
        """
        self.__dict__ = kwargs
