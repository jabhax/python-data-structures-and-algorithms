from HandbrakeLight import HandbrakeLight
from FoglampLight import FoglampLight


class Dashboard(object):
    def __init__(self):
        self._lights = { 'handbrake': HandbrakeLight(), 'fog': FoglampLight() }
        self.DEFAULTS = { 'lights': ['handbrake', 'fog'] }

    @property
    def view(self):
        [f'Dashboard - {lt} ({l.status})' for lt, l in self._lights.items()]

    @property
    def lights(self):
        return self._lights

    def set_lights_status(self, lights=['handbrake', 'fog'], status=False):
        # turn lights into List[str] if not already List[str]
        if type(lights) is not list:
            lights = [str(lights)] if isinstance(lights, str) else [lights]
            # Evaluate lights param as List[str]
            if lights[0].lower() in self.DEFAULTS['lights']:
                self._lights[lights[0]].on = status
            else:
                raise ValueError('Invalid Light object!')
        # Check if empty list was passed in
        if len(lights) == 0:
            raise ValueError('"lights" param cant be empty!')
        # Set all the lights to provided status
        for light in lights:
            if light.lower() in self.DEFAULTS['lights']:
                self._lights[light].on = not(self._lights[light].on)

    def toggle_lights(self, lights=['handbrake', 'fog']):
        if type(lights) is not list:
            lights = [str(lights)] if isinstance(lights, str) else [lights]
        for light in lights:
            self.set_lights_status([light], not(self._lights[light].on))

    def __repr__(self):
        hb, fog = self.lights['handbrake'], self.lights['fog']
        return (f'DashBoard:\n'
                f'  - { hb }\n'
                f'  - { fog }\n')


def main():
    dashboard = Dashboard()
    dashboard.view
    for i in range(5):
        print(f'~*~Toggled Dashboard Lights ({i+1})~*~')
        dashboard.toggle_lights()
        dashboard.view
    print(dashboard)


if __name__ == '__main__':
    main()
