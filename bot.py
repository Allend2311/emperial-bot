import discord
from discord.ext import commands
from flask import Flask
import threading
import os
bot.run(os.getenv("DISCORD_TOKEN"))
# Flask app for keep-alive
app = Flask('')

@app.route('/')
def home():
    return "Bot is alive!"

def run():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = threading.Thread(target=run)
    t.start()

# Call keep_alive before bot runs
keep_alive()

# ---------------- BOT SETUP ----------------
intents = discord.Intents.default()
intents.guilds = True
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)
