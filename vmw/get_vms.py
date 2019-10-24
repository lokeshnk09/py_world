from pyVmomi import vim
from vmw.vc_connect import get_all_obj, content


clusters = get_all_obj(content, [vim.ClusterComputeResource])
for cluster in clusters:
    print("ClusterName:", cluster.name)


def get_vms():
    count = 0
    vms = get_all_obj(content, [vim.VirtualMachine])
    _virtual_machines = {}
    for vm in vms:
        print('{}-VirtualName: {}' .format(count, vm.name))
        count += 1
    return vms


v = get_vms()


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