#Uses python3
import sys
import math
import heapq

def minimum_distance(x, y):
    n = len(x)
    result = 0.
    
    #write your code here
    return result


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    x = data[1::2]
    y = data[2::2]
    print(x)
    print(y)
    print("{0:.9f}".format(minimum_distance(x, y)))
