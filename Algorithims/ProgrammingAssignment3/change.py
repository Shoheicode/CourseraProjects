def change(money):
    change = 0
    while money >= 10:
        money = money-10
        change +=1

    while money >= 5:
        money = money -5
        change+=1
    
    while money >= 1:
        money = money -1
        change +=1

    return change


if __name__ == '__main__':
    m = int(input())
    print(change(m))
