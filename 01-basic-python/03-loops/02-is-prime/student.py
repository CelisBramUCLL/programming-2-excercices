# Write your code here
def is_prime(n):
    if n == 0 or n == 1:
        return False
    for x in range(2, n):
        if n % x == 0:
            return False
    return True
