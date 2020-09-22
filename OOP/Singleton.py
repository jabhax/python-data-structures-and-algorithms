# Design Patterns

'''
The Singleton Pattern restricts the instantiation of a class to one object.
It is a type of creational pattern and involves only one class to create
methods and specified objects. It provides a global point of access to the
instance created.
'''
class Singleton:
    __instance = None

    @staticmethod
    def getInstance():
        ''' Static getter for Singleton instance property '''
        if Singleton.__instance is None: Singleton()
        return Singleton.__instance

    def __init__(self):
        ''' Virtually private constructor '''
        if Singleton.__instance:
            raise Exception('Can\'t create more than one singleton class!')
        else:
            Singleton.__instance = self

def main():
    # The number of instances of Singletion() that are created remain the same
    # and there is no difference in the objects listed in output.
    s, num_inits = Singleton(), 5
    print(f's = Single(), {s}')
    for i in range(num_inits):
        s = Singleton.getInstance()
        print(f's = Singleton.getInstance(), {s}')
    try:
        x = Singleton()
        y = Singleton()
        print('This could should not be reached!')
    except Exception as e:
        print(f'Attempted to call Singleton() again. Encountered excepted error:\n{e}')


if __name__ == '__main__':
    main()
