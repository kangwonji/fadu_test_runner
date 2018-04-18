from utils import platform


def test_info():
    """
    platform의 os name, release number, version number를 dictionary 형태로 리턴한다.
    """
    info = platform.info()
    for key in ['system', 'release', 'version']:
        assert key in info
