import os
import discord
from discord.ext import commands
from utils.config import config
from utils.database import projectDb


my_intents = discord.Intents.all()
client = commands.Bot(command_prefix=',', intents = my_intents, case_insensitive=True)


@client.event
async def on_ready():
    print(f'Logged in as {client.user.name} - {client.user.id}!')


if __name__ == '__main__':
    with open('./schema.sql') as f:
        with projectDb() as c:
            c.executescript(f.read())

    for filename in os.listdir('../app/cogs/'):
        if filename.endswith('.py') and not filename.startswith('__'):
            client.load_extension(f'cogs.{filename[:-3]}')

client.run(config['bot']['token'])
