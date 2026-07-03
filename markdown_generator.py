from datetime import datetime, timedelta


def generate_markdown(articles, tag):
    today = datetime.now().date()
    week_ago = today - timedelta(days=7)

    lines = []

    # タイトル
    lines.append(f"# 【{tag}】Qiita 週間いいね数ランキング【自動更新】")
    lines.append("")

    # 集計情報
    lines.append(f"最終更新日: {today}")
    lines.append("")
    lines.append("## 集計について")
    lines.append("")
    lines.append(f"集計期間: {week_ago} ～ {today}")
    lines.append(f"対象タグ: {tag}")
    lines.append("")
    lines.append("条件:")
    lines.append("- 過去7日以内")
    lines.append("- ストック数が2以上")
    lines.append("- いいね数順")
    lines.append("")
    lines.append("---")
    lines.append("")

    # ランキング
    for rank, article in enumerate(articles, start=1):

        created = article["created_at"][:10]

        tag_names = [tag["name"] for tag in article["tags"]]
        tags = " / ".join(tag_names)

        lines.append(f"## {rank}位: [{article['title']}]({article['url']})")
        lines.append("")
        lines.append(f"**タグ**")
        lines.append(tags)
        lines.append("")
        lines.append(f"👍 {article['likes_count']} いいね")
        lines.append(f"⭐ {article['stocks_count']} ストック")
        lines.append("")
        lines.append(f"👤 投稿者: @{article['user']['id']}")
        lines.append(f"📅 投稿日: {created}")
        lines.append("")
        lines.append("---")
        lines.append("")

    return "\n".join(lines)