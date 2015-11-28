"""
Importing this module will monkey patch fabric.
 - Modifies put to accept user and group parameters and call chmod on them after the put
 - Adds mkdir
 - Adds chmod function to chmod, chown and chgrp a remote path
"""
import fabric.api
from fabric.api import sudo,run
from fabric.network import needs_host


@needs_host
def mkdir(path=None,use_sudo=False,mode=None,user=None,group=None):
    cmd='mkdir {}'.format(path)
    sudo(cmd) if use_sudo else run(cmd)
    chmod(path,use_sudo,mode,user,group)
fabric.api.mkdir=mkdir


@needs_host
def chmod(remote_path=None,use_sudo=False,mode=None,user=None,group=None):
    if mode:
        cmd='chmod {:03o} {}'.format(mode,remote_path)
        sudo(cmd) if use_sudo else run(cmd)
    if user:
        cmd='chown {} {}'.format(user,remote_path)
        sudo(cmd) if use_sudo else run(cmd)
    if group:
        cmd='chgrp {} {}'.format(group,remote_path)
        sudo(cmd) if use_sudo else run(cmd)
fabric.api.chmod=chmod


oldPut=fabric.api.put
@needs_host
def put(local_path=None,remote_path=None,use_sudo=False,mirror_local_mode=False,mode=None,user=None,group=None,use_glob=True,temp_dir=""):
    ret=oldPut(local_path,remote_path,use_sudo=use_sudo,mirror_local_mode=mirror_local_mode,mode=mode,use_glob=use_glob,temp_dir=temp_dir)
    # do chmod if required
    if ret.succeeded and (user or group):
        for path in ret:
            chmod(path,use_sudo,None,user,group)
fabric.api.put=put
