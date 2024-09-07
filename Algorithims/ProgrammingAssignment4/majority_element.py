def majority_element_naive(elements):
    candidate = None
    count = 0
    for num in elements:
        if count == 0:
            candidate = num
        count += 1 if num == candidate else -1

    # Step 2: Verify if candidate is majority
    if elements.count(candidate) > len(elements) // 2:
        return 1
    else:
        return 0


if __name__ == '__main__':
    input_n = int(input())
    input_elements = list(map(int, input().split()))
    assert len(input_elements) == input_n
    print(majority_element_naive(input_elements))
