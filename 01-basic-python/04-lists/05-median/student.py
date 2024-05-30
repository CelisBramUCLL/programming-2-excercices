# Write your code here
def median(ns):
    ns = sorted(ns)
    if len(ns) % 2 == 0:
        return (ns[len(ns) // 2] + ns[len(ns) // 2 - 1]) / 2
    else:
        return ns[len(ns) // 2]
