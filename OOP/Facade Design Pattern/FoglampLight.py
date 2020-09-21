from DashboardLight import DashboardLight


class FoglampLight(DashboardLight):
    pass


def main():
    fl_light = FoglampLight()
    print(f'FoglampLight.on: { fl_light.on }')
    fl_light.status

    fl_light.on = True
    print(f'FoglampLight.on: { fl_light.on }')
    fl_light.status


if __name__ == '__main__':
    main()
