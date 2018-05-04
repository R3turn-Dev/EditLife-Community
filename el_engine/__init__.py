from .settings import SettingManager as SettingMan

_setting_man = SettingMan()
_setting = _setting_man.get()

DB_Engine = _setting.Preferences['DB_Engine']
DB_Profile = _setting.Engine[DB_Engine]

Web_Engine = _setting.Preferences['Web_Engine']
Web_Profile = _setting.Engine[Web_Engine]

print("""[ Profiles ]\n{}\n{}\n{}\n{}""".format(
    "  + DB Profile : " + DB_Engine,
    "\n".join(["{:>10} : {:5}".format(" - "+k, repr(v)) for k, v in DB_Profile.items()]),
    "  + Web Profile : " + Web_Engine,
    "\n".join(["{:>10} : {:5}".format(" - "+k, repr(v)) for k, v in Web_Profile.items()])
))
