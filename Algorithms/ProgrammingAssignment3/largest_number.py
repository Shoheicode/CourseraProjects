from itertools import permutations


def largest_number(numbers):
    numbers = list(map(str, numbers))

    numbers.sort(reverse=True)

    largest = 0

    for i in numbers:


    return largest


if __name__ == '__main__':
    _ = int(input())
    input_numbers = input().split()
    print(largest_number(input_numbers))
