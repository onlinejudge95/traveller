from modules.box__default.settings.models import Settings


def get_setting(name):
    """
    Used as key-value lookup from Settings table

    Parameters
    ----------
    name: str
        name of key

    Returns
    -------
    str
        value of key
    """
    s = Settings.query.filter(Settings.setting == name).first()
    if s is None:
        return None
    else:
        return s.value



def set_setting(key, value):
    setting = Settings.query.filter(Settings.setting == key).first()
    if setting:
        setting.value = value
        setting.update()