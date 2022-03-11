def sort(list):
    size = len(list)
    gap = size//2
    while gap > 0:
        for i in range(gap, size):
            zaczep = list[i]
            j = i

            while j >= gap and list[j-gap] > zaczep:
                list[j] = list[j-gap]
                j -= gap
            list[j] = zaczep
        gap = gap//2
    return list


if __name__ == "__main__":
    print(sort([1, 2, 6, 3, 78, 2, 2, 2, 5, 2, 98, 2, 15, 65, 13, 1, 374, 1]))
