import os
import discord
import traceback
from utils.checks import Check


class Dev(discord.Cog):
    def __init__(self, bot):
        self.bot: discord.Bot = bot

    @discord.Cog.listener()
    async def on_ready(self):
        print(f"{self.__class__.__name__} Cog has been loaded!")

    scg_dev = discord.commands.SlashCommandGroup("dev", "Development management module")

    @scg_dev.command(name="list", description="List all registered application modules.", checks=[Check.is_dev])
    async def list_subcmd(self, ctx):
        embed = discord.Embed(
            title='Cogs list',
            color=discord.Colour.light_grey()
        )
        loaded, unloaded = [], []
        for filename in os.listdir('../app/cogs/'):
            if filename.endswith('.py') and not filename.startswith('__'):
                try:
                    self.bot.unload_extension(f'cogs.{filename[:-3]}')
                except discord.ExtensionNotLoaded:
                    unloaded.append(filename[:-3])
                else:
                    loaded.append(filename[:-3])
                    self.bot.load_extension(f'cogs.{filename[:-3]}')
        embed.add_field(
            name='Loaded cogs',
            value='\n'.join(loaded) if '\n'.join(loaded) else '\uFEFF',
            inline=False
        )
        embed.add_field(
            name='Unloaded cogs',
            value='\n'.join(unloaded) if '\n'.join(unloaded) else '\uFEFF',
            inline=False
        )
        await ctx.respond(embed=embed)

    @scg_dev.command(name="load", description="Load a registered application module.", checks=[Check.is_dev])
    async def load_subcmd(self, ctx, cog):
        embed = discord.Embed(
            title='Loading cog',
            color=discord.Colour.light_grey()
        )
        filename = f'{cog.lower()}.py'
        if not os.path.exists(f'../app/cogs/{filename}'):
            embed.add_field(
                name=f'Failed to load: `{filename[:-3]}`',
                value='This cog does not exist.',
                inline=False
            )
        elif filename.endswith('.py') and not filename.startswith('__'):
            try:
                self.bot.load_extension(f'cogs.{filename[:-3]}')
                embed.add_field(
                    name=f'Loaded: `{filename[:-3]}`',
                    value='\uFEFF',
                    inline=False
                )
            except Exception:
                trace = traceback.format_exc()
                embed.add_field(
                    name=f'Failed to load: `{filename[:-3]}`',
                    value=trace,
                    inline=False
                )
        await ctx.respond(embed=embed)

    @scg_dev.command(name="unload", description="Unload a registered application module.", checks=[Check.is_dev])
    async def unload_subcmd(self, ctx, cog):
        embed = discord.Embed(
            title='Unloading cog',
            color=discord.Colour.light_grey()
        )
        filename = f'{cog.lower()}.py'
        if not os.path.exists(f'../app/cogs/{filename}'):
            embed.add_field(
                name=f'Failed to unload: `{filename[:-3]}`',
                value='This cog does not exist.',
                inline=False
            )
        elif filename.endswith('.py') and not filename.startswith('__'):
            try:
                self.bot.unload_extension(f'cogs.{filename[:-3]}')
                embed.add_field(
                    name=f'Unloaded: `{filename[:-3]}`',
                    value='\uFEFF',
                    inline=False
                )
            except Exception:
                trace = traceback.format_exc()
                embed.add_field(
                    name=f'Failed to Unload: `{filename[:-3]}`',
                    value=trace,
                    inline=False
                )
        await ctx.respond(embed=embed)

    @scg_dev.command(name="reload", description="Reload a registered application module.", checks=[Check.is_dev])
    async def reload_subcmd(self, ctx, cog=None):
        if not cog:
            embed = discord.Embed(
                title='Reloading all cogs',
                color=discord.Colour.light_grey()
            )
            for filename in os.listdir('../app/cogs/'):
                if filename.endswith('.py') and not filename.startswith('__'):
                    try:
                        self.bot.unload_extension(f'cogs.{filename[:-3]}')
                        self.bot.load_extension(f'cogs.{filename[:-3]}')
                        embed.add_field(
                            name=f'Reloaded: `{filename[:-3]}`',
                            value='\uFEFF',
                            inline=False
                        )
                    except Exception as e:
                        embed.add_field(
                            name=f"Failed to reload: `{filename[:-3]}`",
                            value=e,
                            inline=False
                        )
            await ctx.respond(embed=embed)
        else:
            embed = discord.Embed(
                title='Reloading cog',
                color=discord.Colour.light_grey()
            )
            filename = f'{cog.lower()}.py'
            if not os.path.exists(f'../app/cogs/{filename}'):
                embed.add_field(
                    name=f'Failed to reload: `{filename[:-3]}`',
                    value='This cog does not exist.',
                    inline=False
                )
            elif filename.endswith('.py') and not filename.startswith('__'):
                try:
                    self.bot.unload_extension(f'cogs.{filename[:-3]}')
                    self.bot.load_extension(f'cogs.{filename[:-3]}')
                    embed.add_field(
                        name=f'Reloaded: `{filename[:-3]}`',
                        value='\uFEFF',
                        inline=False
                    )
                except Exception:
                    trace = traceback.format_exc()
                    embed.add_field(
                        name=f'Failed to reload: `{filename[:-3]}`',
                        value=trace,
                        inline=False
                    )
            await ctx.respond(embed=embed)


def setup(bot):
    bot.add_cog(Dev(bot))
