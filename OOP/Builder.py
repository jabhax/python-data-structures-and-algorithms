'''
    Builder Pattern is a unique design pattern which helps in building complex
    object using simple objects and uses an algorithmic approach. This design
    pattern comes under the category of creational pattern. In this design
    pattern, a builder class builds the final object in step-by-step procedure.
    This builder is independent of other objects.

    Advantages of Builder Pattern:
    - It provides clear separation and a unique layer between construction and
      representation of a specified object created by class.
    - It provides better control over construction process of the pattern
      created.
    - It gives the perfect scenario to change the internal representation of
      objects.
'''


class Director():
    ''' Class for directing the building-process of Star objects '''
    __builder = None

    def set_builder(self, builder):
        ''' Sets the main builder object '''
        self.__builder = builder

    def get_star(self):
        ''' Builds the star object using provided builder '''
        star = Star()
        star.set_body(self.__builder.get_body())
        star.set_size(self.__builder.get_size())
        orbit = self.__builder.get_orbit()
        star.set_orbit(orbit)
        for i in range(orbit.planet_capacity):
            star.attach_planet(self.__builder.get_planet(i))
        return star

class Star():
    ''' Star class Implementation '''
    def __init__(self):
        self.__size = None
        self.__body = None
        self.__planets = []
        self.__orbit = 0

    def set_size(self, size):
        self.__size = size

    def set_body(self, body):
        self.__body = body

    def set_orbit(self, orbit):
        self.__orbit = orbit

    def attach_planet(self, planet):
        if len(self.__planets)+1 <= self.__orbit.planet_capacity:
            self.__planets.append(planet)

    def specs(self):
        print(
            f'Body: { self.__body.shape }\n'
            f'Mass: { self.__size.mass }\n'
            f'Radius: { self.__size.radius }\n'
            f'Orbit can support up to { self.__orbit.planet_capacity } planets\n'
            f'Planets:\n    { self.__planets }\n'
        )

class Builder:
    ''' Star Builder Definition/Interface '''
    def get_planet(self, name): pass
    def get_orbit(self): pass
    def get_size(self): pass
    def get_body(self): pass

class SunBuilder(Builder):
    ''' Specific star builder for building Sun-like stars '''
    def get_planet(self, name):
        return Planet(name=name)

    def get_size(self):
        return Size(radius=6000, mass=1.0)

    def get_body(self):
        return Body(shape='round')

    def get_orbit(self):
        return Orbit(7)


class Planet:
    ''' Planet Implementation '''
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'Planet { self.name }'

class Orbit:
    ''' Orbit Implementation '''
    def __init__(self, planet_capacity):
        self.planet_capacity = planet_capacity

class Size:
    ''' Size Implementation '''
    def __init__(self, radius, mass):
        self.radius = radius
        self.mass = mass

class Body:
    ''' Body Implementation '''
    def __init__(self, shape):
        self.shape = shape


def main():
    sun_builder = SunBuilder()
    director = Director()
    # Build a sun
    print('Star: Sun')
    director.set_builder(sun_builder)
    sun = director.get_star()
    sun.specs()


if __name__ == '__main__':
    main()
