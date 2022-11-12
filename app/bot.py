import os
import discord
from utils.config import config
from utils.database import ProjectDB


bot = discord.Bot(intents=discord.Intents.all())


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} - {bot.user.id}!')

@bot.event
async def on_message(message: discord.Message):
    if isinstance(message.channel, discord.DMChannel):
        return

if __name__ == '__main__':
    with open('./schema.sql') as f:
        with ProjectDB() as c:
            c.executescript(f.read())

    for filename in os.listdir('../app/cogs/'):
        if filename.endswith('.py') and not filename.startswith('__'):
            bot.load_extension(f'cogs.{filename[:-3]}')

bot.run(config['bot']['token'])
