# Design Patterns

'''
The Strategy Pattern is a type of behavioral pattern. The main goal of Strategy
Pattern is to enable client to choose from different algorithms or procedures
to complete the specified task. Different algorithms can be swapped in and out
without any complications for the mentioned task. And this pattern can be used
to improve flexibility when external resources are accessed.
'''

import types


class Strategy:
    def __init__(self, func=None):
        self.name = 'Strategy 1'
        if func:
            self.execute = types.MethodType(func, self)

    def execute(self):
        print(f'{self.name}')


def algoX(self):
    print(f'{self.name}:  Algorithm X')

def algoY(self):
    print(f'{self.name}: Algorithm Y')

def main():
    s1 = Strategy()
    s2 = Strategy(algoX)
    s2.name = 'Strategy 2'
    s3 = Strategy(algoY)
    s3.name = 'Strategy 3'
    s1.execute()
    s2.execute()
    s3.execute()


if __name__ == '__main__':
    main()
