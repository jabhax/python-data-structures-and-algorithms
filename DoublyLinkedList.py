''' Doubly-Linked List '''
import time


''' Node Object Implementation '''
class Node:
    # Constructor
    def __init__(self, v):
        self.next = None
        self.prev = None
        self.value = v

class DoublyLinkedList:
    # Constructor
    def __init__(self, v):
        self.head = Node(v)
        self.tail = self.head
        self.length = 1

    # Prepend Implementation
    def prepend(self, v):
        temp = Node(v)
        temp.next = self.head
        self.head.prev = temp
        self.head = temp
        self.length += 1

    # Insert Implementation
    def insert(self, v, i):
        if i >= self.length:
            return
        temp = Node(v)
        curr = self.head
        prev = curr
        pos = 0
        while curr != None:
            if pos == i:
                temp.next = curr
                prev.next = temp
                curr.prev = temp
                temp.prev = prev
                break
            prev = curr
            curr = curr.next
            pos += 1
        self.length += 1

    # Append Implementation
    def append(self, v):
        temp = Node(v)
        temp.prev = self.tail
        self.tail.next = temp
        self.tail = temp
        self.length += 1

    # Remove Implementation
    def remove(self, i):
        if i >= self.length:
            print(f'Invalid index {i}')
            return
        curr = self.head
        prev = curr
        pos = 0
        while curr != None:
            if pos == i:
                curr.next.prev = prev
                prev.next = curr.next
            prev = curr
            curr = curr.next
            pos += 1
        self.length -= 1

    def __str__(self):
        result = []
        curr = self.head
        while curr != None:
            result.append(curr.value)
            curr = curr.next
        return str(result)

# Main
def main():
    # Test Append, Prepend methods
    l = DoublyLinkedList(10)
    print(f'[LinkedList] => Items(size={l.length}): {l}')
    tt = 7 # truncate time decimale places by tt
    for i in range(1, 5):
        # Time how long Append takes
        start = time.time()
        l.append(i * 2)
        end = round(time.time() - start, tt)
        print(f'Took ({end}s): [APPEND ({i * 2})] => Items(size={l.length}): {l}')
        # Time how long Prepend takes
        start = time.time()
        l.prepend(i * 3)
        end = round(time.time() - start, tt)
        print(f'Took ({end}s): [PREPEND ({i * 3})] => Items(size={l.length}): {l}')

    # Test Insert, Remove methods
    for i in range(1, 5):
        # Time how long Insert takes
        start = time.time()
        l.insert(l.length/2, i*10)
        end = round(time.time() - start, tt)
        print(f'Took ({end}s): [INSERT: ({i * 10}, pos: {i})] => Items(size={l.length}): {l}')
        # Time how long Remove takes
        start = time.time()
        l.remove(i)
        end = round(time.time() - start, tt)
        print(f'Took ({end}s): [REMOVE (pos: {i})] => Items(size={l.length}): {l}')


if __name__ == '__main__':
    main()
