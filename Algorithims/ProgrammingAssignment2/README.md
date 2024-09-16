# Algorithims

These programs based on efficient algorithms can solve the same problem billions of times faster than programs based on naïve algorithms. I learned how to estimate the running time and memory of an algorithm without even implementing it. Armed with this knowledge, I am able to compare various algorithms, select the most efficient ones, and finally implement them.

## Learning Objectives
- Estimate the running time of an algorithm
- Practice implementing efficient solutions
- Practice solving programming challenges
- Implement programs that are several orders of magnitude faster than straightforward programs

## Table of Contents
- [Fibonacci Sequence](#fibonacci-sequence)
- [Fibonacci Last Digit](#fibonacci-last-digit)
- [Greatest Common Divisor](#greatest-common-divisor)
- [Least Common Divisor](#least-common-divisor)
- [Huge Fibonacci Number](#Huge-Fibonacci-Number)

## Fibonacci Sequence
### Fibonacci Sequence Problem
Compute the n-th Fibonacci number.
#### Input: 
An integer n
#### Output: 
n-th Fibonacci number

![image](https://github.com/user-attachments/assets/1d62e443-a811-493b-b531-f7c519ea47f1)


---


Input format. The first line contains an integer n. The next line contains n non-negative integers a1,...,an (separated by spaces).
Output format. The maximum pairwise product.
Constraints. 2 ≤ n ≤ 2 · 105; 0 ≤ a1 ,...,an ≤ 2 · 105

### Samples:
#### Sample 1
Input:
```python
3
```

Output:
```python
2
```

#### Sample 2
Input:
```python
10
```

Output:
```python
55
```

### Full Code Breakdown
#### Full Code
```python
lis = []

def fibonacci_number(n):
    if n == 0:
        return 0
    if n == 1:
        return 1

    lis = [0] * (n+1)
    lis[0] = 0
    lis[1] = 1

    for i in range(2, n+1):
        lis[i] = lis[i-1]+lis[i-2]

    return lis[n]


if __name__ == '__main__':
    input_n = int(input())
    print(fibonacci_number(input_n))
```

#### Function fibonacci_number(n)
The input of this function is n where n is an integer <br>
The output of this function is the fibonacci number that is related to that nth integer
```python
    if n == 0:
        return 0
    if n == 1:
        return 1
```
These are the first test cases, where if n = 0 or 1, it will return the respective nth values. These are all the values we need for to get the fibonacci numbers after.
```python
    lis = [0] * (n+1)
    lis[0] = 0
    lis[1] = 1
```
Using the list above, we will be storing the values of the nth resursive sum inside a list. It can solve the problem and the other method is the recursive method but I went with this one. 
```python
    for i in range(2, n+1):
        lis[i] = lis[i-1]+lis[i-2]

    return lis[n]
```
This then goes through all the possible values n value from 2 to n+1 and at each i value between that range it adds the value before and the second value before. 
<br>
For example, if the value was 5, it would iterate like follows:
```python
Input: 5
i = 2: lis[2] = lis[1] + lis[0] = 1 + 0 = 1
i = 3: lis[3] = lis[2] + lis[1] = 1 + 1 = 2
i = 4: lis[4] = lis[3] + lis[2] = 3
i = 5: lis[5] = lis[4] + lis[3] = 5
```
<br>
After, it returns the value at the nth spot in the list of possible fibonacci numbers
<br>
The Big O of this function is O(n) where n is the number you are trying to get

## Huge Fibonacci Number
### Huge Fibonacci Number Problem
Compute the n-th Fibonacci number modulo m.
#### Input: 
An integer n and a sequence of n non-negative integers.
#### Output: 
The maximum value that can be obtained by multiplying two different elements from the sequence.

---


Input format. The first line contains an integer n. The next line contains n non-negative integers a1,...,an (separated by spaces).
Output format. The maximum pairwise product.
Constraints. 2 ≤ n ≤ 2 · 105; 0 ≤ a1 ,...,an ≤ 2 · 105

### Samples:
#### Sample 1
Input:
```python
3
1 2 3
```

Output:
```python
6
```

#### Sample 2
Input:
```python
10
7 5 14 2 8 8 10 1 2 3
```

Output:
```python
140
```
