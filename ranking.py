def sort_by_likes(articles):
    return sorted(
        articles,
        key=lambda article: article["likes_count"],
        reverse=True,
    )