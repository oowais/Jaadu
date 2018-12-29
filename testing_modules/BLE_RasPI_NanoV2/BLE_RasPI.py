# Uses BluePy - https://github.com/IanHarvey/bluepy

import binascii
from bluepy import btle

class MyDelegate(btle.DefaultDelegate):
    def __init__(self):
        btle.DefaultDelegate.__init__(self)

    def handleNotification(self, cHandle, data):
        try:
            temp = binascii.b2a_hex(data)
            num_data = temp[0:2].decode("utf-8")
            past = temp[2:4].decode("utf-8")
            present = temp[4:6].decode("utf-8")
            future = temp[6:8].decode("utf-8")
            print("I was {}, I am {}, and I will be {}".format(past, present, future))
        except Exception:
            pass


if __name__ == "__main__":
    dev1 = btle.Peripheral("CE:49:03:E2:2F:C6", btle.ADDR_TYPE_RANDOM)
    serv = dev1.getServiceByUUID("713d0001-503e-4c75-ba94-3148f18d941e")
    ch = serv.getCharacteristics("713d0002-503e-4c75-ba94-3148f18d941e")[0]
    notify = dev1.getCharacteristics(uuid="713d0002-503e-4c75-ba94-3148f18d941e")[0]
    notify_handle = notify.getHandle() + 1
    dev1.writeCharacteristic(notify_handle, b"\x01\x00", withResponse=True)
    dev1.setDelegate(MyDelegate())

    while True:
        if dev1.waitForNotifications(1.0):
            continue
