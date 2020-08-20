''' Stack Implementation '''
from LinkedList import Node


class Stack:
    def __init__(self):
        self.top = None
        self.bottom = None
        self.length = 0

    def peek(self):
        return self.top

    def push(self, v):
        temp = Node(v)
        if self.top:
            temp.next = self.top
            self.top = temp
        else:
            self.top = temp
            self.bottom = temp
        self.length += 1

    def pop(self):
        if self.is_empty():
            print('Cannot pop from empty stack.')
            return None
        if self.top == self.bottom:
            self.bottom = None
        old_top = self.top
        self.top = self.top.next
        self.length -= 1
        return old_top

    def is_empty(self):
        return(self.top is None and self.length == 0)

    def __str__(self):
        result, curr = [], self.top
        while curr is not None:
            result.append(curr.value)
            curr = curr.next
        return str(result)


def main():
    s = Stack()
    # Test Push Implementation
    print('Pushing to stack...')
    for i in range(1, 6):
        s.push(i*2)
        print(s)
    print('Popping from stack...')
    # Test Pop Implementation
    for i in range(6):
        s.pop()
        print(s)


if __name__ == '__main__':
    main()
