from sys import stdin


def min_refills(distance, tank, stops):
    stops.append(distance)
    num_refills = 0
    current_pos =0
    last_refill_pos = 0

    for i in range(len(stops)):
        print("HIHIHI")
        print("STOP AT :",i, " " ,  stops[i])
        print("TANK SIZE", tank)
        print("Current pos: ", current_pos)
        # Check if it's possible to reach the next stop or destination
        if stops[i] - current_pos > tank:
            # If we can't reach the next stop after the last refill, refill at the last stop
            if current_pos == last_refill_pos:
                # If the car is at the same place where it last refilled and can't reach the next stop, it's impossible
                return -1  # Impossible to reach the destination
            # Refill at the last stop
            num_refills += 1
            last_refill_pos = current_pos
        
        # Move the car to the next stop
        current_pos = stops[i]
    # write your code here
    return num_refills


if __name__ == '__main__':
    d, m, _, *stops = map(int, stdin.read().split())
    print(min_refills(d, m, stops))
