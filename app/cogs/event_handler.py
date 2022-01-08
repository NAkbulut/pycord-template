import sqlite3
import discord

from discord.ext import commands


class EventHandler(commands.Cog):
    def __init__(self, bot):
        self.bot: discord.Client = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"{self.__class__.__name__} Cog has been loaded!")

    @commands.Cog.listener()
    async def on_application_command_error(self, ctx: commands.Context, error: commands.CommandError):
        title, desc = 'Command Error', error
        if isinstance(error, commands.MissingAnyRole):
            title = 'Missing Permissions'
            desc = 'You are not permitted to run this command.'

        embed = discord.Embed(
            title=title,
            description=desc,
            colour=discord.Colour.red()
        )
        await ctx.reply(embed=embed)


def setup(bot):
    bot.add_cog(EventHandler(bot))
