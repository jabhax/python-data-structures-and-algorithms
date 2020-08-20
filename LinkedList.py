''' Singly-Linked List '''
import time


# Node Object Implementation
class Node:
    # Constructor
    def __init__(self, v):
        self.next = None
        self.value = v


# Linked-List Implementation
class LinkedList:
    # Constructor
    def __init__(self, v):
        self.head = Node(v)
        self.tail = self.head
        self.length = 1

    # Prepend Implementation
    def prepend(self, v):
        temp = Node(v)
        temp.next = self.head
        self.head = temp
        self.length += 1

    # Insert Implementation
    def insert(self, v, i):
        if i >= self.length:
            return
        temp, curr, pos = Node(v), self.head, 0
        prev = curr
        while curr is not None:
            if pos == i:
                temp.next = curr
                prev.next = temp
                break
            prev = curr
            curr = curr.next
            pos += 1
        self.length += 1

    # Append Implementation
    def append(self, v):
        temp = Node(v)
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
        while curr is not None:
            # Remove by skipping over the pointer to the next node.
            if pos == i:
                prev.next = curr.next
            prev = curr
            curr = curr.next
            pos += 1
        self.length -= 1

    # Reverse Implementation
    def reverse(self):
        curr = self.head
        next = curr.next
        self.tail = self.head
        while (next is not None):
            # swap pointers
            temp = next.next
            next.next = curr
            # shift to next items
            curr = next
            next = temp
        self.head.next = None
        self.head = curr

    # Override Default str() Representation
    def __str__(self):
        result = []
        curr = self.head
        while curr is not None:
            result.append(curr.value)
            curr = curr.next
        return str(result)


# Main
def main():
    # Test Append, Prepend methods
    LL = LinkedList(10)
    print(f'[LinkedList] => Items(size={LL.length}): {LL}')
    tt = 10  # truncate time decimale places by tt
    for i in range(1, 5):
        start = time.time()
        LL.append(i * 2)
        end = round(time.time() - start, tt)
        print(f'Took ({end}s): [APPEND ({i * 2})] '
              f'=> Items(size={LL.length}): {LL}')

        start = time.time()
        LL.prepend(i * 3)
        end = round(time.time() - start, tt)
        print(f'Took ({end}s): [PREPEND ({i * 3})] '
              f'=> Items(size={LL.length}): {LL}')

    # Test Insert, Remove methods
    for i in range(1, 5):
        start = time.time()
        LL.insert(LL.length/2, i*10)
        end = round(time.time() - start, tt)
        print(f'Took ({end}s): [INSERT: ({i * 10}, pos: {i})]'
              f' => Items(size={LL.length}): {LL}')

        start = time.time()
        LL.remove(i)
        end = round(time.time() - start, tt)
        print(f'Took ({end}s): [REMOVE (pos: {i})] '
              f'=> Items(size={LL.length}): {LL}')

    # Test Reverse method
    start = time.time()
    LL.reverse()
    end = round(time.time() - start, tt)
    print(f'Took ({end}s): [REVERSED] Items(size={LL.length}): {LL}')


# Call main()
if __name__ == '__main__':
    main()
