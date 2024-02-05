#!/usr/bin/env bash
# Script that generates a .tgz archive from the contents of the web_static folder of AirBnB clone, using do_pack

from datetime import datetime
from fabric.api import *

def do_pack():
    """ 
    Generates a .tgz archive from the contents
    of the web_static folder
    """
    try:
        Today = datetime.now().strftime('%Y%m%d%H%M%S')
        path = "versions/web_static_{:s}.tgz".format(Today)

        msg1 = "Packing web_static to {:s}".format(path)
        print(msg1)

        with hide('running'):
            local('mkdir -p ./versions')

        local('tar -cvzf {:s} web_static'.format(path))

        with hide('running'):
            size = local('wc -c < {:s}'.format(path), capture=True)

        msg2 = 'web_static packed: {:s} -> {:s}Bytes'.format(path, size)
        print(msg2)

        return path

    except:
        return None
