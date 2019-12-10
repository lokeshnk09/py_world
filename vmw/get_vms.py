from pyVmomi import vim
from vmw.vc_connect import get_all_obj, sc


clusters = get_all_obj(sc, [vim.ClusterComputeResource])
for cluster in clusters:
    print("ClusterName:", cluster.name)


def get_vms():
    count = 0
    vms = get_all_obj(sc, [vim.VirtualMachine])
    _virtual_machines = {}
    for vm in vms:
        print('{}-VM_Name : {}' .format(count, vm.name))
        count += 1

    return vms


def get_vm_snapshot():
    for vm in get_all_obj(sc, [vim.VirtualMachine]):
        if not vm or vm.snapshot is None:
            continue
        else:
            for sn in vm.snapshot.rootSnapshotList:
                print("snapshot : ", vm.name, sn.name, sn.description)


if __name__ == '__main__':
    get_vms()
    get_vm_snapshot()





''''
        _ip_address = ""
        summary = vm.summary
        if summary.guest is not None:
            _ip_address = summary.guest.ipAddress
            if _ip_address is None:
                _ip_address = ""

        virtual_machine = {
            summary.config.name: {
                "guest_fullname": summary.config.guestFullName,
                "power_state": summary.runtime.powerState,
                "ip_address": _ip_address
            }
        }

        _virtual_machines.update(virtual_machine)
    return _virtual_machines 
'''