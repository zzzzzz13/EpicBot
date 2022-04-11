"""
Copyright 2021 Nirlep_5252_

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

import discord

from discord.ext import commands
from config import PINK_COLOR_2
from utils.bot import EpicBot
from utils.embed import error_embed
from discord.utils import escape_markdown


class actions(commands.Cog, description="Interact with someone, UwU!~"):
    def __init__(self, client: EpicBot):
        self.client = client

    async def make_actions_msg(self, author, ctx, error_msgs, embed_stuff, url, user: discord.Member = None):
        if user is None:
            ctx.command.reset_cooldown(ctx)
            return error_embed("Bruh!", error_msgs[0])
        if user == author:
            ctx.command.reset_cooldown(ctx)
            return error_embed("Bruh!", error_msgs[1])
        if user == self.client.user:
            ctx.command.reset_cooldown(ctx)
            return error_embed("Bruh!", error_msgs[2])
        embed = discord.Embed(
            title=embed_stuff[0],
            description=embed_stuff[1],
            color=PINK_COLOR_2
        )
        async with self.client.session.get(url) as r:
            pain = await r.json()
            try:
                so_much_pain = pain['url']
            except Exception:
                so_much_pain = pain['link']
            embed.set_image(url=so_much_pain)
            return embed

    async def optional_actions_msg(self, ctx: commands.Context, embed_stuff, url, user: discord.Member = None):
        embed = discord.Embed(color=PINK_COLOR_2)
        if user is None:
            desc = embed_stuff[1]
        else:
            desc = embed_stuff[2]
        embed.title = embed_stuff[0]
        async with self.client.session.get(url) as response:
            try:
                pain = await response.json()
                so_much_pain = pain['url']
            except Exception:
                pain = await response.json()
                so_much_pain = pain['link']
        embed.description = desc
        embed.set_image(url=so_much_pain)

        return embed

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command(help="Bite someone OwO")
    async def bite(self, ctx, user: discord.Member = None):
        if user is not None and user != ctx.author:
            p = await self.client.get_user_profile_(user.id)
            p.update({"bites": p['bites'] + 1})
        else:
            p = None
        if user:
            user_mention = f"**{escape_markdown(user.name)}**"
        else:
            user_mention = None
        await ctx.send(
            embed=await self.make_actions_msg(
                ctx.author,
                ctx,
                [
                    "Who do you want to bite idiot? Mention them next time.",
                    "Imagine biting yourself... why are you so lonely",
                    "Hey, don't bite me pls"
                ],
                [
                    "AWOOO!",
                    f"{user_mention} just got bitten by **{escape_markdown(ctx.author.name)}**.\nThey have been bitten `{'0' if p is None else p['bites']}` times."
                ],
                "https://purrbot.site/api/img/sfw/bite/gif",
                user
            )
        )

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command(help="Cuddle with someone")
    async def cuddle(self, ctx, user: discord.Member = None):
        if user is not None and user != ctx.author:
            p = await self.client.get_user_profile_(user.id)
            p.update({"cuddles": p['cuddles'] + 1})
        else:
            p = None
        if user:
            user_mention = f"**{escape_markdown(user.name)}**"
        else:
            user_mention = None
        await ctx.send(
            embed=await self.make_actions_msg(
                ctx.author,
                ctx,
                [
                    "Who do you want to cuddle with idiot? Mention them next time.",
                    "Imagine cuddling with yourself... why are you so lonely",
                    "UwU *cuddles back*"
                ],
                [
                    "UwU",
                    f"{user_mention} just got cuddled by **{escape_markdown(ctx.author.name)}**.\nThey have gotten `{'0' if p is None else p['cuddles']}` cuddles"
                ],
                "https://purrbot.site/api/img/sfw/cuddle/gif",
                user
            )
        )

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command(help="Wink at someone 😉")
    async def wink(self, ctx, user: discord.Member = None):
        if user is not None and user != ctx.author:
            p = await self.client.get_user_profile_(user.id)
            p.update({"winks": p['winks'] + 1})
        else:
            p = None
        if user:
            user_mention = f"**{escape_markdown(user.name)}**"
        else:
            user_mention = None
        await ctx.send(
            embed=await self.make_actions_msg(
                ctx.author,
                ctx,
                [
                    "Who are you winking at? Mention someone next time!",
                    "Why are you so lonely? Don't wink at yourself!",
                    " Did you just wink at me?"
                ],
                [
                    "Winky Pinky!",
                    f"**{escape_markdown(ctx.author.name)}** just winked at {user_mention}.\nThey have been winked at `{'0' if p is None else p['winks']}` times. "
                ],
                "https://some-random-api.ml/animu/wink",
                user
            )
        )

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command(help="Hug someone 🤗")
    async def hug(self, ctx, user: discord.Member = None):
        if user is not None and user != ctx.author:
            p = await self.client.get_user_profile_(user.id)
            p.update({"hugs": p['hugs'] + 1})
        else:
            p = None
        if user:
            user_mention = f"**{escape_markdown(user.name)}**"
        else:
            user_mention = None
        await ctx.send(
            embed=await self.make_actions_msg(
                ctx.author,
                ctx,
                [
                    "Why are you so lonely? Mention someone that you wanna hug!",
                    "Imagine hugging yourself... why are you so lonely",
                    " Aww thanks for the hug! <3"
                ],
                [
                    "aww hugs UwU",
                    f"this is so cute >< **{escape_markdown(ctx.author.name)}** just hugged {user_mention}\nThey have been hugged `{'0' if p is None else p['hugs']}` times OwO"
                ],
                "https://purrbot.site/api/img/sfw/hug/gif",
                user
            )
        )

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command(help="Kiss someone 💋")
    async def kiss(self, ctx, user: discord.Member = None):
        if user is not None and user != ctx.author:
            p = await self.client.get_user_profile_(user.id)
            p.update({"kisses": p['kisses'] + 1})
        else:
            p = None
        if user:
            user_mention = f"**{escape_markdown(user.name)}**"
        else:
            user_mention = None
        await ctx.send(
            embed=await self.make_actions_msg(
                ctx.author,
                ctx,
                [
                    "Why are you so lonely? Mention someone that you wanna kiss!",
                    "Imagine kissing yourself... why are you so lonely",
                    " *Kisses back*"
                ],
                [
                    "",
                    f"**{escape_markdown(ctx.author.name)}** just kissed {user_mention}\nThey have been kissed `{'0' if p is None else p['kisses']}` times. :flushed:"
                ],
                "https://purrbot.site/api/img/sfw/kiss/gif",
                user
            )
        )

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command(help="Pat someone")
    async def pat(self, ctx, user: discord.Member = None):
        if user is not None and user != ctx.author:
            p = await self.client.get_user_profile_(user.id)
            p.update({"pats": p['pats'] + 1})
        else:
            p = None
        if user:
            user_mention = f"**{escape_markdown(user.name)}**"
        else:
            user_mention = None
        await ctx.send(
            embed=await self.make_actions_msg(
                ctx.author,
                ctx,
                [
                    "Why are you so lonely? Mention someone that you wanna pat!",
                    "Imagine patting yourself... why are you so lonely",
                    " Thank you for patting ><"
                ],
                [
                    "*cute pats*",
                    f" **{escape_markdown(ctx.author.name)}** just patted {user_mention}\nThey have `{'0' if p is None else p['pats']}` pats! "
                ],
                "https://purrbot.site/api/img/sfw/pat/gif",
                user
            )
        )

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command(help="Slap someone 🤚")
    async def slap(self, ctx, user: discord.Member = None):
        if user is not None and user != ctx.author:
            p = await self.client.get_user_profile_(user.id)
            p.update({"slaps": p['slaps'] + 1})
        else:
            p = None
        if user:
            user_mention = f"**{escape_markdown(user.name)}**"
        else:
            user_mention = None
        await ctx.send(
            embed=await self.make_actions_msg(
                ctx.author,
                ctx,
                [
                    "Who do you want to slap idiot? Mention them next time.",
                    "Imagine slapping yourself... why are you so lonely",
                    " Yo, that slap hurt!"
                ],
                [
                    "Damn boi!",
                    f"{user_mention} just got slapped by **{escape_markdown(ctx.author.name)}**.\nThey have been slapped `{'0' if p is None else p['slaps']}` times!"
                ],
                "https://purrbot.site/api/img/sfw/slap/gif",
                user
            )
        )

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command(help="Tickle someone")
    async def tickle(self, ctx, user: discord.Member = None):
        if user is not None and user != ctx.author:
            p = await self.client.get_user_profile_(user.id)
            p.update({"tickles": p['tickles'] + 1})
        else:
            p = None
        if user:
            user_mention = f"**{escape_markdown(user.name)}**"
        else:
            user_mention = None
        await ctx.send(
            embed=await self.make_actions_msg(
                ctx.author,
                ctx,
                [
                    "Who do you want to tickle idiot? Mention them next time.",
                    "Imagine tickling yourself... why are you so lonely",
                    " Hahahaha"
                ],
                [
                    "Tickle, tickle!",
                    f"{user_mention} just got tickled by **{escape_markdown(ctx.author.name)}**.\nThey have been tickled `{'0' if p is None else p['tickles']}` times."
                ],
                "https://purrbot.site/api/img/sfw/tickle/gif",
                user
            )
        )

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command(help="Lick someone")
    async def lick(self, ctx, user: discord.Member = None):
        if user is not None and user != ctx.author:
            p = await self.client.get_user_profile_(user.id)
            p.update({"licks": p['licks'] + 1})
        else:
            p = None
        if user:
            user_mention = f"**{escape_markdown(user.name)}**"
        else:
            user_mention = None
        await ctx.send(
            embed=await self.make_actions_msg(
                ctx.author,
                ctx,
                [
                    "Who do you want to lick idiot? Mention them next time.",
                    "Imagine licking yourself... why are you so lonely",
                    " *licks you back*"
                ],
                [
                    "Yummy!",
                    f"{user_mention} just got licked by **{escape_markdown(ctx.author.name)}**.\nMmm, they have been licked `{'0' if p is None else p['licks']}` times :yum:"
                ],
                "https://purrbot.site/api/img/sfw/lick/gif",
                user
            )
        )

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command(help="Feed someone")
    async def feed(self, ctx, user: discord.Member = None):
        if user is not None and user != ctx.author:
            p = await self.client.get_user_profile_(user.id)
            p.update({"feeds": p['feeds'] + 1})
        else:
            p = None
        if user:
            user_mention = f"**{escape_markdown(user.name)}**"
        else:
            user_mention = None
        await ctx.send(
            embed=await self.make_actions_msg(
                ctx.author,
                ctx,
                [
                    "Who do you want to feed idiot? Mention them next time.",
                    "Imagine feeding yourself... why are you so lonely",
                    " Thanks for feeding me cutie!~"
                ],
                [
                    "Yummy!",
                    f"{user_mention} just got yummy food from **{escape_markdown(ctx.author.name)}**.\nThey have been fed `{'0' if p is None else p['feeds']}` times."
                ],
                "https://purrbot.site/api/img/sfw/feed/gif",
                user
            )
        )

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command(help="Facepalm at someone")
    async def facepalm(self, ctx, user: discord.Member = None):
        if user:
            user_mention = f"**{escape_markdown(user.name)}**"
        else:
            user_mention = None
        p = await self.client.get_user_profile_(ctx.author.id)
        p.update({"facepalms": p['facepalms'] + 1})
        facepalm_text = f"You have facepalmed `{p['facepalms']}` times."
        await ctx.send(
            embed=await self.optional_actions_msg(
                ctx,
                [
                    " Bruh",
                    f"**{escape_markdown(ctx.author.name)}** is facepalming...\n{facepalm_text}",
                    f"**{escape_markdown(ctx.author.name)}** is facepalming at {user_mention}.\n{facepalm_text}",
                ],
                "https://some-random-api.ml/animu/face-palm",
                user
            )
        )

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command(help="*Blushes* UwU!")
    async def blush(self, ctx, user: discord.Member = None):
        if user:
            user_name = escape_markdown(str(user.name))
        else:
            user_name = None
        p = await self.client.get_user_profile_(ctx.author.id)
        p.update({"blushes": p['blushes'] + 1})
        blush_text = f"You have blushed `{p['blushes']}` times. >///<"
        await ctx.send(
            embed=await self.optional_actions_msg(
                ctx,
                [
                    "UwU!",
                    f"**{escape_markdown(str(ctx.author.name))}** is blushing...\n{blush_text}",
                    f"**{escape_markdown(str(ctx.author.name))}** is blushing at **{user_name}**\n{blush_text}",
                ],
                "https://shiro.gg/api/images/blush",
                user
            )
        )

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command(help="Wag your tail!")
    async def tail(self, ctx, user: discord.Member = None):
        if user:
            user_name = escape_markdown(str(user.name))
        else:
            user_name = None
        p = await self.client.get_user_profile_(ctx.author.id)
        p.update({"tail_wags": p['tail_wags'] + 1})
        tail_text = f"You have wagged your tail `{p['tail_wags']}` times."
        await ctx.send(
            embed=await self.optional_actions_msg(
                ctx,
                [
                    "Meow!~",
                    f"**{escape_markdown(str(ctx.author.name))}** is wagging their tail...\n{tail_text}",
                    f"**{escape_markdown(str(ctx.author.name))}** is wagging their tail at **{user_name}**\n{tail_text}",
                ],
                "https://purrbot.site/api/img/sfw/tail/gif",
                user
            )
        )

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command(help=";(")
    async def cry(self, ctx, user: discord.Member = None):
        if user:
            user_name = escape_markdown(str(user.name))
        else:
            user_name = None
        p = await self.client.get_user_profile_(ctx.author.id)
        p.update({"cries": p['cries'] + 1})
        cries_text = f"You have cried `{p['cries']}` times."
        await ctx.send(
            embed=await self.optional_actions_msg(
                ctx,
                [
                    "Sad!",
                    f"**{escape_markdown(str(ctx.author.name))}** is crying... ;(\n{cries_text}",
                    f"**{escape_markdown(str(ctx.author.name))}** is crying because of **{user_name}** ;(\n{cries_text}",
                ],
                "https://purrbot.site/api/img/sfw/cry/gif",
                user
            )
        )


def setup(client):
    client.add_cog(actions(client))
