from pyVmomi import vim
from vmw import vc_connect
from pyVim.connect import SmartConnect, Disconnect


def get_vm_list():
    datacenter = c.content.rootFolder()

