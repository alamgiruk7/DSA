'''SHELL SORT'''


def swap(a, b, arr):
    if a != b:
        arr[a], arr[b] = arr[b], arr[a]


def shellSort(arr):
    size = len(arr)
    gap = size // 2

    while gap > 0:
        for i in range(gap, len(arr), gap):
            j = i - gap
            while j >= 0 and arr[i] <= arr[j]:
                if arr[i] == arr[j]:
                    size -= 1
                    del arr[i]
                    continue
                swap(i, j, arr)
                j -= gap
                i -= gap

        gap = gap // 2


if __name__ == '__main__':
    test_cases = [
        [11, 10, 29, 7, 9, 2, 11, 28, 23, 3, 4, 3, 10, 11, 29, 7, 12, 17, 1],
        [3, 7, 9, 11],
        [25, 22, 21, 10],
        [29, 15, 28],
        [],
        [6]
    ]

    for test in test_cases:
        shellSort(test)
        print(test)
