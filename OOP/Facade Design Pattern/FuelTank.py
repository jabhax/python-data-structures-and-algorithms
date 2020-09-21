class FuelTank(object):
    def __init__(self, level=30):
        self._level = level

    @property
    def fuel(self):
        return self._level

    @fuel.setter
    def fuel(self, level):
        self._level = 0 if level < 0 else level
        self._level = 100 if level > 100 else level

    def __repr__(self):
        return (f'{self.__class__.__name__}:\n'
                f'    - Fuel Level: { self._level }')


def main():
    tank = FuelTank()
    print(tank)
    tank.fuel = 20
    print(f'Fuel Level: { tank.fuel }')


if __name__ == '__main__':
    main()
