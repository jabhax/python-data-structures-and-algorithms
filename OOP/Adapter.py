class EUSocketInterface:
    def voltage(self): pass
    def is_live(self): pass
    def is_neutral(self): pass
    def is_earth(self): pass

class Socket(EUSocketInterface):
    # Adaptee
    def voltage(self):
        return 240

    def is_live(self):
        return 1

    def is_neutral(self):
        return -1

    def is_earth(self):
        return 0

class USASocketInterface:
    # Target Interface
    def voltage(self): pass
    def is_live(self): pass
    def is_neutral(self): pass
    def is_earth(self): pass

class Adapter(USASocketInterface):
    # Adapter
    __socket = None
    def __init__(self, socket):
        self.__socket = socket

    def voltage(self):
        return 120

    def is_live(self):
        return self.__socket.is_live()

    def is_neutral(self):
        return self.__socket.is_neutral()

class Device:
    # Client
    __adapter = None
    def __init__(self, adapter):
        self.__adapter = adapter

    def power_on(self):
        if self.__adapter.voltage() > 120:
            msg = (f'Danger!!! Voltage = { self.__adapter.voltage() }V exceeds'
                    f' max voltage of 120V')
        else:
            msg = ((f'Device successfully powered on and is live!')
                    if (self.__adapter.is_live() and self.__adapter.is_neutral() == -1)
                    else (f'Device is powered off.'))
            print(msg)


def main():
    # Plug in
    socket = Socket()
    adapter = Adapter(socket)
    device = Device(adapter)
    # power on Device
    device.power_on()
    return 0

if __name__ == '__main__':
    main()
