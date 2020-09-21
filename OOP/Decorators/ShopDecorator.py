import six
from abc import ABCMeta


@six.add_metaclass(ABCMeta)
class AbstractItem(object):
    def get_cost(self): pass
    def get_parts(self): pass
    def get_tax(self): return self.get_cost() * 0.1


class ConcreteItem(AbstractItem):
    def get_cost(self):
        return 1.00

    def get_parts(self):
        return 'ABC Item'

    def __repr__(self):
        return (f'Item\n'
                f'  - Parts: {self.get_parts()}\n'
                f'  - Cost: {self.get_cost()}\n')


@six.add_metaclass(ABCMeta)
class AbstractItemDecorator(AbstractItem):
    def __init__(self, decorated_item):
        self._decorated_item = decorated_item

    def get_cost(self):
        return self._decorated_item.get_cost()

    def get_parts(self):
        return self._decorated_item.get_parts()

    def __repr__(self):
        tax = f'{self.get_tax():.2f}'
        return (f'Item\n'
                f'  - Parts: {self.get_parts()}\n'
                f'  - Cost: {self.get_cost()}\n'
                f'  - Sales Tax: {tax} \n')


class PartA(AbstractItemDecorator):
    def __init__(self, decorated_item):
        AbstractItemDecorator.__init__(self, decorated_item)

    def get_cost(self):
        return self._decorated_item.get_cost()

    def get_parts(self):
        return f'{self._decorated_item.get_parts()}, Part A'


class PartB(AbstractItemDecorator):
    def __init__(self, decorated_item):
        AbstractItemDecorator.__init__(self, decorated_item)

    def get_cost(self):
        return self._decorated_item.get_cost() + 0.25

    def get_parts(self):
        return f'{self._decorated_item.get_parts()}, Part B'


class PartC(AbstractItemDecorator):
    def __init__(self, decorated_item):
        AbstractItemDecorator.__init__(self, decorated_item)

    def get_cost(self):
        return self._decorated_item.get_cost() + 0.75

    def get_parts(self):
        return f'{self._decorated_item.get_parts()}, Part C'
