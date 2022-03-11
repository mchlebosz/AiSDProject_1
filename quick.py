import random
import sys
x = 100000
# sys.setrecursionlimit(x)
CONSTANT = 4000


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
            i = i + 1

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


if __name__ == "__main__":
    array = [1, 2, 6, 3, 78, 2, 2, 2,
             5, 2, 98, 2, 15, 65, 13, 1, 374, 1]
    sortLeft(array)
    print(array)
    array = [1, 2, 6, 3, 78, 2, 2, 2,
             5, 2, 98, 2, 15, 65, 13, 1, 374, 1]
    sortRand(array)
    print(array)
