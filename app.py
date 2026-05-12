import os
import discord
from discord.ext import commands
from discord import app_commands

ALLOWED_CHANNELS = [
    1472233895654195284, 1469277900649005087
]

IMAGE_FILE = "standard (1).gif"

intents = discord.Intents.default()
intents.guilds = True
intents.message_content = True

TOKEN = os.environ["DISCORD_TOKEN"]


bot = commands.Bot(command_prefix="!", intents=intents)

@bot.tree.command(
    name="announcement",
    description="Send an announcement embed"
)
@app_commands.describe(
    message="Your announcement message"
)
async def announcement(interaction: discord.Interaction, message: str):
    if not interaction.user.guild_permissions.administrator:
        await interaction.response.send_message("❌ Admin only command.", ephemeral=True)
        return

    if interaction.channel.id not in ALLOWED_CHANNELS:
        await interaction.response.send_message(
            "❌ You cannot use this command here.",
            ephemeral=True,
        )
        return

    embed = discord.Embed(
        title="📢 ANNOUNCEMENT",
        description=f"**```{message}```**",
        color=discord.Color.red(),
    )

    embed.set_footer(
        text=f"By {interaction.user}",
        icon_url=interaction.user.display_avatar.url,
    )

    file = discord.File(IMAGE_FILE, filename="announcement.gif")
    embed.set_image(url="attachment://announcement.gif")

    await interaction.response.send_message(embed=embed, file=file)

@bot.event
async def on_ready():
    try:
        synced = await bot.tree.sync()
        print(f"✅ Synced {len(synced)} command(s) globally")
    except Exception as e:
        print("Sync error:", e)

    print(f"✅ Logged in as {bot.user}")

if __name__ == "__main__":
    bot.run(TOKEN)

