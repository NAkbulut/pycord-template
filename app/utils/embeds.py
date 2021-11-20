import discord
from typing import List
from discord.ext import commands


class Embed():

    def __init__(self, ctx: commands.Context):
        self.ctx = ctx

    async def warn(self, desc: str, title: str = 'Warning') -> discord.Message:
        embed = discord.Embed(
            title=f':warning:  {title}',
            description=desc,
            colour=discord.Colour.dark_gold()
        )
        message = await self.ctx.reply(embed=embed)
        return message

    async def error(self, desc: str, title: str = 'Error') -> discord.Message:
        embed = discord.Embed(
            title=f':no_entry: {title}',
            description=desc,
            colour=discord.Colour.red()
        )
        message = await self.ctx.reply(embed=embed)
        return message

    async def info(self, desc: str, title: str = 'Info') -> discord.Message:
        embed = discord.Embed(
            title=f':information_source: {title}',
            description=desc,
            colour=discord.Colour.blue()
        )
        message = await self.ctx.reply(embed=embed)
        return message

    async def success(self, desc: str, title: str = 'Success') -> discord.Message:
        embed = discord.Embed(
            title=f':white_check_mark: {title}',
            description=desc,
            colour=discord.Colour.green()
        )
        message = await self.ctx.reply(embed=embed)
        return message

    async def prompt(self, desc: str, title: str, emotes: List[discord.Emoji]) -> discord.Message:
        embed = discord.Embed(
            title=f'{title}',
            description=desc,
            colour=discord.Colour.orange()
        )
        message: discord.Message = await self.ctx.reply(embed=embed)
        for emote in emotes:
            await message.add_reaction(emote)
        return message
