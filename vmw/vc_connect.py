from pyVmomi import vim
from pyVim.connect import SmartConnect, Disconnect
import ssl


s = ssl.SSLContext(ssl.PROTOCOL_SSLv23)  # For VC 6.5/6.0 s=ssl.SSLContext(ssl.PROTOCOL_TLSv1)
s.verify_mode = ssl.CERT_NONE

try:
    sc = SmartConnect(host="192.168.1.11", user="administrator@vsphere.local", pwd="VMware1!", sslContext=s)
    content = sc.content
    print('Valid certificate')

except:
    sc = SmartConnect(host="192.168.1.11", user="vmadmin", pwd="VMware1!", sslContext=s)
    print('Invalid or untrusted certificate')


def get_all_obj(content, viewtype):
    obj = {}
    container = content.viewManager.CreateContainerView(content.rootFolder, viewtype, True)
    for ref_object in container.view:
        obj.update({ref_object: ref_object.name})
    return obj


def data_center():
    datacenter = content.rootFolder.childEntity
    for i in datacenter:
        print("Datacenter : ", i.name)
        print("Time :", sc.CurrentTime())
        print("vCenter Version : ", content.about.version)
        print("vCenter build : ", content.about.build)


def get_vms():
    vms = get_all_obj(content, [vim.VirtualMachine])
    for vm in vms:
        print(vm.name)


clusters = get_all_obj(content, [vim.ClusterComputeResource])
for cluster in clusters:
    print("ClusterName:", cluster.name)


if __name__ == "__main__":
    data_center()
    get_vms()