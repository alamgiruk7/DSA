def bubbleSort(num_list):
    size = len(num_list)
    for i in range(size-1):
        swap = False
        for j in range(size-1-i):
            if num_list[j] > num_list[j+1]:
                num_list[j], num_list[j+1] = num_list[j+1], num_list[j]
                swap = True
        if not swap:
            break


list_of_numbers = [5, 2, 51, 52, 32, 55, 12, 252, 51,
                   122, 1423, 24, 41, 59, 65, 77, 42, 52, 412, 999]

bubbleSort(list_of_numbers)
print(list_of_numbers)
