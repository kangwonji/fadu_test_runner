import platform


def info():
    platform_info = platform.uname()
    # TODO: status 정보 구체화 필요
    return {
        'system': platform_info.system,
        'release': platform_info.release,
        'version': platform_info.version,
    }
