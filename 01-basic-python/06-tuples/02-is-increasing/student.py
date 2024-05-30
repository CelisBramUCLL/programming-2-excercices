# Write your code here
def is_increasing(ns):
    ms = ns[1:]
    xs = list(zip(ms, ns))

    for i in range(0, len(xs)):
        if xs[i][0] < xs[i][1]:
            return False
    return True
