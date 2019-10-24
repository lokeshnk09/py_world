from pyVmomi import vim
from pyVim.connect import SmartConnect, Disconnect
import ssl


s = ssl.SSLContext(ssl.PROTOCOL_SSLv23)  # For VC 6.5/6.0 s=ssl.SSLContext(ssl.PROTOCOL_TLSv1)
s.verify_mode = ssl.CERT_NONE

try:
    c = SmartConnect(host="192.168.1.11", user="administrator@vsphere.local", pwd="VMware1!", sslContext=s)
    print('Valid certificate')
except:
    c = SmartConnect(host="192.168.1.11", user="vmadmin", pwd="VMware1!", sslContext=s)
    print('Invalid or untrusted certificate')


def data_center():
    datacenter = c.content.rootFolder
    for i in datacenter.childEntity:
        print("Datacenter : ", i.name)
        print("Time :", c.CurrentTime())
        print("vCenter Version : ", c.content.about.version)
        print("vCenter build : ", c.content.about.build)


if __name__ == "__main__":
    data_center()




