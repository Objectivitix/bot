import datetime
from typing import Optional

import discord
from discord.ext import commands
import pytz

from bot.utilities import get_yaml_val

colors = get_yaml_val("bot/config.yml", "colors")["colors"]

DURATION_DICT = get_yaml_val("bot/config.yml", "duration")["duration"]


class Times(commands.Cog):
    """Cog for Time commands."""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(aliases=["tz"])
    async def timeintimezone(
        self,
        ctx: commands.Context,
        timezone: str = "US/Central",
        intime: Optional[str] = None,
    ):
        """Gets time in specified timezone.

        If an argument is given, the command
        returns what the time will be in the
        specified duration in the specified timezone."""
        strzone = timezone
        timezone = pytz.timezone(timezone)
        if not intime:
            timestamp = datetime.datetime.now(tz=timezone)
            embed = discord.Embed(
                title=f"Time in {strzone}:",
                description=f"{timestamp.strftime('%I:%M %p')}",
                color=colors["green"],
            )
            await ctx.send(embed=embed)
        else:
            seconds = int(intime[0:-1]) * DURATION_DICT[intime[-1]]
            utc = int(datetime.datetime.utcnow().timestamp())
            timestamp = seconds + utc
            timestamp = datetime.datetime.utcfromtimestamp(timestamp)
            timestamp = timestamp.astimezone(timezone)
            timestamp = timestamp.strftime("%I:%M %p")
            embed = discord.Embed(
                title=f"Time in {strzone} in {intime}:",
                description=timestamp,
                color=colors["green"],
            )
            await ctx.send(embed=embed)


def setup(bot: commands.Bot):
    """Loads cog."""
    bot.add_cog(Times(bot))
