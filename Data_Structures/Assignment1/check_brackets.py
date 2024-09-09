# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    index = 0
    for i, next in enumerate(text):
        index +=1
        if next in "([{":
            # Process opening bracket, write your code here
            opening_brackets_stack.append((next, index))

        if next in ")]}":
            if len(opening_brackets_stack) == 0:
                print(index)
                return False
            val, pos = opening_brackets_stack.pop()
            # Process closing bracket, write your code here
            if val == '(' and next == ")":
                continue
            elif val == '[' and next == "]":
                continue
            elif val == '{' and next == "}":
                continue
            else:
                print(index)
                return False
    
    if len(opening_brackets_stack) != 0:
        _, pos = opening_brackets_stack[0]
        print(pos)
        return False
    return True


def main():
    text = input()
    mismatch = find_mismatch(text)
    if mismatch:
        print("Success")
    
    # Printing answer, write your code here


if __name__ == "__main__":
    main()
