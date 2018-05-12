from .settings import SettingManager as SettingMan
from .db import engineSelect
from .web import FlaskEngine
from .webpage import Blueprints

_setting_man = SettingMan()
_setting = _setting_man.get()

DB_Engine = _setting.Preferences['DB_Engine']
DB_Profile = _setting.Engine[DB_Engine]

Web_Engine = _setting.Preferences['Web_Engine']
Web_Profile = _setting.Engine[Web_Engine]


Web = FlaskEngine(Web_Profile)

_registered = {}
for each in Blueprints:
    Web.register_blueprint(
        each.parent.extract(),
        url_prefix=each.parent.route_path
    )
    _registered[each.parent.name] = each.parent.description

print("""[ Profiles ]\n{}\n{}\n{}\n{}\n{}{}\n{}""".format(
    "  + DB Profile : " + DB_Engine,
    "\n".join(["{:>10} : {:5}".format(" - "+k, repr(v)) for k, v in DB_Profile.items()]),
    "  + Web Profile : " + Web_Engine,
    "\n".join(["{:>10} : {:5}".format(" - "+k, repr(v)) for k, v in Web_Profile.items()]),
    "  + Detected blueprints : ",
    len(Web.app.blueprints),
    "\n".join(["     {:>10} {:>10}".format(name, desc) for name, desc in _registered.items()])
))
