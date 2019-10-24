from pyVmomi import vim
from vmw import vc_connect
from pyVim.connect import SmartConnect, Disconnect


def get_vm_list():
    dc = vc_connect.data_center()
    containerview = dc.viewManager.CreateContainerview(dc, [vim.VirtualMachine], True)
    children = containerview.view
    vm_list = {}
    for child in children:
        summary = child.summary
        if not summary.config.name == control_vm:
            vm_list[summary.config.name] = summary.config.uuid

    dc.Disconnect(service_instance)
    return vm_list