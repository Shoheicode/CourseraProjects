# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next in "([{":
            # Process opening bracket, write your code here
            opening_brackets_stack.append(next)

        if next in ")]}":
            # Process closing bracket, write your code here
            if opening_brackets_stack.pop() == '(' and next == ")":
                break
            elif opening_brackets_stack.pop() == '(' and next == ")":
                break
            elif opening_brackets_stack.pop() == '(' and next == ")":
                break
            else:
                return False
    
    if opening_brackets_stack.count != 0:
        return False
    return True


def main():
    text = input()
    mismatch = find_mismatch(text)
    print(mismatch)
    # Printing answer, write your code here


if __name__ == "__main__":
    main()
