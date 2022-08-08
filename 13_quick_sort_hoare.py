'''QUICK SORT with Hoare Method'''


def swap(a, b, arr):
    if a != b:
        arr[a], arr[b] = arr[b], arr[a]


def partition(elements_list, start, end):
    pivot_index = start
    pivot = elements_list[pivot_index]

    while start < end:
        while start < len(elements_list) and elements_list[start] <= pivot:
            start += 1

        while elements_list[end] > pivot:
            end -= 1

        if start < end:
            swap(start, end, elements_list)

    swap(pivot_index, end, elements_list)

    return end


def quickSort(numbers_list, start, end):
    if start < end:
        pi = partition(numbers_list, start, end)
        quickSort(numbers_list, start, pi - 1)
        quickSort(numbers_list, pi + 1, end)


if __name__ == "__main__":
    elements = [11, 9, 29, 7, 7, 9, 2, 15, 28]
    quickSort(elements, 0, len(elements)-1)
    print(elements)
