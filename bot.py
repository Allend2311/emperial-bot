import discord
from discord.ext import commands
from flask import Flask
import threading
import os
bot.run(os.getenv("DISCORD_TOKEN"))
# Flask app for keep-alive
app = Flask('')

# ---------------- FLASK KEEP-ALIVE ----------------
app = Flask(__name__)

@app.route('/')
def home():
@@ -16,14 +16,51 @@

def keep_alive():
    t = threading.Thread(target=run)
    t.daemon = True
    t.start()

# Call keep_alive before bot runs
# Start keep-alive
keep_alive()

# ---------------- BOT SETUP ----------------
intents = discord.Intents.default()
intents.guilds = True
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

# ---------------- SLASH COMMAND ----------------
@bot.tree.command(name="announce", description="Send announcement to Empire")
async def announce(interaction: discord.Interaction):
    guild = interaction.guild
    role = discord.utils.get(guild.roles, name="Empire")
    channel = bot.get_channel(1469277900649005087)  # Announcement channel ID

    if role and channel:
        await channel.send(
            f"{role.mention}\n"
            "**📢 ANNOUNCEMENT 📢**\n"
            "```\n"
            "WHAT: WE HAVE A MEETING\n"
            "WHEN: SATURDAY (10:00 PM)\n"
            "ALL FAMILIA IMPERIAL REQUIRED\n"
            "THANK YOU!\n"
            "```"
        )
        await interaction.response.send_message("✅ Announcement sent!", ephemeral=True)
    else:
        await interaction.response.send_message("❌ Role or channel not found.", ephemeral=True)

# ---------------- READY EVENT ----------------
@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")
    try:
        synced = await bot.tree.sync()
        print(f"Slash commands synced: {len(synced)}")
    except Exception as e:
        print(f"Sync error: {e}")

# ---------------- RUN BOT ----------------
bot.run(os.getenv("DISCORD_TOKEN"))
