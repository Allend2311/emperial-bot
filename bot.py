import discord
from discord.ext import commands
from flask import Flask, request
import threading

# ---------------- CONFIG ----------------
GUILD_ID = 1469038556092829923  # REPLACE WITH YOUR SERVER ID
NOTIFY_ROLE_NAME = "Notify Me"

intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix="!", intents=intents)

# ---------------- FLASK API ----------------
app = Flask(__name__)

@app.route("/subscribe", methods=["POST"])
def subscribe():
    data = request.json
    user_id = data.get("user_id")

    guild = bot.get_guild(GUILD_ID)
    if not guild:
        return {"status": "guild_not_found"}, 400

    member = guild.get_member(int(user_id))
    role = discord.utils.get(guild.roles, name=NOTIFY_ROLE_NAME)

    if member and role:
        bot.loop.create_task(member.add_roles(role))
        return {"status": "ok"}

    return {"status": "error"}, 400


def run_flask():
    app.run(host="0.0.0.0", port=8080)


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")


def start():
    threading.Thread(target=run_flask).start()
    bot.run("YOUR_BOT_TOKEN")


if __name__ == "__main__":
    start()
