def max_pairwise_product(numbers):
    n = len(numbers)
    max_product = 0
    max = 0
    maxIndex = 0
    
    for first in range(n):
        if max < numbers[first]:
            maxIndex = first
            max = numbers[first]

    numbers[maxIndex] = numbers[n-1]
    numbers[n-1] = max

    max = 0
    maxIndex = 0

    for second in range(n-1):
        if max < numbers[second]:
            maxIndex = second
            max = numbers[second]

    numbers[maxIndex] = numbers[n-2]
    numbers[n-2] = max

    return numbers[n-1]*numbers[n-2]


if __name__ == '__main__':
    _ = int(input())
    input_numbers = list(map(int, input().split()))
    print(max_pairwise_product(input_numbers))
