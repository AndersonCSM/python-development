def quicksort(arr):

    if len(arr) < 2:
        return arr  # nao a o que ordenar
    else:
        pivo = arr[0]
        arr_min = [i for i in arr[1:] if i <= pivo]  # array com valores menores que o pivo ja pulado o pivo de indice 1
        arr_max = [i for i in arr[1:] if i > pivo]  # array com valores maiores que o pivo ja pulado o pivo de indice 1

        return quicksort(arr_min) + [pivo] + quicksort(arr_max)  # chamada recursiva


def main():
    nums = [4, 10, 23, 9, 8, 7, 65, 5, 42, 3, 20, 1]

    print(quicksort(nums))


main()
