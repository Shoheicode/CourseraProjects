# Explanation:
# binary_search_first_occurrence(arr, q):
# The function implements a modified binary search. It keeps track of the first occurrence of 
# q found and continues searching to the left until it is sure that no smaller index contains q.

# Input/Output Handling:
# The input consists of reading the size n of the sorted array 
# 𝑎
# 𝑟
# 𝑟
# arr, the array itself, and the query integer 
# 𝑞
# q.
# The result, which is the index of the first occurrence of 
# 𝑞
# q, is printed. If 
# 𝑞
# q does not appear in the array, -1 is printed.

def binary_search(keys, query):
    # write your code here
    low, high = 0, len(keys) - 1
    result = -1
    while low <= high:
        mid = (low + high) // 2
        if keys[mid] == query:
            result = mid
            high = mid-1
        elif keys[mid] < query:
            low = mid + 1
        else:
            high = mid - 1
    return result


if __name__ == '__main__':
    num_keys = int(input())
    input_keys = list(map(int, input().split()))
    assert len(input_keys) == num_keys

    num_queries = int(input())
    input_queries = list(map(int, input().split()))
    assert len(input_queries) == num_queries

    for q in input_queries:
        print(binary_search(input_keys, q), end=' ')
