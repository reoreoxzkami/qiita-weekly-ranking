from markdown_generator import generate_markdown
from qiita_api import fetch_articles
from filters import filter_recent_articles
from filters import (
    filter_recent_articles,
    filter_stock_articles,
)
from ranking import sort_by_likes

articles = fetch_articles("JavaScript")

print(f"取得件数 : {len(articles)}")

articles = filter_recent_articles(articles)

print(f"7日以内 : {len(articles)}")

articles = filter_stock_articles(articles)

print(f"ストック2以上 : {len(articles)}")

articles = sort_by_likes(articles)

print()
print("=== ランキング ===")

for rank, article in enumerate(articles, start=1):
    print(
        f"{rank}位 | "
        f"{article['likes_count']}いいね | "
        f"{article['stocks_count']}ストック"
    )
    print(article["title"])
    print("-" * 50)

markdown = generate_markdown(
    articles,
    "JavaScript",
)

with open("ranking.md", "w", encoding="utf-8") as f:
    f.write(markdown)

print("ranking.md を作成しました！")