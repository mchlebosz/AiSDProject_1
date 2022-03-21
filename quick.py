import random
import sys
#x = 100000
# sys.setrecursionlimit(x)
CONSTANT = 80000


def sortLeft(a_list):
    # Setting Recursion size
    sys.setrecursionlimit(max(sys.getrecursionlimit(), len(a_list) + CONSTANT))

    def partition(a_list, low, high):
        # left pivot
        pivot = a_list[low]
        while True:
            # continously checking for wrong elements which we swap
            while a_list[low] < pivot:
                low += 1
            while a_list[high] > pivot:
                high -= 1
            # if we are over all indices stop
            if low >= high:
                return high
            # else we swap elements
            a_list[low], a_list[high] = a_list[high], a_list[low]
            # and decrease gap between pointers
            low += 1
            high -= 1

    def quicksort(a_list, low, high):
        # must run partition on sections with 2 elements or more
        # while left pointer < right pointer
        if low < high:
            # we do partition and returning pivot
            p = partition(a_list, low, high)
            quicksort(a_list, low, p)
            quicksort(a_list, p+1, high)
    # we start quicksort with 0 and len - 1
    quicksort(a_list, 0, len(a_list)-1)
    return a_list


def sortRand(a_list):
    sys.setrecursionlimit(max(sys.getrecursionlimit(), len(a_list) + CONSTANT))

    def partition(a_list, low, high):
        # Random pivot
        pivot = a_list[random.randint(low, high)]
        while True:
            while a_list[low] < pivot:
                low += 1
            while a_list[high] > pivot:
                high -= 1
            if low >= high:
                return high
            a_list[low], a_list[high] = a_list[high], a_list[low]
            low += 1
            high -= 1

    def quicksort(a_list, low, high):
        # must run partition on sections with 2 elements or more
        if low < high:
            p = partition(a_list, low, high)
            quicksort(a_list, low, p)
            quicksort(a_list, p+1, high)

    quicksort(a_list, 0, len(a_list)-1)
    return a_list


if __name__ == "__main__":
    array = [1, 2, 6, 3, 78, 2, 2, 2,
             5, 2, 98, 2, 15, 65, 13, 1, 374, 1]

    # quicksortL(array)
    sortRand2(array)
    # quicksortL(array)
    print(array)
