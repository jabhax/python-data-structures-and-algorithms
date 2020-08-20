''' SORTING '''
import time
import random


# Bubble Sort
# Time Complexity:
#   - Best: Ω(n)
#   - Avg: 	Θ(n^2)
#   - Worst: O(n^2)
# Space Complexity: O(1) Worst-Case
def bubble_sort(a):
    for i in range(len(a)):
        for j in range(len(a)-1):
            if a[j] > a[j+1]:
                temp = a[i]
                a[i] = a[j]
                a[j] = temp
    return a


# Selection Sort:
# Time Complexity:
#   - Best: Ω(n^2)
#   - Avg: 	Θ(n^2)
#   - Worst: O(n^2)
# Space Complexity: O(1) Worst-Case
def selection_sort(a):
    for i in range(len(a)):
        min = i
        for j in range(i+1, len(a)):
            if a[j] < a[min]:
                min = j
                temp = a[i]
                a[i] = a[min]
                a[min] = temp
    return a


# Insertion Sort:
# Time Complexity:
#   - Best: Ω(n)
#   - Avg: 	Θ(n^2)
#   - Worst: O(n^2)
# Space Complexity: O(1) Worst-Case
def insertion_sort(a):
    for i in range(1, len(a)):
        temp = a[i]
        j = i-1
        while j >= 0 and a[j] > temp:
            a[j+1] = a[j]
            j -= 1
        a[j+1] = temp
    return a


# Merge Sort:
# Time Complexity:
#   - Best: Ω(n log(n))
#   - Avg: 	Θ(n log(n))
#   - Worst: O(n log(n))
# Space Complexity: O(n) Worst-Case
def merge_sort(a):
    # Base Case:
    # If array has 0 or 1 element, then it is already sorted so return
    if len(a) < 2:
        return a
    # Otherwise, array has more than 1 element and needs to be sorted.
    # Split array in half to get left and right halves.
    mid = int(len(a) / 2)
    left = merge_sort(a[:mid])
    right = merge_sort(a[mid:])
    # Create pointers that will traverse the left & right halves, and a third
    # pointer for updating the main array in-space as (l, r, and k).
    # Iterate until EITHER left OR right has been fully traveresed.
    l, r, k = 0, 0, 0
    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            a[k] = left[l]
            l += 1
        else:
            a[k] = right[r]
            r += 1
        k += 1
    # Get remaining sorted elems from LEFT in case it was not fully traversed.
    while l < len(left):
        a[k] = left[l]
        l += 1
        k += 1
    # Get remaining sorted elems from RIGHT in case it was not fully traversed.
    while r < len(right):
        a[k] = right[r]
        r += 1
        k += 1
    # Finally, return the updated array in its sorted order.
    return a


# Quick Sort:
# Time Complexity: O()
#   - Best: Ω(n log(n))
#   - Avg: 	Θ(n log(n))
#   - Worst: O(n^2)
# Space Complexity: O(log(n)) Worst-Case
def quick_sort(a):
    low, high, pi = 0, len(a), 0
    if high < 2:  # Base case
        return a
    # All other cases
    for i in range(1, high):  # Partitioning loop
        if a[i] <= a[low]:
            pi += 1
            temp = a[i]
            a[i] = a[pi]
            a[pi] = temp
    temp = a[low]
    a[low] = a[pi]
    a[pi] = temp
    left = quick_sort(a[low:pi])
    right = quick_sort(a[pi+1:high])
    a = left + [a[pi]] + right
    return a


# Helper function for calculating end-time from start-time using time.time()
def _et(start_time, tr=8):
    end_time = round(time.time()-start_time, tr)
    start_time = time.time()
    return end_time


def main():
    # Test Bubble Sort Implementation
    unsorted = [3, 8, 1, 5, 7, 0, 2, 9, 6, 4]
    st = time.time()
    print(f'Original Unsorted: {unsorted}\n'
          f'Bubble Sort: {bubble_sort(unsorted)}\n'
          f'Time for Bubble Sort: {_et(st)}s\n')
    # Test Selection Sort Implementation
    random.shuffle(unsorted)
    st = time.time()
    print(f'Original Unsorted: {unsorted}\n'
          f'Selection Sort: {selection_sort(unsorted)}\n'
          f'Time for Selection Sort: {_et(st)}s\n')
    # Test Insertion Sort Implementation
    random.shuffle(unsorted)
    st = time.time()
    print(f'Original Unsorted: {unsorted}\n'
          f'Insertion Sort: {insertion_sort(unsorted)}\n'
          f'Time for Insertion Sort: {_et(st)}s\n')
    # Test Merge Sort Implementation
    random.shuffle(unsorted)
    st = time.time()
    print(f'Original Unsorted: {unsorted}\n'
          f'Merge Sort: {merge_sort(unsorted)}\n'
          f'Time for Merge Sort: {_et(st)}s\n')
    # Test Quick Sort Implementation
    random.shuffle(unsorted)
    st = time.time()
    print(f'Original Unsorted: {unsorted}\n'
          f'Quick Sort: {quick_sort(unsorted)}\n'
          f'Time for Quick Sort: {_et(st)}s')


if __name__ == '__main__':
    main()
