from .root import Root
from ..settings import SettingManager

path = SettingManager().get().Preferences['Template_path']

Blueprints = [
    Root(path)
]