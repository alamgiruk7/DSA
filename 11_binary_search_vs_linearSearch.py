'''Binary vs Linear Search Algorithm'''
from test_time import calc_time

@calc_time
def linearSearch(num_list, value):
    for i, elem in enumerate(num_list):
        if elem == value:
            return i

    return -1


@calc_time
def binarySearch(num_list, value):
    first_index = 0
    last_index = len(num_list) - 1
    mid_index = 0

    while first_index <= last_index:
        mid_index = (first_index + last_index) // 2
        mid_number = num_list[mid_index]

        if mid_number == value:
            return mid_index

        if mid_number < value:
            first_index = mid_index + 1
        else:
            last_index = mid_index - 1

    return -1


if __name__ == '__main__':
    mylist = [*range(100001)]

    number_to_find = 99999

    index1 = binarySearch(mylist, number_to_find)
    print(f"Number found at index {index1} using Binary Search.")

    index = linearSearch(mylist, number_to_find)
    print(f"Number found at index {index} using Linear Search.")
