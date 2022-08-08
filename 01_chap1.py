'''Binary Search and Complexity Analysis'''


cards = [13, 23, 52, 5, 12, 6, 11, 35, 42]

query = 12

expected_output = 4

def locate_card(cards, query):
    position = 0

    while position < len(cards):
        if cards[position] == query:
            return position
        
        position += 1

    return -1


test1 = {
    'input': {
        'cards': [13, 23, 52, 5, 12, 6, 11, 35, 42],
        'query': 12
    },
    'output': 4
}

tests = list()

tests.append(test1)

# 2. Normal Test Case
tests.append(
    {
        'input': {
        'cards': [13, 23, 52, 12, 5, 6, 11, 35, 42],
        'query': 12
        },
        'output': 3
    }
)
# 3. Repetitive query number in list
tests.append(
    {
        'input': {
        'cards': [13, 23, 52, 43, 12, 12, 12, 5, 6, 11, 35, 42],
        'query': 12
        },
        'output': 4
    }
)
# 4. Repetitive numbers in list
tests.append(
    {
        'input': {
        'cards': [13, 23, 52, 12, 5, 6, 6, 6, 6, 11, 35, 42],
        'query': 11
        },
        'output': 9
    }
)
# 5. If there is only one element in the list
tests.append(
    {
        'input': {
        'cards': [12],
        'query': 12
        },
        'output': 0
    }
)
# 6. If the list is empty
tests.append(
    {
        'input': {
        'cards': [],
        'query': 12
        },
        'output': -1
    }
)
# 7. If the query number is not present in the list
tests.append(
    {
        'input': {
        'cards': [13, 23, 52, 12, 5, 6, 6, 6, 6, 11, 35, 42],
        'query': 51
        },
        'output': -1
    }
)


for i, test in enumerate(tests):
    result = locate_card(test['input']['cards'], test['input']['query'])
    if (result == test['output']):
        print(f"Test {i+1} Passed.")
    else: 
        print(f"Test {i+1} Failed.")

