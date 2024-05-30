# Write your code here
def keys_with_value(dict, value):
    list = []
    for k, v in dict.items():
        if v == value:
            list.append(k)
    return list
