def sort(list, gaps=[100894, 44842, 19930, 8858, 3837, 1750, 701, 301, 132, 57, 23, 10, 4, 1]):
    size = len(list)
    gap = 10
    while gap > 0:
        for i in range(gap, size):
            zaczep = list[i]
            j = i

            while j >= gap and list[j-gap] > zaczep:
                list[j] = list[j-gap]
                j -= gap
            list[j] = zaczep
        gap -= 1
    return list


if __name__ == "__main__":
    print(sort([1, 2, 6, 3, 78, 2, 2, 2, 5, 2, 98, 2, 15, 65, 13, 1, 374, 1]))
