# Design Patterns

'''
String serialization is the process of writing a state of object into a byte
stream. In python, the “pickle” library is used for enabling serialization.
This module includes a powerful algorithm for serializing and de-serializing a
Python object structure. “Pickling” is the process of converting Python object
hierarchy into byte stream and “unpickling” is the reverse procedure.
'''

import pickle


def serialize(s):
    return pickle.dumps(s)

def deserialize(s):
    return pickle.loads(s)


def main():
    some_object = {
        'grades': { 'Alice': 89, 'Bob': 72, 'Charles': 87 },
        'cars': { 'BMW': 'White', 'Toyota': 'Red', 'Honda': 'Yellow' },
        'pokemon': { 'Charizard': 'FIRE', 'Blastoise': 'WATER', 'Venusaur': 'GRASS' }
    }
    print(f'serialize(some_object): {serialize(some_object)}')
    print(f'deserialize(serialize(some_object)): {deserialize(serialize(some_object))}')


if __name__ == '__main__':
    main()
