#!/usr/bin/python3
""" Generates a .tgz archive from web_static folder of AirBnB clone """

from datetime import datetime
from fabric.api import *


def do_pack():
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
        
        """ Hides output of the versions directries created if it doesnt exist"""
        with hide('running'):
            local('mkdir -p ./versions')
 
        """ creates archive with cvzf locally"""
        local('tar -cvzf {:s} web_static'.format(path))

        with hide('running'):
        """ counts the no of bytes in path ^ capture captures byte count"""
            size = local('wc -c < {:s}'.format(path), capture=True)

        print('web_static packed: {:s} -> {:s}Bytes'.format(path, size))

        return path

    except:
        return None
