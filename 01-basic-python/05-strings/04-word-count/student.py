# Write your code here
def word_count(string):
    if string == "":
        return 0
    words = string.split(" ")
    return len(words)
