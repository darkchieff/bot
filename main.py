import os
import discord
from discord.ext import commands
from flask import Flask
from threading import Thread

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

RADIO_URL = "http://stream.live.vc.bbcmedia.co.uk/bbc_radio_one"

app = Flask('')

@app.route('/')
def home():
    return "I'm alive!"

def run():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

@bot.command()
async def join(ctx):
    if ctx.author.voice:
        channel = ctx.author.voice.channel
        await channel.connect()
        await ctx.send(f"Joined {channel}")
    else:
        await ctx.send("You're not in a voice channel.")

@bot.command()
async def play(ctx):
    if ctx.voice_client is None:
        await ctx.invoke(bot.get_command('join'))

    vc = ctx.voice_client
    if vc.is_playing():
        vc.stop()

    vc.play(discord.FFmpegPCMAudio(RADIO_URL, executable="./ffmpeg"), after=lambda e: print(f'Player error: {e}') if e else None)
    await ctx.send("Now playing BBC Radio 1")

@bot.command()
async def stop(ctx):
    if ctx.voice_client:
        await ctx.voice_client.disconnect()
        await ctx.send("Stopped and left the channel.")
    else:
        await ctx.send("I'm not in a voice channel.")

keep_alive()
bot.run(os.environ['YOUR_BOT_TOKEN'])
