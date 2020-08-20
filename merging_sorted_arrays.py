''' Merging Sorted Arrays '''
import time

# Merge Two Sorted Arrays into a single Merged-Array, while preserving order.
# Sorts in increasing order.
def merge_sorted_arrays(a1, a2, duplicates=True):
    merged, n, i, j = [], (len(a1) + len(a2)), 0, 0
    for _ in range(n-1):
        if a1[i] < a2[j]:
            merged.append(a1[i])
            i += 1
        elif a1[i] > a2[j]:
            merged.append(a2[j])
            j += 1
        else:
            if duplicates:
                merged.append(a1[i])
            i += 1
    return merged


def main():
    sorted_1 = [0, 3, 4, 8, 9, 15, 18, 21, 27, 31]
    sorted_2 = [-40, -22, -13, -10, -4, -1 , 0, 6, 11, 24, 30]
    print(f'Array 1: {sorted_1}\nArray 2: {sorted_2}')
    # Time how long merging takes.
    start = time.time()
    print(f'Merged output 1 (Duplicates): {merge_sorted_arrays(sorted_1, sorted_2)}')
    print(f'Merged output 2 (No Duplicates): {merge_sorted_arrays(sorted_1, sorted_2, duplicates=False)}')
    print(f'Took [{time.time()-start}s]')

if __name__ == '__main__':
    main()
