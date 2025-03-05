import discord
from discord.ext import tasks, commands
from datetime import datetime, timezone, timedelta
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Retrieve token and channel ID securely
CHANNEL_ID = int(os.getenv("CHANNEL_ID"))
BOT_TOKEN = os.getenv("BOT_TOKEN")

# Set your event date and time (UTC)
EVENT_DATE = datetime(2025, 4, 14, 0, 0, 0, tzinfo=timezone.utc)
# Initialize bot with necessary intents
intents = discord.Intents.default()
intents.messages = True

bot = commands.Bot(command_prefix='!', intents=intents)

# Runs when the bot is ready
@bot.event
async def on_ready():
    print(f'✅ Logged in as {bot.user.name}')
    
    # Sync slash commands
    try:
        synced = await bot.tree.sync()
        print(f"✅ Synced {len(synced)} slash commands.")
    except Exception as e:
        print(f"❌ Failed to sync commands: {e}")

    daily_reminder.start()  # Start the scheduled reminder task

# Task that runs every day at 8 PM UTC
@tasks.loop(hours=24)
async def daily_reminder():
    now = datetime.now(timezone.utc)
    reminder_time = now.replace(hour=20, minute=0, second=0, microsecond=0)

    # If it's past 8 PM today, schedule for tomorrow
    if now > reminder_time:
        reminder_time += timedelta(days=1)

    await discord.utils.sleep_until(reminder_time)  # Wait until the correct time

    time_left = EVENT_DATE - datetime.now(timezone.utc)
    if time_left > timedelta(0):
        days = time_left.days
        hours = (time_left.seconds // 3600) % 24
        minutes = (time_left.seconds // 60) % 60
        countdown_message = (f"📢 Countdown Reminder: {days} days, {hours} hours, "
                             f"and {minutes} minutes until the event!")
        channel = bot.get_channel(CHANNEL_ID)
        if channel:
            await channel.send(countdown_message)
    else:
        channel = bot.get_channel(CHANNEL_ID)
        if channel:
            await channel.send("🚀 The event has started!")
        daily_reminder.cancel()  # Stop the task after the event

# Slash Command: Check the Countdown
@bot.tree.command(name="countdown", description="Check the countdown to the event.")
async def countdown(interaction: discord.Interaction):
    time_left = EVENT_DATE - datetime.now(timezone.utc)

    if time_left > timedelta(0):
        days = time_left.days
        hours = (time_left.seconds // 3600) % 24
        minutes = (time_left.seconds // 60) % 60
        await interaction.response.send_message(f"🕒 Time left until the DAUG 2025: {days} days, {hours} hours, and {minutes} minutes.")
    else:
        await interaction.response.send_message("🚀 The event has already started!")

# Run the bot
bot.run(BOT_TOKEN)