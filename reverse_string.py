''' Reversing a String '''
import time


# Reverse a string iteratively using last index as starting point.
# Stor in array and re-join back into a string.
def reverse(s):
    return ''.join([s[end] for end in range(len(s)-1, -1, -1)])


# Recursively reverse a string, by taking first element and appending it to
# the end of the <string> - <first element>
def reverse_recursive(s):
    return s[-1] if len(s) < 2 else reverse_recursive(s[1:]) + s[0]


def main():
    input = 'Hi, my name is Justin!'
    print(f'Input String: {input}\n')
    # Time how long it takes to reverse iteratively.
    start = time.time()
    print(f'Reverse String (Loop): {reverse(input)}')
    print(f'Took [{time.time()-start}s]\n')
    # Time how long it takes to reverse recursively.
    start = time.time()
    print(f'Reverse String (Rec): {reverse_recursive(input)}')
    print(f'Took [{time.time()-start}s]')


if __name__ == '__main__':
    main()
