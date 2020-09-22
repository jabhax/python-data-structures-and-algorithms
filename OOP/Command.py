# Design Patterns

'''
Command Pattern adds a level of abstraction between actions and includes an
object, which invokes these such actions.
'''


class Command:
    '''
    Client creates a command object that includes a list of commands to be
    executed. The command object created implements a specific interface.
    '''
    def __init__(self, cmd, *args):
        self._cmd = cmd
        self._args = args

    def __call__(self, *args):
        return self._cmd(*self._args + args)

def demo(a, b, c):
    ''' Demo command function '''
    print(f'a: {a}')
    print(f'b: {b}')
    print(f'c: {c}')

def main():
    cmd = Command(dir, __builtins__)
    print(f'cmd: { cmd }')
    print(f'cmd(): { cmd() }')
    cmd = Command(demo, 1, 2)
    cmd(3)


if __name__ == '__main__':
    main()
