from pyVim import connect
import ssl
from pyVmomi import vim

s = ssl.SSLContext(ssl.PROTOCOL_SSLv23)  # For VC 6.5/6.0 s=ssl.SSLContext(ssl.PROTOCOL_TLSv1)
s.verify_mode = ssl.CERT_NONE

try:
    service_instance = connect.SmartConnect(host="192.168.1.11", user="administrator@vsphere.local", pwd="VMware1!", sslContext=s)
    sc = service_instance.content
    print('Valid certificate')

except:
    service_instance = connect.SmartConnect(host="192.168.1.11", user="vmadmin", pwd="VMware1!", sslContext=s)
    print('Invalid or untrusted certificate')


def get_all_obj(content, viewtype):
    obj = {}
    container = content.rootFolder
    container_view = content.viewManager.CreateContainerView(container, viewtype, True)
    for ref_object in container_view.view:
        obj.update({ref_object: ref_object.name})
    return obj


def get_vms_info():
    count = 0
    vms = get_all_obj(sc, [vim.VirtualMachine])
    for vm in vms:
        summary = vm.summary
        print("Name       : ", summary.config.name)
        if summary.guest is not None:
            ip_address = summary.guest.ipAddress
            tools_version = summary.guest.toolsStatus
            if tools_version is not None:
                print("VMware-tools: ", tools_version)
            else:
                print("Vmware-tools: None")
            if ip_address:
                print("IP         : ", ip_address)
            else:
                print("IP         : None")
        print('--------------------------------')
        count += 1


if __name__ == "__main__":
    get_vms_info()



