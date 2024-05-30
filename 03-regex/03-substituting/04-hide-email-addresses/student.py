# Write your code here
import re


def hide_email_addresses(string):
    def replace(match):
        word = match.group()

        return "*" * len(word)

    return re.sub(r"[a-zA-Z.0-9]*@[a-zA-Z.0-9]*", replace, string)
