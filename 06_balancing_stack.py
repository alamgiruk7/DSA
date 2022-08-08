'''Balanced Stack'''
from collections import deque

def is_balanced(s):
    stack = deque()

    for ch in s:
        if ch == '(' or ch == '{' or ch == '[':
            stack.append(ch)
        elif ch == ')' or ch == '}' or ch == ']':
            if len(stack) == 0:
                return False
            elif not is_match(ch, stack.pop()):
                return False

    return len(stack) == 0

def is_match(ch1, ch2):
    match_case = {
        ')': '(',
        '}': '{',
        ']': '['
    }

    return match_case[ch1] == ch2


if __name__ == '__main__':
    print(is_balanced("((a+b))"))
    print(is_balanced("([{a+b]})"))
    print(is_balanced("{[a+b]}"))
    print(is_balanced("{}{}"))
    