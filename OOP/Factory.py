# Design Patterns

'''
The factory pattern comes under the creational patterns list category.
It provides one of the best ways to create an object. In factory pattern,
objects are created without exposing the logic to client and referring to the
newly created object using a common interface. When a user calls a method such
that we pass in a string and the return value as a new object is implemented
through factory method. The type of object used in factory method is determined
by string which is passed through method.
'''
import math


class Button(object):
    html = ''
    def get(self):
        return self.html

class Image(Button):
    html = "<img></img>"

class Input(Button):
    html = "<input></input>"

class Flash(Button):
    html = "<obj></obj>"

class ButtonFactory():
    def create_btn(self, typ):
        target_class = typ.capitalize()
        return globals()[target_class]()


class Pizza:
    def __init__(self, ingredients, radius=5):
        self.ingredients = ingredients
        self.radius = radius

    def __repr__(self):
        return (f'Pizza({self.ingredients}, '
                f'{ self.radius })')

    # Class methods
    @classmethod
    def margherita(cls):
        return cls(['Mozzarella', 'Tomatoes'])

    @classmethod
    def prosciutto(cls):
        return cls(['Mozzarella', 'Tomatoes', 'Ham'])

    # Instance methods
    def area(self):
        return self.circle_area(self.radius)

    # Static methods
    @staticmethod
    def circle_area(radius):
        return (radius ** 2) * math.pi


def main():
    # Button Factory
    print('Button Factory...')
    btn_obj = ButtonFactory()
    btn = ['image', 'input', 'flash']
    for b in btn: print(btn_obj.create_btn(b).get())
    # Pizza Factory
    print('Pizza Factory...')
    print(f'Pizza.margherita(): { Pizza.margherita() }')
    print(f'Pizza.prosciutto(): { Pizza.prosciutto() }')
    p1 = Pizza(['Mozzarella', 'Tomatoes'], 4)
    print(f'p1: {p1}')
    print(f'p1.area(): {p1.area()}')
    print(f'Pizza.circle_area(4): {Pizza.circle_area(4)}')


if __name__ == '__main__':
    main()
