from src.profile.common import common_profile
from src.profile.territories.ita import ita_profile
from src.profile.territories.jpn import jpn_profile


def get_all_profile():
    jpn_profile.get_japan_profile()
    ita_profile.get_italy_profile()
    common_profile.get_common_profile()
