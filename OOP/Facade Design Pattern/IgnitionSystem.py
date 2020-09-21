class IgnitionSystem(object):
    @staticmethod
    def produce_spark():
        return True

    def __repr__(self):
        return (f'{self.__class__.__name__}\n'
                f'  - Methods:\n'
                f'    - @staticmethod produce_spark(): -> boolean\n')


def main():
    ignition_system = IgnitionSystem()
    print(ignition_system)
    print(f'ignition_system.produce_spark(): { ignition_system.produce_spark() }')


if __name__ == '__main__':
    main()
