from qiita_api import fetch_articles

articles = fetch_articles("JavaScript")

print(type(articles))
print(len(articles))

print(articles[0]["title"])