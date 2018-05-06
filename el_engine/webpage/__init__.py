from ..settings import SettingManager

path = SettingManager().get().Preferences['Template_path']

# Templates
from .root import Root


Blueprints = [
    Root(path)
]