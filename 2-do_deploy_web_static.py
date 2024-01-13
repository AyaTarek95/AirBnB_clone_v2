#!/usr/bin/python3
"""distributes an archive
to my web servers
"""

from fabric.api import put, run, env
from os.path import exists
env.user = 'ubuntu'
env.hosts = ['54.237.101.225', '18.207.1.65']


def do_deploy(archive_path):
    """distribute archive
    to web servers
    """
    if exists(archive_path) is False:
        return False
    try:
        file_name = archive_path.split('/')[-1]
        no_exten = file_name.split('.')[0]
        path = '/data/web_static/releases/'
        put(archive_path, '/tmp/')
        run('mkdir -p {}{}/'.format(path, no_exten))
        run('tar -xzf /tmp/{} -C {}{}/'.format(file_name, path, no_exten))
        run('rm /tmp/{}'.format(file_name))
        run('rm -rf /data/web_static/current')
        run('ln -s {}{}/ /data/web_static/current'.format(path, no_exten))
        return True
    except Exception:
        return False
