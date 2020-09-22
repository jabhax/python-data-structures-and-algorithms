# Design Patterns

'''
Adapter Pattern works as a bridge between two incompatible interfaces. This
pattern involves a single class, which is responsible for joining the
functionalities of Independent or Incompatible Interfaces. It converts the
interface of a class into another interface based on some requirement. The
pattern includes a polymorphism which names one name and multiple forms. Say
for a shape class which can use as per the requirements gathered.

Example:
    A real life example could be the case of a card reader, which acts as an
    adapter between memory card and a laptop. You plug in the memory card into
    the card reader and the card reader into the laptop so that memory card can
    be read via the laptop.
'''

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
