import discord
from typing import List


class Embed():

    def __init__(self, ctx: discord.ApplicationContext):
        self.ctx = ctx

    async def success(self, desc: str, title: str = 'Success') -> discord.Message:
        embed = discord.Embed(
            title=f':white_check_mark: {title}',
            description=desc,
            colour=discord.Colour.green()
        )
        message = await self.ctx.respond(embed=embed)
        return message

    async def error(self, desc: str, title: str = 'Error') -> discord.Message:
        embed = discord.Embed(
            title=f':no_entry: {title}',
            description=desc,
            colour=discord.Colour.red()
        )
        message = await self.ctx.respond(embed=embed)
        return message
        
    async def warn(self, desc: str, title: str = 'Warning') -> discord.Message:
        embed = discord.Embed(
            title=f':warning:  {title}',
            description=desc,
            colour=discord.Colour.dark_gold()
        )
        message = await self.ctx.respond(embed=embed)
        return message

    async def info(self, desc: str, title: str = 'Info') -> discord.Message:
        embed = discord.Embed(
            title=f':information_source: {title}',
            description=desc,
            colour=discord.Colour.blue()
        )
        message = await self.ctx.respond(embed=embed)
        return message
