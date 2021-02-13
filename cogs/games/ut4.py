from discord.ext import commands


class UT4:
    """Unreal Tournament 4 related commands"""
    def __init__(self, bot):
        self.bot = bot

    @commands.group(invoke_without_command=True)
    async def ut4(self):
        await self.bot.say('https://www.epicgames.com/unrealtournament/')

    @ut4.command()
    async def changelog(self):
        await self.bot.say('https://wiki.unrealengine.com/Version_Notes')


def setup(bot):
    bot.add_cog(UT4(bot))
