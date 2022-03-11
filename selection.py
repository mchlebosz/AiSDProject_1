def sort(lista):
    for i in range(len(lista)):
        for j in range(i+1, len(lista)):
            if lista[i] > lista[j]:
                a = lista[i]
                lista[i] = lista[j]
                lista[j] = a
    return lista


if __name__ == "__main__":
    print(sort([1, 2, 6, 3, 78, 2, 2, 2, 5, 2, 98, 2, 15, 65, 13, 1, 374, 1]))
