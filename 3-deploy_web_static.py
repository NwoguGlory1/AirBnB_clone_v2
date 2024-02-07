#!/usr/bin/python3
""" Creates and distributes an archive to your web servers"""

from datetime import datetime
from fabric.api import *
from os import path

"""Define your web server hosts/user """
env.hosts = ['100.25.162.179', '54.161.253.7']
env.user = "ubuntu"
env.key_filename = ['']


@runs_once
def do_pack(archive_path=None):
    """
    Generates a .tgz archive from the contents
    of the web_static folder
    """
    """ Define the timestamp and path for the archive"""
    try:
        Today = datetime.now().strftime('%Y%m%d%H%M%S')
        path = "versions/web_static_{:s}.tgz".format(Today)

        """ Prints a message to indcate start of packing process"""
        print("Packing web_static to {:s}".format(path))

        """ Hides output of versions directries created if it doesnt exist"""
        with hide('running'):
            local('mkdir -p ./versions')

        """ creates archive with cvzf locally"""
        local('tar -cvzf {:s} web_static'.format(path))

        with hide('running'):
            """ counts the no of bytes in path & capture captures byte count"""
            size = local('wc -c < {:s}'.format(path), capture=True)

        print('web_static packed: {:s} -> {:s}Bytes'.format(path, size))

        return path

    except:
        return None


def do_deploy(archive_path):
    """
    Deploy an archive to multiple web servers.
    archive_path: Local path to the archive file
    """

    if not path.exists(archive_path):
        return False

    path_nx = path.splitext(archive_path)[0]
    """ splits archive to get only base name eg /path/to/archive"""
    path_nx = path_nx.split('/')[-1]
    """further splits /path/to/archive to get archive """
    path_yx = path_nx + '.tgz'
    """ appends .tgz extensn to base name, archive.tgz"""

    try:
        """ Uploads archive to the remote server"""
        put(archive_path, '/tmp/', sudo=True)

        """" creates directories for archive before decompressn"""
        run('sudo mkdir -p /data/web_static/releases/{:s}/'.format(path_nx))

        """
        Extracts archive to
        /data/web_static/releases/<archive filename without .tgz extensn>
        tar: funtion to compress/decompress files
        -xvzf: option to help tar
        /tmp/{:s} : path to compressed archive, path_yx
        C: means change to directory
        /data/web_static/releases: path where archive isdecompressed, path_nx
        """

        run('sudo tar -xvzf /tmp/{:s} -C /data/web_static/releases/{:s}/'.
            format(path_yx, path_nx))

        """ Delete the archive fpath_yx from /tmp/"""
        run('sudo rm /tmp/{:s}'.format(path_yx))

        """ moved all files/dir from web_static subdir to releases"""
        run('sudo mv /data/web_static/releases/{:s}/web_static/*'
            ' /data/web_static/releases/{:s}/'.
            format(path_nx, path_nx))

        """ Deletes then now empty web_static subdir"""
        run('sudo rm -rf /data/web_static/releases/{:s}/web_static'.
                format(path_nx))

        """Deletes symbolic link created in task 0 """
        run('sudo rm -rf /data/web_static/current')

        """ Create new sym link /data/web_static/current now linked
        to /data/web_static/releases/<archive filename without .tgz """
        run('ln -s /data/web_static/releases/{:s}/ /data/web_static/current'.
            format(path_nx))

        print("New version deployed!")
        return True
    except:
        return False


def deploy():
    """ creates and distributes an archive to your web servers"""
    archive_path = do_pack()
    if not archive_path :
        return False

    return do_deploy(archive_path)
