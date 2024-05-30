# Write your code here
def target_sum(ns, target):
    for x in range(0, len(ns) - 1):
        for y in range(0, len(ns)):
            if x != y and ns[x] + ns[y] == target:
                return True
    return False
