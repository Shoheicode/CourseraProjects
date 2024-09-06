# python3
from collections import deque

def max_sliding_window_naive(sequence, m):
    n = len(sequence)
    if n * m == 0:
        return []
    
    # Deque to store indices of elements in the current window
    deq = deque()
    max_vals = []
    
    for i in range(n):
        # Remove elements not within the sliding window
        if deq and deq[0] < i - m + 1:
            deq.popleft()
        
        # Maintain elements in decreasing order in the deque
        while deq and sequence[deq[-1]] <= sequence[i]:
            deq.pop()
        
        # Add the current element index to the deque
        deq.append(i)
        
        # The front of the deque is the index of the maximum element in the current window
        if i >= m - 1:
            max_vals.append(sequence[deq[0]])
    
    return max_vals

if __name__ == '__main__':
    n = int(input())
    input_sequence = [int(i) for i in input().split()]
    assert len(input_sequence) == n
    window_size = int(input())

    print(*max_sliding_window_naive(input_sequence, window_size))

