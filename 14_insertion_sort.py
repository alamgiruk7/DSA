'''INSERTION SORT'''


def swap(a, b, arr):
    if a != b:
        arr[a], arr[b] = arr[b], arr[a]


def insertionSort(arr):
    for i in range(1, len(arr)):
        j = i - 1
        while j >= 0:
            if arr[j] >= arr[i]:
                swap(i, j, arr)
                j -= 1
                i -= 1
            else:
                break


def median(arr):
    if len(arr) % 2 == 0:
        a = len(arr) // 2
        b = (len(arr) // 2) - 1

        return (arr[a] + arr[b]) / 2
    else:
        return arr[len(arr) // 2]


if __name__ == "__main__":
    elements = [11, 10, 29, 7, 9, 2, 15, 28]
    insertionSort(elements)
    print(elements)
    print(len(elements))
    print("Median:", median(elements))
