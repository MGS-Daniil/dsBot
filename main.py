from webserver import keep_alive
import time
import os
import sys
import json
import discord
from discord.utils import get
from discord.ext import commands
bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())

@bot.command()
async def pip(ctx):
  await ctx.send("Python?")

keep_alive()
bot.run(os.getenv("TOKEN"))