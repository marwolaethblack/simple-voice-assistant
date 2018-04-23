import requests
from bs4 import BeautifulSoup
import re


def searchDDG(query):
    response = requests.get("https://duckduckgo.com/html/?q=" + query)
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup.find("a", class_="result__snippet").get_text()
def searchGoogle(query):
    response = requests.get("https://www.google.com/search?q=" + query + "&hl=en")
    soup = BeautifulSoup(response.text, 'html.parser')
    content = soup.find("td", id="rhs_block").get_text(separator=" ")
    #Remove the People also search for field
    return truncate_string(content, "People also search for")

def truncate_string(string, substring):
    end = string.find(substring)
    return string[0:end]

