import requests

from config import BASE_URL, PER_PAGE


def fetch_articles(tag=None):

    if tag:
        url = f"{BASE_URL}/items?query=tag:{tag}&per_page={PER_PAGE}"
    else:
        url = f"{BASE_URL}/items?per_page={PER_PAGE}"

    print("URL:", url)

    response = requests.get(url)

    print("Status:", response.status_code)
    # print("Response:", response.text)

    return response.json()