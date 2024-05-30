def matching_parentheses(string):
    count = 0
    if len(string) == 0:
        return True
    for char in string:
        if char == "(":
            count += 1
        if char == ")":
            count -= 1
        if count < 0:
            return False
    return count == 0
