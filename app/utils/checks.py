import discord
from typing import Literal
from utils.config import config


class Check():

    def is_dev(ctx: discord.ApplicationContext) -> Literal[True]:
        if ctx.author.id in config['bot']['dev']:
            return True
        else:
            raise discord.CheckFailure
