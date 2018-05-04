from .settings import SettingManager as SettingMan

_setting_man = SettingMan()
_setting = _setting_man.get()

DB_Engine = _setting.Preferences['DB_Engine']

print(DB_Engine)