''' Merge-Sort on Arrays/Lists '''
import time


# Recursive Mergsort with Iterative Merge
def merge_sort(a):
    if len(a) == 1:
        return a
    mid = int(len(a) / 2)
    # Split Array in into right and left
    return merge(merge_sort(a[:mid]), merge_sort(a[mid:]))


# Iterative Merge
def merge(L, R):
    merged, i, j = [], 0, 0
    while i < len(L) and j < len(R):
        if L[i] < R[j]:
            merged.append(L[i])
            i += 1
        else:
            merged.append(R[j])
            j += 1
    return merged + L[i:] + R[j:]


# Main
def main():
    nums_arr = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]
    print(f'List of Numbers: {nums_arr}')
    start = time.time()
    print(f'Merge Sort: {merge_sort(nums_arr)}')
    print(f'Took [{time.time()-start}s]')


# Call main()
if __name__ == '__main__':
    main()
