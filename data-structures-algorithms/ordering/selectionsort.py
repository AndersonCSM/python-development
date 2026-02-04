def get_min(arr):
    min = arr[0]
    min_idx = 0

    for i in range(1, len(arr)):
        if arr[i] < min:
            min = arr[i]
            min_idx = i

    return min_idx


def selectionsort(arr):
    aux = []

    for i in range(len(arr)):
        min = get_min(arr)

        aux.append(arr.pop(min))

    return aux


def main():
    arr = [1, 4, 10, 20, 2, 30, 9, 6, 7]

    print(selectionsort(arr))


main()
