class Engine(object):
    def __init__(self):
        self._rpm = 0

    def on(self):
        self._rpm = 2000

    def off(self):
        self._rpm = 0

    @property
    def rpm(self):
        return self._rpm

    def __repr__(self):
        return (f'{self.__class__.__name__}:\n'
                f'    - Revs per Minute: { self._rpm }')


def main():
    engine = Engine()
    engine.on()
    print(f'Current RPM: { engine.rpm }')
    print(engine)
    engine.off()
    print(f'Current RPM: { engine.rpm }')
    print(engine)


if __name__ == '__main__':
    main()
