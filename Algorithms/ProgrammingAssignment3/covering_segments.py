from sys import stdin
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')

def optimal_points(segments):
    points = []
    compl = []
    # write your code here
    for s in segments:
        points.append((s.start, s.end))
    
    #Sort the right most value by least to greatest
    points.sort(key=lambda x: x[1])

    while points:
        curr_point = points[0][1]
        compl.append(curr_point)

        points = [point for point in points if point[0] > curr_point]
        
    return compl


if __name__ == '__main__':
    input = stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    print(*points)
