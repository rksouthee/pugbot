import asyncio
from discord.ext import commands
import discord
import discord.utils

VERSION = '0.4.4'
URL = 'https://github.com/rksouthee/discord-pugbot/blob/master/CHANGELOG.md'


class Info:
    """Information about the bot"""
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def info(self):
        result = ['**__About Me:__**']
        result.append('- Version: {}'.format(VERSION))
        result.append('- Author: rksouthee')
        result.append('- Library: discord.py (Python)')
        await self.bot.say('\n'.join(result))

    @commands.command()
    async def changelog(self):
        await self.bot.say(URL)

    @commands.command(pass_context=True, no_pm=True)
    async def invite(self, ctx):
        """Returns an active instant invite for the current Channel

        Bot must have proper permissions to get this information
        """
        try:
            invites = await self.bot.invites_from(ctx.message.server)
        except discord.Forbidden:
            return await self.bot.say('I do not have the proper permissions')
        except discord.HTTPException:
            return await self.bot.say('Invite failed')

        invite = discord.utils.get(invites, channel=ctx.message.channel)
        if invite is None:
            try:
                invite = await self.bot.create_invite(ctx.message.channel)
            except discord.HTTPException:
                return await self.bot.say('Unable to create new invite')
        await self.bot.say(invite)

    @commands.command(pass_context=True)
    async def purge(self, ctx, limit: int=100):
        """Purge bot's PMs to you, must PM the bot"""
        channel = ctx.message.channel
        if channel.is_private:
            messages = 1
            async for entry in self.bot.logs_from(channel, limit=limit, before=ctx.message):
                if messages % 5 == 0:
                    await asyncio.sleep(5)

                if entry.author == self.bot.user:
                    await self.bot.delete_message(entry)
                    messages += 1


def setup(bot):
    bot.add_cog(Info(bot))
