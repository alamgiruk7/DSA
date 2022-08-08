'''
1. When I try to find number 5 in below list using binary search, it doesn't work and returns me -1 index. Why is that?
    numbers = [1,4,6,9,10,5,7]
'''
# Answer: Because this list is not sorted. First it needs to be sorted.


'''
2. Find index of all the occurances of a number from sorted list
    numbers = [1,4,6,9,11,15,15,15,17,21,34,34,56]
    number_to_find = 15  
This should return 5,6,7 as indices containing number 15 in the array
'''


def binarySearch(numbers_list, num_to_find, left_index, right_index):
    mid_index = (left_index + right_index) // 2

    if numbers_list[mid_index] == num_to_find:
        return mid_index
    
    if left_index <= right_index:
        if num_to_find < numbers_list[mid_index]:
            right_index = mid_index - 1
        elif num_to_find > numbers_list[mid_index]:
            left_index = mid_index + 1

        return binarySearch(numbers_list, num_to_find, left_index, right_index)
    else:
        return -1

def find_occurances(numbers_list, num_to_find):
    index = binarySearch(numbers_list, num_to_find,
                         0, len(list_of_numbers) - 1)
    indices = [index]

    # search indices on left side
    i = index - 1
    while i >= 0:
        if numbers_list[i] == num_to_find:
            indices.append(i)
        else:
            break
        i -= 1

    # search indices on right side
    i = index + 1
    while i <= len(numbers_list):
        if numbers_list[i] == num_to_find:
            indices.append(i)
        else: 
            break
        i += 1

    return sorted(indices)


list_of_numbers = [1, 4, 6, 9, 11, 15, 15, 15, 15, 17, 21, 34, 34, 56]
find_num = 15

# index = binarySearch(list_of_numbers, find_num, 0, len(list_of_numbers) - 1)

occur = find_occurances(list_of_numbers, find_num)

print(f"Number found at position: {occur}")