# Write your code here
def make_path(parts):
    string = ""
    for i in range(0, len(parts)):
        string += parts[i]
        if i != len(parts) - 1:
            string += "/"
    return string
