def sort(list):
    for i in range(1, len(list)):
        key = list[i]
        j = i-1
        while list[j] > key and j >= 0:
            """   a = list[j]
              list[j] = list[j+1] """
            list[j+1] = list[j]
            j = j-1
        list[j + 1] = key

    return list


if __name__ == "__main__":
    print(sort([1, 2, 6, 3, 78, 2, 2, 2, 5, 2, 98, 2, 15, 65, 13, 1, 374, 1]))
