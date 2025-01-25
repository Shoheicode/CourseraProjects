def change(money):
    # Calculates Change through greedy algorithm
    change = 0
    # Calculate the number of 10s, 5s, and 1s
    while money >= 10:
        money = money - 10
        change += 1

    while money >= 5:
        money = money - 5
        change += 1

    while money >= 1:
        money = money - 1
        change += 1

    return change


if __name__ == "__main__":
    m = int(input())
    print(change(m))
