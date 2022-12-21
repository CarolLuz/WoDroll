import os
import discord
from dotenv import load_dotenv
from discord.ext import commands
import code_roll

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="#", intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} succesfully logged in!')

@bot.event
async def on_message(message):
    if message.author == bot.user: 
        return
    if message.content == '#help':
        await message.channel.send(f'''\n
                        For Vampire (V20), enter #rollv followed by the dice and the dificulty\n
                        For Changeling (C20), enter #rollc instead \n
                        For example: #rollc 4d10 6''')
    if '#roll' in message.content:
        code_roll.rolling_dice(message.content)
    


    username = str(message.author)
    user_message = str(message.content)
    channel = str(message.channel)

    print(f'{username} said: "{user_message}" at {channel}')

    await bot.process_commands(message)

  
bot.run(TOKEN)