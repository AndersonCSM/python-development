def bubblesort(lista):
    size = len(lista)

    for i in range(size):
        for j in range(size - 1):
            n1 = lista[j]
            n2 = lista[j + 1]

            if n1 > n2:
                lista[j], lista[j + 1] = n2, n1

    return lista


def main():
    nums = [4, 10, 23, 9, 8, 7, 65, 5, 42, 3, 20, 1]

    print(bubblesort(nums))


main()
