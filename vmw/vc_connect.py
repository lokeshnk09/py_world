
from pyVim import connect
import ssl

s = ssl.SSLContext(ssl.PROTOCOL_SSLv23)  # For VC 6.5/6.0 s=ssl.SSLContext(ssl.PROTOCOL_TLSv1)
s.verify_mode = ssl.CERT_NONE

try:
    sc = connect.SmartConnect(host="192.168.1.11", user="administrator@vsphere.local", pwd="VMware1!", sslContext=s)
    content = sc.content
    print('Valid certificate')

except:
    sc = connect.SmartConnect(host="192.168.1.11", user="vmadmin", pwd="VMware1!", sslContext=s)
    print('Invalid or untrusted certificate')


def get_all_obj(content, viewtype):
    obj = {}
    container = content.viewManager.CreateContainerView(content.rootFolder, viewtype, True)
    for ref_object in container.view:
        obj.update({ref_object: ref_object.name})
    return obj


def data_center():
    dc = content.rootFolder.childEntity
    for i in dc:
        print("Datacenter : ", i.name)
        print("Time :", sc.CurrentTime())
        print("vCenter Version : ", content.about.version)
        print("vCenter build : ", content.about.build)


if __name__ == "__main__":
    data_center()

