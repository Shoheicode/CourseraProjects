from itertools import permutations
from functools import cmp_to_key

def compare(x, y):
    if x+y > y+x:
        return -1
    else:
        return 1

def largest_number(numbers):
    numbers = list(map(str, numbers))

    largest = ""

    sorted_numbers = sorted(numbers, key=cmp_to_key(compare))

    largest = ''.join(sorted_numbers)

    if largest[0] == '0':
        return 0

    return largest


if __name__ == '__main__':
    _ = int(input())
    input_numbers = input().split()
    print(largest_number_naive(input_numbers))
