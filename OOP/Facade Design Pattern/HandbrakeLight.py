from DashboardLight import DashboardLight


class HandbrakeLight(DashboardLight):
    pass

def main():
    hb_light = HandbrakeLight()
    print(f'HandbrakeLight.on: { hb_light.on }')
    hb_light.status

    hb_light.on = True
    print(f'HandbrakeLight.on: { hb_light.on }')
    hb_light.status


if __name__ == '__main__':
    main()
