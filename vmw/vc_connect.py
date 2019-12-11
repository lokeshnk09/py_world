
from pyVim import connect
import ssl

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
    container = content.viewManager.CreateContainerView(content.rootFolder, viewtype, True)
    for ref_object in container.view:
        obj.update({ref_object: ref_object.name})
    return obj


def data_center():
    dc = sc.rootFolder.childEntity
    for i in dc:
        print("Datacenter : ", i.name)
        print("Time :", service_instance.CurrentTime())
        print("vCenter Version : ", sc.about.version)
        print("vCenter build : ", sc.about.build)


if __name__ == "__main__":
    data_center()

