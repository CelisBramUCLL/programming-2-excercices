def indices_of(xs, condition):
    result = []
    for i in range(0, len(xs)):
        if condition(xs[i]):
            result.append(i)

    return result
