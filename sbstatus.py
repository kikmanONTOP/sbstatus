# discord.py 1.7.3
import discord
from discord.ext import commands

token = input("your discord acc token: ")
command_prefix = '!'

intents = discord.Intents.all()
client = commands.Bot(command_prefix=command_prefix, case_insensitive=True, intents=intents, self_bot=True)
status = input("status name: ")
@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name=status))
    print("working real!!!!!")
client.run(token, bot=False)