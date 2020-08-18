#!/usr/bin/python3
"""create a .tgz file"""
from datetime import datetime
import os.path
from fabric.api import put, run, env
from fabric.operations import local, put, run

env.hosts = ['35.243.223.95', '54.147.36.179']


def do_pack():
    """funtion do_pack"""
    local('mkdir -p versions')
    path = local("tar -cvzf versions/web_static_{}.tgz web_static".format(
        datetime.strftime(datetime.now(), "%Y%m%d%H%M%S")))
    if path.failed:
        return None
    else:
        return path


def do_deploy(archive_path):
    """funtion frabric"""
    if (os.path.isfile(archive_path) is False):
        return False
    try:
        archive = archive_path.split("/")[-1]
        archiv_name = archive.split(".")[0]

        put(archive_path, "/tmp/{}".format(archive))
        run("sudo mkdir -p /data/web_static/releases/{}/".format(archiv_name))
        run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/"
            .format(archive, archiv_name))
        run("rm /tmp/{}".format(archiv_name))
        run("mv /data/web_static/releases/{}/web_static/* "
            "/data/web_static/releases/{}/"
            .format(archiv_name, archiv_name))
        run("rm -rf /data/web_static/releases/{}/web_static"
            .format(archiv_name))
        run("rm -rf /data/web_static/current")
        run("ln -s /data/web_static/releases/{}/ /data/web_static/current"
            .format(archiv_name))
    except AssertionError as error:
        return False


def deploy():
    """function deploy"""
    path = do_pack()

    if path is None:
        return False

    return do_deploy(path)
