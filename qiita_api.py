import requests

from config import BASE_URL, PER_PAGE


def fetch_articles(tag=None):

    print(tag)

    url = f"{BASE_URL}/items?per_page={PER_PAGE}"

    response = requests.get(url)

    return response.json()