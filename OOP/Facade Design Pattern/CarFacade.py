from IgnitionSystem import IgnitionSystem
from Engine import Engine
from FuelTank import FuelTank
from Dashboard import Dashboard


class CarFacade(object):
    def __init__(self):
        self._ignition_system = IgnitionSystem()
        self._engine = Engine()
        self._tank = FuelTank()
        self._dashboard = Dashboard()

    @property
    def kmpl(self):
        # km per liter
        return 17.0

    def burn_fuel(self, km):
        liters = min(self._tank.fuel, km / self.kmpl)
        self._tank.fuel -= liters

    def start(self):
        print('Starting engine...')
        self._dashboard.view
        if self._ignition_system.produce_spark():
            self._engine.on()
        else:
            print('Can\'t start engine; fault ignition system!')

    def has_enough_fuel(self, km , kmpl):
        return (self._tank.fuel >= (km / kmpl))

    def drive(self, km=100):
        if self._engine.rpm > 0:
            while (self.has_enough_fuel(km, self.kmpl)):
                self.burn_fuel(km)
                print(f'Drove { km }km! {self._tank.fuel:.2f}L of fuel remaining.')
        else:
            print(f'Please turn on the Engine before attempting to drive!')

    def park(self):
        print('Parking...')
        self._dashboard.set_lights_status('handbrake', False)
        self._dashboard.view
        self._engine.off()

    def fill_tank(self):
        self._tank.fuel = 100

    def toggle_fogs(self):
        print('Toggling Fog Lights')
        self._dashboard.toggle_lights('fog')

    def toggle_handbrakes(self):
        print('Toggling Handbrake Lights')
        self._dashboard.toggle_lights('handbrakes')

    def toggle_dashboard(self):
        print('Toggling All Lights')
        self._dashboard.toggle_lights()

    def __repr__(self):
        return (f'Car:\n  * { self._ignition_system }'
                f'\n  * { self._engine }'
                f'\n  * { self._tank }'
                f'\n  * { self._dashboard }')

def main():
    car = CarFacade()
    car.start()
    car.drive()
    car.toggle_fogs()
    car.toggle_fogs()
    car.park()
    car.fill_tank()
    print(f'Printing car...\n{car}')

    car.drive()
    car.start()
    car.drive()
    print(f'Printing car...\n{car}')

if __name__ == '__main__':
    main()
