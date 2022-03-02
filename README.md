# twitter_bot
<h2>はじめに</h2>

知り合いに頼まれて作成しました。  
が、Twitterは自動の"いいね"を禁止してるらしいです。(完成後に知りました)  
せっかく作ったのでここに供養します。

<h2>概要</h2>

このスクリプトは以下の機能を定期実行します。

- 指定したワードを含むツイートへのいいね(機能1)
- 片思いフォロワーへのフォロー(機能2)
- フォローしてくれないアカウントのフォロー解除(機能3)

※ 各機能のオン、オフや実行間隔、いいね数、フォロー数等は指定できます。

<h2>実行に必要な準備</h2>

1. TwitterAPIの利用申請
2. 実行環境の構築(Python)
3. 設定ファイルの作成(JSON)

<h3>1.TwitterAPIの利用申請</h3>

こちらから。
https://developer.twitter.com/en/docs/twitter-api

<h3>2.実行環境の構築</h3>

基本的なPython環境を構築後、以下のコマンドでライブラリを追加して下さい。

```
pip install requests requests_oauthlib
```

<h3>3.設定ファイルの作成</h3>

新規で"settings.json"というファイルを作成後、以下の構成で必要な内容を記述して下さい。

```
{
  "twitter": {
    "consumer_key": 発行されたconsumer key,
    "consumer_secret": 発行されたconsumerconsumer secret,
    "access_token": 発行されたconsumeraccess token,
    "access_token_secret": 発行されたconsumeraccess token secret
  },
  "bot": {
    "interval_min": 定期実行の間隔(分),
    "favorite": {
      "enable": 機能1の実行の有無(true:実行する false:実行しない),
      "max_count": 実行ごとのいいねの最大数,
      "words": [
        検索ワード(上位ほど優先的に検索に利用される)
      ]
    },
    "create_friendships": {
      "enable": 機能2の実行の有無(true:実行する false:実行しない),
      "max_count": 実行ごとの新規フォローの最大数
    },
    "destroy_friendships": {
      "enable": 機能3の実行の有無(true:実行する false:実行しない),
      "max_count": 実行ごとのフォロー解除の最大数
    }
  }
}
```
設定ファイルのサンプル

```
{
  "twitter": {
    "consumer_key": "xxxxxxxxxxxxxxxxxxxxxxxxxx",
    "consumer_secret": "xxxxxxxxxxxxxxxxxxxxxxxxxx",
    "access_token": "xxxxxxxxxxxxxxxxxxxxxxxxxx",
    "access_token_secret": "xxxxxxxxxxxxxxxxxxxxxxxxxx"
  },
  "bot": {
    "interval_min": 120,
    "favorite": {
      "enable": true,
      "max_count": 20,
      "words": [
        "#BTC",
        "ビットコイン",
      ]
    },
    "create_friendships": {
      "enable": true,
      "max_count": 10
    },
    "destroy_friendships": {
      "enable": true,
      "max_count": 10
    }
  }
}
```

<h2>実行方法</h2>

以下のコマンドを実行でOKです。

```
python run.py
```
