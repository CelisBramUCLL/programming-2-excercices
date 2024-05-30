# Write your code here
import re


def scrape_email_addresses(string):
    return re.findall(r"[a-zA-Z.0-9]*@[a-zA-Z.0-9]*", string)
