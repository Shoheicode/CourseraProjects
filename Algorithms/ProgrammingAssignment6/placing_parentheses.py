def evaluate(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        assert False

def min_and_max(i, j, operators, min_val, max_val):
    min_value = float('inf')
    max_value = float('-inf')

    for k in range(i, j):
        op = operators[k]
        a = evaluate(max_val[i][k], max_val[k + 1][j], op)
        b = evaluate(max_val[i][k], min_val[k + 1][j], op)
        c = evaluate(min_val[i][k], max_val[k + 1][j], op)
        d = evaluate(min_val[i][k], min_val[k + 1][j], op)

        min_value = min(min_value, a, b, c, d)
        max_value = max(max_value, a, b, c, d)

    return min_value, max_value

def maximum_value(dataset):
    digits = []
    operators = []

    # Split the input into digits and operators
    for i, char in enumerate(dataset):
        if i % 2 == 0:
            digits.append(int(char))
        else:
            operators.append(char)

    n = len(digits)
    min_val = [[0] * n for _ in range(n)]
    max_val = [[0] * n for _ in range(n)]

    # Base case: single digits
    for i in range(n):
        min_val[i][i] = digits[i]
        max_val[i][i] = digits[i]

    # Fill the DP tables
    for s in range(1, n):  # s is the length of the subexpression
        for i in range(n - s):
            j = i + s
            min_val[i][j], max_val[i][j] = min_and_max(i, j, operators, min_val, max_val)

    # The result is the maximum value for the entire expression
    return max_val[0][n - 1]


if __name__ == "__main__":
    print(maximum_value(input()))
