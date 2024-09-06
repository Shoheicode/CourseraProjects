def max_pairwise_product(numbers):
    n = len(numbers)
    
    # Find the index of the largest element
    index = 0
    for i in range(1, n):
        if numbers[i] > numbers[index]:
            index = i
    # Swap the largest element with the last element
    numbers[index], numbers[n - 1] = numbers[n - 1], numbers[index]
    
    # Find the index of the second largest element
    index = 0
    for i in range(1, n - 1):
        if numbers[i] > numbers[index]:
            index = i
    # Swap the second largest element with the second last element
    numbers[index], numbers[n - 2] = numbers[n - 2], numbers[index]
    
    # Return the product of the two largest elements
    return numbers[n - 1] * numbers[n - 2]


if __name__ == '__main__':
    _ = int(input())
    input_numbers = list(map(int, input().split()))
    print(max_pairwise_product(input_numbers))
