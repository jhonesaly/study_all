import requests
import re

def validate_author_and_title(author, title):
    query = author + ' ' + title
    query = query.replace(' ', '+')
    response = requests.get(f'https://www.google.com/search?q={query}')
    result = re.search('<div class="r"><a href="(.*?)"', response.text)
    if result:
        link = result.group(1)
        response = requests.get(link)
        if author.lower() in response.text.lower() and title.lower() in response.text.lower():
            return True
    return False