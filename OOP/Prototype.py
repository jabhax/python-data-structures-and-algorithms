# Design Patterns

'''
Prototype design pattern helps to hide the complexity of the instances created
by the class. The concept of the existing object will differ with that of the
new object, which is created from scratch.

The newly copied object may have some changes in the properties if required.
This approach saves time and resources that go in for the development of a
product.
'''


import copy


class Prototype:
    _type, _power = None, None
    def clone(self): pass
    def get_type(self): return self._type
    def get_power(self): return self._power

class FireType(Prototype):
    def __init__(self, power_value):
        self._type = 'Fire'
        self._power = power_value

    def clone(self): return copy.copy(self)

class WaterType(Prototype):
    def __init__(self, power_value):
        self._type = 'Water'
        self._power = power_value

    def clone(self): return copy.copy(self)


class GrassType(Prototype):
    def __init__(self, power_value):
        self._type = 'Grass'
        self._power = power_value

    def clone(self): return copy.copy(self)

class TypeFactory():
    '''
    Class that Manages prototypes. Static factory, that encapsulates prototype
    initialization and then allows instatiation of the classes from these
    prototypes.
    '''
    __fireType_FirePower, __fireType_WaterPower, __fireType_GrassPower = None, None, None
    __waterType_FirePower, __waterType_WaterPower, __waterType_GrassPower = None, None, None
    __grassType_FirePower, __grassType_WaterPower, __grassType_GrassPower = None, None, None

    @staticmethod
    def initialize():
        FIRE, WATER, GRASS = '*FIRE*', '~WATER~', '#GRASS#'
        TypeFactory.__fireFire = FireType(FIRE)
        TypeFactory.__fireWater = FireType(WATER)
        TypeFactory.__fireGrass = FireType(GRASS)
        TypeFactory.__waterFire = WaterType(FIRE)
        TypeFactory.__waterWater = WaterType(WATER)
        TypeFactory.__waterGrass = WaterType(GRASS)
        TypeFactory.__grassFire = GrassType(FIRE)
        TypeFactory.__grassWater = GrassType(WATER)
        TypeFactory.__grassGrass = GrassType(GRASS)

    @staticmethod
    def get_fireFire():
        return TypeFactory.__fireFire.clone()

    @staticmethod
    def get_fireWater():
        return TypeFactory.__fireWater.clone()

    @staticmethod
    def get_fireGrass():
        return TypeFactory.__fireGrass.clone()

    @staticmethod
    def get_waterFire():
        return TypeFactory.__waterFire.clone()

    @staticmethod
    def get_waterWater():
        return TypeFactory.__waterWater.clone()

    @staticmethod
    def get_waterGrass():
        return TypeFactory.__waterGrass.clone()

    @staticmethod
    def get_grassFire():
        return TypeFactory.__grassFire.clone()

    @staticmethod
    def get_grassWater():
        return TypeFactory.__grassWater.clone()

    @staticmethod
    def get_grassGrass():
        return TypeFactory.__grassGrass.clone()

def main():
    TypeFactory.initialize()
    # Test Fire Types
    instance = TypeFactory.get_fireFire()
    print(f'Type: { instance.get_type() }, Power: { instance.get_power() }')
    instance = TypeFactory.get_fireWater()
    print(f'Type: { instance.get_type() }, Power: { instance.get_power() }')
    instance = TypeFactory.get_fireGrass()
    print(f'Type: { instance.get_type() }, Power: { instance.get_power() }')
    # Test Water Types
    instance = TypeFactory.get_waterFire()
    print(f'Type: { instance.get_type() }, Power: { instance.get_power() }')
    instance = TypeFactory.get_waterWater()
    print(f'Type: { instance.get_type() }, Power: { instance.get_power() }')
    instance = TypeFactory.get_waterGrass()
    print(f'Type: { instance.get_type() }, Power: { instance.get_power() }')
    # Test Grass Types
    instance = TypeFactory.get_grassFire()
    print(f'Type: { instance.get_type() }, Power: { instance.get_power() }')
    instance = TypeFactory.get_grassWater()
    print(f'Type: { instance.get_type() }, Power: { instance.get_power() }')
    instance = TypeFactory.get_grassGrass()
    print(f'Type: { instance.get_type() }, Power: { instance.get_power() }')

if __name__ == '__main__':
    main()
