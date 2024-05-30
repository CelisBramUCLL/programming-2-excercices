def closest(points, target_point):
    return min(
        points,
        key=lambda point: (
            ((target_point[0] - point[0]) ** 2 + (target_point[1] - point[1]) ** 2)
            ** 0.5
        ),
    )
