from src.profile.common import common_profile
from src.profile.territories.ita import ita_profile
from src.profile.territories.jpn import jpn_profile


def get_all_profile():
    japan = jpn_profile.get_japan_profile()
    italy = ita_profile.get_italy_profile()
    common = common_profile.get_common_profile()
    return f"{japan} | {italy} | {common}"


if __name__ == '__main__':
    print(get_all_profile())
