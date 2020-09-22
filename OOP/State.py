# Design Patterns

'''
The State Pattern provides a module for state machines, which are implemented
using subclasses, derived from a specified state machine class. The methods are
state independent and cause transitions declared using decorators, etc.
'''

class ComputerState():
    name, allowed = 'state', []

    def __str__(self):
        return self.name

    def change(self, state):
        ''' Change current state to a different state '''
        if state.name not in self.allowed:
            print(f'({self}) to ({state.name}) not possible!')
        else:
            print(f'state: {self} => state: {state.name}')
            self.__class__ = state

class Off(ComputerState):
    ''' Computer in the off State; Default state'''
    name, allowed = 'OFF', ['ON']

class On(ComputerState):
    ''' Computer in powered on state; working state!'''
    name, allowed = 'ON', ['OFF', 'SUSPEND', 'HIBERNATE']

class Suspend(ComputerState):
    ''' Computer in suspended state after being changed on '''
    name, allowed = 'SUSPEND', ['ON']

class Hibernate(ComputerState):
    ''' Computer in hibernation state after being powered on '''
    name, allowed = 'HIBERNATE', ['ON']

class Computer(object):
    ''' Computer Class Implementation '''
    def __init__(self, model='Razer'):
        self.model = model
        self.state = Off()

    def change(self, state):
        ''' Call change(state) from ComputerStates Impl '''
        self.state.change(state)


def main():
    computer = Computer()
    state_map = {
        'ON': [On],
        'ON-S': [On, Suspend],
        'ON-H': [On, Hibernate],
        'ON-OFF': [On, Off],
        'ON-OFF-ON': [On, Off, On],
        'ON-OFF-ON-S-H-ON-OFF': [On, Off, On, Suspend, Hibernate, On, Off]
    }
    for path, states in state_map.items():
        print(f'Path: [{path}]')
        for state in states:
            computer.change(state)


if __name__ == '__main__':
    main()
