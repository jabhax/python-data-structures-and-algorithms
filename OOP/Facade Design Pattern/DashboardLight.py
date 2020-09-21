class DashboardLight(object):
    def __init__(self, on=False):
        self._on = on

    def __str__(self):
        return (f'{self.__class__.__name__}:\n'
                f'    - Methods:\n'
                f'      - @property on(): -> boolean\n'
                f'      - @property setter on(status): -> void\n'
                f'      - @property status(): -> string\n')

    @property
    def on(self):
        return self._on

    @on.setter
    def on(self, status):
        self._on = status

    @property
    def status(self):
        msg = 'status: ON' if self._on else 'status: OFF'
        print(msg)
        return msg

def main():
    db_light = DashboardLight()
    #  print dashboard-light status
    print(f'on: { db_light.on }')
    db_light.status
    #  turn on dashboard-light and print status
    db_light.on = True
    print(f'on: { db_light.on }')
    db_light.status
    # print DashboardLight instance
    print(db_light)


if __name__ == '__main__':
    main()
