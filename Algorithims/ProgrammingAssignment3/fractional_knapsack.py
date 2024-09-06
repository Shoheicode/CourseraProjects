from sys import stdin


def optimal_value(capacity, weights, values):
    print("HIHIHIO")
    items = [(values[i], weights[i], values[i] / weights[i]) for i in range(len(values))]
    
    # Sort items by value-to-weight ratio in descending order
    items.sort(key=lambda x: x[2], reverse=True)
    
    total_value = 0.0  # Total value collected in the backpack
    current_weight = 0  # Current weight in the backpack
    
    for value, weight, ratio in items:
        if current_weight + weight <= capacity:
            # If the whole item can be taken, take it
            current_weight += weight
            total_value += value
        else:
            # Take the fraction of the item that fits
            remaining_capacity = capacity - current_weight
            total_value += ratio * remaining_capacity
            break  # The backpack is full
    
    return total_value

if __name__ == "__main__":
    data = list(map(int, stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
