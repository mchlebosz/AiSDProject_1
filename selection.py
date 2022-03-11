""" def sort(lista):
    for i in range(len(lista)):
        for j in range(i+1, len(lista)):
            if lista[i] > lista[j]:
                a = lista[i]
                lista[i] = lista[j]
                lista[j] = a
    return lista
 """


def sort(array):
    size = len(array)
    for step in range(size):
        min_i = step
        for i in range(step + 1, size):
            if array[i] < array[min_i]:
                min_i = i
        (array[step], array[min_i]) = (array[min_i], array[step])
    return array


if __name__ == "__main__":
    print(sort([1, 2, 6, 3, 78, 2, 2, 2, 5, 2, 98, 2, 15, 65, 13, 1, 374, 1]))
