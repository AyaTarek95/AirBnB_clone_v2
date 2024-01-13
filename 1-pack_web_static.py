#!/usr/bin/python3
"""generates a .tgz archive
from web_static folder
"""
from fabric.api import local
from datetime import datetime


def do_pack():
    """generates archive from folder"""
    try:
        fdate = datetime.now().strftime('%Y%m%d%H%M%S')
        fileN = f'web_static_{fdate}.tgz'
        local('mkdir -p versions')
        local(f'tar -cvzf versions/{fileN} web_static')
        return f'versions/{fileN}'
    except Exception:
        return None
