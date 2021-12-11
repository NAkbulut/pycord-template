import os
import discord
from discord.ext import commands
from utils.config import config
from utils.database import ProjectDB


my_intents = discord.Intents.all()
bot = commands.Bot(command_prefix=',', intents = my_intents, case_insensitive=True)


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} - {bot.user.id}!')


if __name__ == '__main__':
    with open('./schema.sql') as f:
        with ProjectDB() as c:
            c.executescript(f.read())

    for filename in os.listdir('../app/cogs/'):
        if filename.endswith('.py') and not filename.startswith('__'):
            bot.load_extension(f'cogs.{filename[:-3]}')

bot.run(config['bot']['token'])
