# Write your code here
def add_indices(xs):
    ys = []
    for i in range(0, len(xs)):
        ys.append(i)

    return list(zip(ys, xs))
