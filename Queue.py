''' Queue Implementation '''
from LinkedList import Node


class Queue:
    # Constructor
    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0

    # Peek Implementation
    def peek(self):
        return self.first

    # Enqueue Implementation
    def enqueue(self, v):
        temp = Node(v)
        if self.is_empty():
            self.first = temp
            self.last = temp
        else:
            self.last.next = temp
            self.last = temp
        self.length += 1

    # Dequeue Implementation
    def dequeue(self):
        if self.is_empty():
            print('Cannot dequeue empty queue.')
            return None
        if self.first == self.last:
            self.last = None
        old_first = self.first
        self.first = self.first.next
        self.length -= 1
        return old_first

    # Implement boolean check whether the Queue is empty.
    def is_empty(self):
        return (self.first is None and self.length == 0)

    # Override default str() representation.
    def __str__(self):
        result = []
        curr = self.first
        while curr is not None:
            result.append(curr.value)
            curr = curr.next
        return str(result)


# Main
def main():
    q = Queue()
    # Test Enqueue Implementation
    print('Enqueueing...')
    for i in range(1, 6):
        q.enqueue(i*2)
        print(q)
    # Test Dequeue Implementation
    print('Dequeueing...')
    for i in range(6):
        q.dequeue()
        print(q)


# Call main()
if __name__ == '__main__':
    main()
