#!/usr/bin/python3
""" creating a .tgz archive from the contentsof web_static folder
"""
from fabric.api import local
from datetime import datetime


def do_pack():
    """Compressing the contents of web_static folder"""
    time = datetime.now().strftime("%Y%m%d%H%M%S")
    pathfile = "versions/web_static_{}.tgz".format(time)
    try:
        local("mkdir -p versions")
        local("tar -cvzf {} web_static".format(pathfile))
        return pathfile
    except Exception as e:
        return None
