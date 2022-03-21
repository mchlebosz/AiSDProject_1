import random
import sys
#x = 100000
# sys.setrecursionlimit(x)
CONSTANT = 80000


def partition(array, low, high):

    # choose the leftmost element as pivot
    (array[low], array[high]) = (array[high], array[low])
    # send it to the end
    pivot = array[high]

    # pointer for greater element
    i = low - 1

    # traverse through all elements
    # compare each element with pivot
    for j in range(low, high):
        if array[j] <= pivot:
            # if element smaller than pivot is found
            # swap it with the greater element pointed by i
            i += 1

            # swapping element at i with element at j
            (array[i], array[j]) = (array[j], array[i])

    # swap the pivot element with the greater element specified by i
    (array[i + 1], array[high]) = (array[high], array[i + 1])

    # return the position from where partition is done
    return i + 1


def partitionRand(array, low, high):

    # choose the random element as pivot
    randIndex = random.randint(low, high)
    # send it to the end
    (array[randIndex], array[high]) = (array[high], array[randIndex])
    pivot = array[high]

    # pointer for greater element
    i = low - 1

    # traverse through all elements
    # compare each element with pivot
    for j in range(low, high):
        if array[j] <= pivot:
            # if element smaller than pivot is found
            # swap it with the greater element pointed by i
            i = i + 1

            # swapping element at i with element at j
            (array[i], array[j]) = (array[j], array[i])

    # swap the pivot element with the greater element specified by i
    (array[i + 1], array[high]) = (array[high], array[i + 1])

    # return the position from where partition is done
    return i + 1


def sortLeft(array, low=0, high=None):
    sys.setrecursionlimit(max(sys.getrecursionlimit(), len(array)+CONSTANT))
    if high is None:
        high = len(array) - 1
    if low >= high:
        return
    if low < high:
        # find pivot element such that
        # element smaller than pivot are on the left
        # element greater than pivot are on the right
        piv = partition(array, low, high)
        # recursive call on the left of pivot
        sortLeft(array, low, piv - 1)
        # recursive call on the right of pivot
        sortLeft(array, piv + 1, high)


def sortRand(array, low=0, high=None):
    sys.setrecursionlimit(max(sys.getrecursionlimit(), len(array)+CONSTANT))

    if high is None:
        high = len(array) - 1

    if low < high:
        # find pivot element such that
        # element smaller than pivot are on the left
        # element greater than pivot are on the right
        piv = partitionRand(array, low, high)
        # recursive call on the left of pivot
        sortLeft(array, low, piv - 1)
        # recursive call on the right of pivot
        sortLeft(array, piv + 1, high)


def qsort(A, L=0, P=None):

    sys.setrecursionlimit(max(sys.getrecursionlimit(), len(array) + CONSTANT))
    if P == None:
        P = len(A)-1

    x = A[0]
    i = L
    j = P
    while(i < j):
        while(A[i] < x):
            i += 1
        while(A[j] > x):
            j -= 1
        if i <= j:
            A[i], A[j] = A[j], A[i]
            i = i+1
            j = j-1
        if L < j:
            qsort(A, L, j)
        if P > i:
            qsort(A, i, P)
        """
            X to Pivot
            L to najbardziej na lewo
            P na prawo """


def quicksortL(a_list):
    """Hoare partition scheme, see https://en.wikipedia.org/wiki/Quicksort"""
    sys.setrecursionlimit(max(sys.getrecursionlimit(), len(a_list) + CONSTANT))

    def _quicksort(a_list, low, high):
        # must run partition on sections with 2 elements or more
        if low < high:
            p = partition(a_list, low, high)
            _quicksort(a_list, low, p)
            _quicksort(a_list, p+1, high)

    def partition(a_list, low, high):
        pivot = a_list[low]
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
    _quicksort(a_list, 0, len(a_list)-1)
    return a_list


def quicksortR(a_list):
    """Hoare partition scheme, see https://en.wikipedia.org/wiki/Quicksort"""
    sys.setrecursionlimit(max(sys.getrecursionlimit(), len(a_list) + CONSTANT))

    def _quicksort(a_list, low, high):
        # must run partition on sections with 2 elements or more
        if low < high:
            p = partition(a_list, low, high)
            _quicksort(a_list, low, p)
            _quicksort(a_list, p+1, high)

    def partition(a_list, low, high):
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
    _quicksort(a_list, 0, len(a_list)-1)
    return a_list


if __name__ == "__main__":
    array = [1, 2, 6, 3, 78, 2, 2, 2,
             5, 2, 98, 2, 15, 65, 13, 1, 374, 1]

    # quicksortL(array)

    quicksortL(array)
    print(array)
