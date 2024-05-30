# Write your code here
def create_dictionary(keys, values):
    dict = {}
    for i in range(0, len(keys)):
        dict[keys[i]] = values[i]
    return dict
