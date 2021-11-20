from typing import Literal
from utils.config import config
from discord.ext import commands


class Check():

    def is_dev(ctx: commands.Context) -> Literal[True]:
        if ctx.author.id in config['bot']['dev']:
            return True
        else:
            raise commands.MissingAnyRole(config['bot'['dev']])
