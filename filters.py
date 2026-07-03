from datetime import datetime, timedelta


def filter_recent_articles(articles, days=7):

    recent_articles = []

    now = datetime.now()

    for article in articles:

        created_at = datetime.fromisoformat(
            article["created_at"].replace("Z", "+00:00")
        )

        if now - created_at.replace(tzinfo=None) <= timedelta(days=days):
            recent_articles.append(article)

    return recent_articles

def filter_stock_articles(articles, min_stocks=2):

    filtered_articles = []

    for article in articles:
        if article["stocks_count"] >= min_stocks:
            filtered_articles.append(article)

    return filtered_articles