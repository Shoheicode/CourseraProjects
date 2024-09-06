from sys import stdin


def min_refills(distance, tank, stops):
    # Add the destination as a final "stop"
    stops.append(distance)
    
    num_refills = 0
    current_position = 0
    current_refill = 0
    
    while current_position < distance:
        # Find the farthest reachable stop
        last_refill = current_position
        
        # Move to the farthest stop within the car's fuel range
        while current_refill < len(stops) and stops[current_refill] - last_refill <= tank:
            current_position = stops[current_refill]
            current_refill += 1
            
        # If no station is reachable from the last refill point, return impossible
        if current_position == last_refill:
            return -1  # Impossible to reach the destination
            
        # If we haven't reached the destination, increment the number of refills
        if current_position < d:
            num_refills += 1
    
    return num_refills


if __name__ == '__main__':
    #d, m, _, *stops = map(int, stdin.read().split())
    d = int(input())
    m = int(input())
    _ = int(input())
    stops = []
    for i in range(_):
        stops.append(int(input()))
    print(min_refills(d, m, stops))
