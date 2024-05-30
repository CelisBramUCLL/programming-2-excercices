from itertools import pairwise


def total_distance(path, distance):
    return sum(distance(i[0], i[1]) for i in pairwise(path))
