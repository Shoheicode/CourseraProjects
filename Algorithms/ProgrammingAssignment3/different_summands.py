def optimal_summands(n):
    summands = []
    currentS = 1

    while n > 0:
        if n-currentS > currentS:
            summands.append(currentS)
            n-= currentS
            currentS+=1
            
        else:
            summands.append(n)
            break

    # write your code here
    return summands


if __name__ == '__main__':
    n = int(input())
    summands = optimal_summands(n)
    print(len(summands))
    print(*summands)
