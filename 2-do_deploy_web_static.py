#!/usr/bin/python3
"""a Fabric script (based on the file 1-pack_web_static.py) and deploye """
from fabric.api import run, env, put
import os.path

env.hosts = ['54.236.44.93', '100.26.122.135']
env.key_filename = '~/.ssh/school'
env.user = 'ubuntu'


def do_deploy(archive_path):
    """Generate the .tgz archive from the contents of web_static folder"""
    if not os.path.isfile(archive_path):
        return False

    # Get the name of the compressed file and remove the file extension
    compresedfile = archive_path.split("/")[-1]
    no_extension = compresedfile.split(".")[0]

    try:
        # Define the remote path and symlink to be used for deployment
        path = "/data/web_static/releases/{}/".format(no_extension)
        sym_link = "/data/web_static/current"

        # Upload the compressed file to the server
        put(archive_path, "/tmp/")

        """ Create the directory for the release and extract the compressed\
                file into it"""
        run("sudo mkdir -p {}".format(path))
        run("sudo tar -xvzf /tmp/{} -C {}".format(
            compresedfile, path))

        """Clean up the compressed file and move the web files to the\
                release directory"""
        run("sudo rm /tmp/{}".format(compresedfile))
        run("sudo mv {}/web_static/* {}".format(path, path))
        run("sudo rm -rf {}/web_static".format(path))

        # Update the symlink to point to the new release directory
        run("sudo rm -rf /data/web_static/current")
        run("sudo ln -sf {} {}".format(path, sym_link))

        # Return success if the deployment was successful
        return True
    except Exception as e:

        # If an exception occurred during deployment, return failure
        return False
