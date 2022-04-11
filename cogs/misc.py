"""
copyright 2021 nirlep_5252_

licensed under the apache license, version 2.0 (the "license");
you may not use this file except in compliance with the license.
you may obtain a copy of the license at

    http://www.apache.org/licenses/license-2.0

unless required by applicable law or agreed to in writing, software
distributed under the license is distributed on an "as is" basis,
without warranties or conditions of any kind, either express or implied.
see the license for the specific language governing permissions and
limitations under the license.
"""

import discord
import time
import humanfriendly

from utils.embed import error_embed, success_embed
from discord.ext import commands
from config import emojis, main_color, website_link, support_server_link, credits_contributors, start_time, suggestion_channel, bug_report_channel
from utils.bot import epicbot


class misc(commands.cog, description="commands mostly related to the bot!"):
    def __init__(self, client: epicbot):
        self.client = client

    @commands.cooldown(1, 5, commands.buckettype.user)
    @commands.command(category="misc", help="check my ping.")
    async def ping(self, ctx):
        time1 = time.perf_counter()
        msg = await ctx.message.reply(embed=discord.embed(title=f"pinging... {emojis['loading']}", color=main_color))
        time2 = time.perf_counter()

        db_time1 = time.perf_counter()
        await self.client.prefixes.find_one({"_id": ctx.guild.id})
        db_time2 = time.perf_counter()

        shard_text = ""
        for shard, latency in self.client.latencies:
            shard_text += f"shard {shard}" + ' ' * (3 - len(str(shard))) + f': {round(latency*1000)}ms\n'

        embed = success_embed(
            "🏓  pong!",
            f"""
**basic:**
```yaml
api      : {round(self.client.latency*1000)}ms
bot      : {round((time2-time1)*1000)}ms
database : {round((db_time2-db_time1)*1000)}ms
```
**shards:**
```yaml
{shard_text}
```
            """
        ).set_thumbnail(url=self.client.user.display_avatar.url)
        await msg.edit(embed=embed)

    @commands.cooldown(1, 2, commands.buckettype.user)
    @commands.command(category="misc", help="invite cheems to your amazing server!")
    async def invite(self, ctx):
        await ctx.message.reply(embed=discord.embed(
            title="invite cheems \💖",
            description="thank you so much!",
            color=main_color,
            url=f"https://discord.com/oauth2/authorize?client_id={self.client.user.id}&permissions=8&scope=bot%20applications.commands"
        ).set_footer(text="uwu"))

    @commands.cooldown(1, 2, commands.buckettype.user)
    @commands.command(category="misc", help="vote cheems to gain perks!")
    async def vote(self, ctx):
        await ctx.message.reply(embed=discord.embed(
            title="vote cheems \💖",
            description=f"""
you can vote for me on these links:

- [top.gg](https://top.gg/bot/{self.client.user.id}/vote)
- [bots.discordlabs.org](https://bots.discordlabs.org/bot/{self.client.user.id}/vote)
- [discordbotlist.com](https://discordbotlist.com/bots/{self.client.user.id}/upvote)
            """,
            color=main_color,
        ).set_footer(text="i love you!"))

    @commands.cooldown(1, 2, commands.buckettype.user)
    @commands.command(category="misc", aliases=['discord'], help="join cheems's support server.")
    async def support(self, ctx):
        await ctx.message.reply(support_server_link)

    @commands.cooldown(1, 5, commands.buckettype.user)
    @commands.command(category="misc", help="check cheems's uptime.")
    async def uptime(self, ctx):
        await ctx.message.reply(embed=discord.embed(
            title="uptime",
            description=f"i have been up for **{humanfriendly.format_timespan(round(time.time()-start_time))}**",
            color=main_color
        ))

    @commands.cooldown(1, 5, commands.buckettype.user)
    @commands.command(category="misc", help="credits to our contributors and helpers!")
    async def credits(self, ctx):
        contributors = ""
        for e in credits_contributors:
            contributors += f"- [`{e}`](https://github.com/{credits_contributors[e][0]}) - {credits_contributors[e][1]}\n"
        await ctx.message.reply(embed=discord.embed(
            title="credits",
            description="this bot wouldn't have been possible without them!",
            color=main_color
        ).set_thumbnail(url=self.client.user.display_avatar.url).add_field(
            name="owner",
            value="- [`jovinpayz`](https://dsc.gg/cheems-invite)",
            inline=false
        ).add_field(
            name="contributors",
            value=contributors,
            inline=false
        ).add_field(
            name="other credits",
            value="""
- [`reef`](https://github.com/reef1447 - setup
            """,
            inline=false
        ).set_footer(text="they are amazing 💖"))

    @commands.cooldown(1, 5, commands.buckettype.user)
    @commands.command(category="misc", help="view our privacy policy")
    async def privacy(self, ctx):
        await ctx.message.reply(f"you can view our privacy policy here {website_link}/privacy")

    @commands.cooldown(3, 120, commands.buckettype.user)
    @commands.command(category="misc", help="submit a suggestion!")
    async def suggest(self, ctx, *, suggestion=none):
        prefix = ctx.clean_prefix

        if suggestion is none:
            ctx.command.reset_cooldown(ctx)
            return await ctx.message.reply(embed=error_embed(
                f"{emojis['tick_no']} incorrect usage!",
                f"please use it like this: `{prefix}suggest <suggestion>`"
            ))

        user_profile = await self.client.get_user_profile_(ctx.author.id)
        user_profile.update({"suggestions_submitted": user_profile['suggestions_submitted'] + 1})

        files = []
        for file in ctx.message.attachments:
            files.append(await file.to_file())

        embed = success_embed("suggestion!", suggestion
                ).set_author(name=ctx.author, icon_url=ctx.author.display_avatar.url
                ).set_footer(text=f"user id: {ctx.author.id} | guild id: {ctx.guild.id}")

        msg = await self.client.get_channel(suggestion_channel).send(embed=embed, files=files)
        await msg.add_reaction('👍')
        await msg.add_reaction('👎')
        await ctx.reply(embed=success_embed(
            f"{emojis['tick_yes']} suggestion submitted!",
            f"thank you for submitting the suggestion!\nyou have suggested a total of `{user_profile['suggestions_submitted']}` suggestions!"
        ))

    @commands.cooldown(2, 7200, commands.buckettype.user)
    @commands.command(category="misc", aliases=['bug'], help="report a buggie >~<")
    async def bugreport(self, ctx, *, bug=none):
        prefix = ctx.clean_prefix
        if bug is none:
            ctx.command.reset_cooldown(ctx)
            return await ctx.message.reply(embed=error_embed("incorrect usage", f"please use it like this: `{prefix}bug <bug>`"))
        user_profile = await self.client.get_user_profile_(ctx.author.id)
        user_profile.update({"bugs_reported": user_profile['bugs_reported'] + 1})
        embed = discord.embed(
            title="bug",
            description=f"""
```
{bug}
```
            """,
            color=main_color
        )
        embed.set_author(name=ctx.author, icon_url=ctx.author.display_avatar.url)
        embed.set_footer(text=f"user id: {ctx.author.id} | guild id: {ctx.guild.id}")
        await self.client.get_channel(bug_report_channel).send(embed=embed)
        await ctx.reply(embed=success_embed(
            f"{emojis['tick_yes']} bug submitted!",
            f"thank you for submitting the bug!\nyou have reported a total of `{user_profile['bugs_reported']}` bugs"
        ))


def setup(client):
    client.add_cog(misc(client))
