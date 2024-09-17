# Explanation:
# Candidate Selection (Boyer-Moore Voting Algorithm):

# Traverse through the array while maintaining a candidate and a counter.
# - If the counter is zero, set the current element as the candidate.
# - If the element matches the candidate, increment the counter. Otherwise, decrement the counter.
# Verification:
# - After the first pass, check if the candidate actually occurs more than 𝑛/2 times by counting its occurrences.
# 
# Input/Output Handling:
# - Input consists of reading the size 𝑛 of the sequence and the sequence itself.
# - The result is 1 if there is a majority element, otherwise 0.


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
