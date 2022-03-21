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
    if P is None:
        P = len(A)-1
    x = A[0]
    i = L
    j = P
    while(i < j):
        while(A[i] < x):
            i += 1
        while(A[j] > x):
            j -= 1
        if i < j:
            A[i], A[j] = A[j], A[i]
    if i > j:
        qsort(A, L, j)
        qsort(A, i, P)
        """
            X to Pivot
            L to najbardziej na lewo
            P na prawo """


def quick_sort_rnd(data, left=0, right=None):
    if right is None:
        right = len(data) - 1
    if left >= right:
        return
    #pivot = data[rand() % (right - left + 1) + left]
    pivot = data[0]

    i = left
    j = right

    while i <= j:
        while data[i] < pivot:
            i += 1
        while data[j] > pivot:
            j -= 1

        if i <= j:
            data[i], data[j] = data[j], data[i]
            i += 1
            j -= 1
        else:
            break

    if j > left:
        quick_sort_rnd(data, left, j)
    if i < right:
        quick_sort_rnd(data, i, right)


if __name__ == "__main__":
    """ array = [1, 2, 6, 3, 78, 2, 2, 2,
             5, 2, 98, 2, 15, 65, 13, 1, 374, 1]
    sortLeft(array)
    print(array) """
    array = [1, 2, 6, 3, 78, 2, 2, 2,
             5, 2, 98, 2, 15, 65, 13, 1, 374, 1]
    quick_sort_rnd(array)
    print(array)
