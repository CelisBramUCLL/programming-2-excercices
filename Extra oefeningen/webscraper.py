import requests
import re


def extract_urls(url):
    response = requests.get(url)
    print(response.text)

    matches = re.findall("https?:\/\/[^\s<>]+\.(?:jpg|png|jpeg)", response.text)

    for match in matches:
        print((match))


extract_urls("https://soundcloud.com")
