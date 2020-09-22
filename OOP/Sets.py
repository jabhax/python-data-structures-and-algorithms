# Sets in Python
import sys
from ast import literal_eval


def union(s1, s2):
    return s1 | s2

def intersection(s1, s2):
    return s1 & s2

def superset(s1, s2):
    # Checks if s1 is a superset of s2
    return (s1 > s2)

def subset(s1, s2):
    # Checks if s1 is a subset of s2
    return (s1 < s2)

def same(s1, s2):
    # Checks if s1 is the same set as s2
    return (s1 == s2)

def difference(s1, s2):
    # Check difference between s1 and s2
    return s1 - s2

def disjointed(s1, s2):
    return s1.isdisjoint(s2)

def clear_set(s):
    s.clear()

def pset(s):
    print(f'Set: {s}')


def main():
    # Create some Sets
    s1, s2 = set(range(1, 4)), set(range(4, 9))
    print(f'S1:{s1}')
    print(f'S2:{s2}')
    # Union Sets
    s3 = union(s1, s2)
    print(f'S3:{s3} is the union of S1:{s1} and S2:{s2}')
    # Intersection Sets
    s4 = intersection(s1, s2)
    print(f'S4:{s4}\n')
    # Set Relations (superset, subset, same)
    print(f'S3:{s3} is a superset of S1:{s1} => {superset(s3, s1)}')
    print(f'S1:{s1} is a subset of S3:{s3} => {subset(s1, s3)}')
    print(f'set(range(1,9)) {set(range(1, 9))} is the same as S3 {s3} => '
          f'{same(set(range(1, 9)), s3)}\n')
    # Set Difference
    s5 = difference(s1, s2)
    print(f'S5:{s5} is the difference between S1:{s1} and S2:{s2}\n')
    # Disjointed
    print(f'S1:{s1} is disjointed from S2:{s2} => {disjointed(s1, s2)}')
    disjointed(s1, s2)
    # Clear Set
    clear_set(s5)
    print(f'S5:{s5} after being cleared')


if __name__ == '__main__':
    main()
