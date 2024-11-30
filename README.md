# study-discord-bot

study discord bot

## インストール

~~~bash
poetry install
~~~

## .envの作成

リポジトリ直下に.envファイルを作成し、トークンとチャンネルIDを指定する

~~~bash
DISCORD_BOT_TOKEN=your_discord_bot_token
DISCORD_CHANNEL_ID=123456789012345678
~~~

## 実行

~~~bash
poetry run python -m study_discord_bot
~~~

画像とメッセージが指定したチャンネルの送信される。
