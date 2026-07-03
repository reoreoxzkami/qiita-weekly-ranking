# Qiita Weekly Ranking Generator

Qiita APIを利用して、タグごとの週間いいねランキングをMarkdown形式で生成するツールです。

## 機能

- 指定タグの記事を取得
- 過去7日以内の記事に絞り込み
- ストック数でフィルタリング
- いいね数順にランキング
- Markdownを自動生成

## 使用方法

```bash
pip install -r requirements.txt
python main.py
```

生成されたランキングは `output/ranking.md` に保存されます。

## 開発支援のお知らせ

認知度向上のため支援寄付を行っています。ご協力頂いた方にはこのリポジトリ説明欄にてご希望のお名前を表記いたします
  寄付リンク:https://buy.stripe.com/dRmaEX2pqcnGbGygLA6Vq0g
