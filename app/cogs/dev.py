import discord
import os
import traceback
from discord.ext import commands
from utils.checks import Check


class Dev(commands.Cog):
    def __init__(self, bot):
        self.bot: commands.Bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"{self.__class__.__name__} Cog has been loaded!")

    @commands.group(name='cogs', aliases=['cog', 'extensions'], description='Cogs management module.')
    async def cogs_maincmd(self, ctx):
        pass

    @cogs_maincmd.command(name='list', aliases=['status'], description='Lists all loaded and unloaded cogs.')
    @commands.check(Check.is_dev)
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
                except commands.ExtensionNotLoaded:
                    unloaded.append(filename)
                else:
                    loaded.append(filename)
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
        await ctx.reply(embed=embed)

    @cogs_maincmd.command(name='load', description='Load a specific cog.', usage='<cog>')
    @commands.check(Check.is_dev)
    async def load_subcmd(self, ctx, cog):
        embed = discord.Embed(
            title='Loading cog',
            color=discord.Colour.light_grey()
        )
        filename = f'{cog.lower()}.py'
        if not os.path.exists(f'../app/cogs/{filename}'):
            embed.add_field(
                name=f'Failed to load: `{filename}`',
                value='This cog does not exist.',
                inline=False
            )
        elif filename.endswith('.py') and not filename.startswith('__'):
            try:
                self.bot.load_extension(f'cogs.{filename[:-3]}')
                embed.add_field(
                    name=f'Loaded: `{filename}`',
                    value='\uFEFF',
                    inline=False
                )
            except Exception:
                trace = traceback.format_exc()
                embed.add_field(
                    name=f'Failed to load: `{filename}`',
                    value=trace,
                    inline=False
                )
        await ctx.reply(embed=embed)

    @cogs_maincmd.command(name='unload', description='Unload a specific cog.', usage='<cog>')
    @commands.check(Check.is_dev)
    async def unload_subcmd(self, ctx, cog):
        embed = discord.Embed(
            title='Unloading cog',
            color=discord.Colour.light_grey()
        )
        filename = f'{cog.lower()}.py'
        if not os.path.exists(f'../app/cogs/{filename}'):
            embed.add_field(
                name=f'Failed to unload: `{filename}`',
                value='This cog does not exist.',
                inline=False
            )
        elif filename.endswith('.py') and not filename.startswith('__'):
            try:
                self.bot.unload_extension(f'cogs.{filename[:-3]}')
                embed.add_field(
                    name=f'Unloaded: `{filename}`',
                    value='\uFEFF',
                    inline=False
                )
            except Exception:
                trace = traceback.format_exc()
                embed.add_field(
                    name=f'Failed to Unload: `{filename}`',
                    value=trace,
                    inline=False
                )
        await ctx.reply(embed=embed)

    @cogs_maincmd.command(name='reload', description='Reloads all/specific cog.', usage='[cog]')
    @commands.check(Check.is_dev)
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
                            name=f'Reloaded: `{filename}`',
                            value='\uFEFF',
                            inline=False
                        )
                    except Exception as e:
                        embed.add_field(
                            name=f"Failed to reload: `{filename}`",
                            value=e,
                            inline=False
                        )
            await ctx.reply(embed=embed)
        else:
            embed = discord.Embed(
                title='Reloading cog',
                color=discord.Colour.light_grey()
            )
            filename = f'{cog.lower()}.py'
            if not os.path.exists(f'../app/cogs/{filename}'):
                embed.add_field(
                    name=f'Failed to reload: `{filename}`',
                    value='This cog does not exist.',
                    inline=False
                )
            elif filename.endswith('.py') and not filename.startswith('__'):
                try:
                    self.bot.unload_extension(f'cogs.{filename[:-3]}')
                    self.bot.load_extension(f'cogs.{filename[:-3]}')
                    embed.add_field(
                        name=f'Reloaded: `{filename}`',
                        value='\uFEFF',
                        inline=False
                    )
                except Exception:
                    trace = traceback.format_exc()
                    embed.add_field(
                        name=f'Failed to reload: `{filename}`',
                        value=trace,
                        inline=False
                    )
            await ctx.reply(embed=embed)


def setup(bot):
    bot.add_cog(Dev(bot))
