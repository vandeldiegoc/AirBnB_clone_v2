#!/urs/bin/python3
"""create a .tgz file"""
from fabric.api import *
from datetime import datetime


def do_pack():
    """funtion do_pack"""
    local('mkdir -p versions')
    path = local("tar -cvzf versions/web_static_{}.tgz web_static".format(
        datetime.strftime(datetime.now(), "%Y%m%d%H%M%S")))
    if path.failed:
        return None
    else:
        return path
