import os

import discord
from discord.ext import commands
from dotenv import load_dotenv

# .envファイルから環境変数を読み込む
load_dotenv()

# Botのトークンを設定
TOKEN = os.getenv("DISCORD_BOT_TOKEN")
CHANNEL_ID = int(os.getenv("DISCORD_CHANNEL_ID"))

# Botの初期化
intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name}")

    # 送信したい画像のパスとメッセージ
    image_path = "ailab_icon.png"  # 画像ファイルのパス
    message_content = "こちらが画像です！"

    # チャンネルを取得して画像とメッセージを送信
    channel = bot.get_channel(CHANNEL_ID)
    if channel:
        with open(image_path, "rb") as img:
            await channel.send(content=message_content, file=discord.File(img))
    else:
        print("チャンネルが見つかりません。")

    # Botを終了（不要であれば削除）
    await bot.close()


# Botを実行
bot.run(TOKEN)
