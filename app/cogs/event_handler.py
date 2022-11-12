import discord
import sqlite3


class EventHandler(discord.Cog):
    def __init__(self, bot):
        self.bot: discord.Bot = bot

    @discord.Cog.listener()
    async def on_ready(self):
        print(f"{self.__class__.__name__} Cog has been loaded!")

    @discord.Cog.listener()
    async def on_application_command_error(self, ctx: discord.ApplicationContext, error: discord.ApplicationCommand.error):
        title, desc = 'Command Error', error
        if isinstance(error, discord.CheckFailure):
            title = 'Missing Permissions'
            desc = 'You are not permitted to run this command.'

        embed = discord.Embed(
            title=title,
            description=desc,
            colour=discord.Colour.red()
        )
        await ctx.respond(embed=embed)


def setup(bot):
    bot.add_cog(EventHandler(bot))
