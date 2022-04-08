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

import time
import os
from dotenv import load_dotenv
load_dotenv()

# LOL TOKEN GO BRR
BOT_TOKEN = os.environ.get("TOKEN")  # your discord bot token
BOT_TOKEN_BETA = os.environ.get("TOKEN_BETA")  # the token of the beta bot (optional)

MONGO_DB_URL = os.environ.get("MONGO")  # your mongodb database connection url string
MONGO_DB_URL_BETA = os.environ.get("MONGO_BETA")  # database for the beta bot (optional)
DB_UPDATE_INTERVAL = 300  # the interval at which the database is updated

PREFIX = "c!"  # the default prefix for the bot
OWNERS = [928620885944983623]  # the bot owners
COOLDOWN_BYPASS = [928620885944983623, 928620885944983623, 928620885944983623]  # the users that bypass the cooldown
EPICBOT_GUILD_ID = 944285798772117524  # the id of the epicbot guild
PREMIUM_GUILDS = [944285798772117524, 944285798772117524, 944285798772117524]  # the ids of the premium guilds (it bypasses some cmd requirements)

# AFK KEYS

UD_API_KEY = os.environ.get("UD_API_KEY")
WEATHER_API_KEY = os.environ.get("WEATHER")
TOP_GG_TOKEN = os.environ.get("SHIT_GG_TOKEN")
TWITCH_CLIENT_ID = os.environ.get("TWITCH_CLIENT_ID")
TWITCH_CLIENT_SECRET = os.environ.get("TWITCH_CLIENT_SECRET")
CHAT_BID = os.environ.get("CHAT_BID")
CHAT_API_KEY = os.environ.get("CHAT_API_KEY")
DAGPI_KEY = os.environ.get("DAGPI_KEY")
STATCORD_KEY = os.environ.get("STATCORD_KEY")
YOUTUBE_API_KEY = os.environ.get("YOUTUBE_API_KEY")

# SECRET LOGS HEHE :3

ONLINE_LOG_CHANNEL = 960824177139548170
SHARD_LOG_CHANNEL = 832645114459324507
ADD_REMOVE_LOG_CHANNEL = 793832499645644800
DATABASE_LOG_CHANNEL = 832645226799300609
COMMANDS_LOG_CHANNEL = 775949886842994698
ERROR_LOG_CHANNEL = 832645286098239488
DM_LOG_CHANNEL = 793482521076695070
BUG_REPORT_CHANNEL = 834665587010568252
RANK_CARD_SUBMIT_CHANNEL = 856512113580703814
SUGGESTION_CHANNEL = 746202728648146986
USER_REPORT_CHANNEL = 863768592159473694

# WEBHOOK LOGS

WEBHOOKS = {
    "startup": (880847339378573403, os.environ.get("startup_webhook")),
    "add_remove": (880847516537585734, os.environ.get("add_remove_webhook")),
    "cmd_uses": (880847705809760276, os.environ.get("cmd_uses_webhook")),
    "cmd_error": (880846787349446778, os.environ.get("cmd_error_webhook")),
    "event_error": (880844779565506601, os.environ.get("event_error_webhook")),
}

# COLORS

# MAIN_COLOR = 0xDC143C # crimson
MAIN_COLOR = 0x459fff  # light blue kinda
RED_COLOR = 0xFF0000
ORANGE_COLOR = 0xFFA500
PINK_COLOR = 0xe0b3c7
PINK_COLOR_2 = 0xFFC0CB
STARBOARD_COLOR = 15655584
INVISIBLE_COLOR = 0x36393F

# LINK

WEBSITE_LINK = "https://soon.tk"
SUPPORT_SERVER_LINK = "https://dsc.gg/cheems-support"
INVITE_BOT_LINK = "https://dsc.gg/cheems-invite"
VOTE_LINK = "https://top.gg/"

# ROLES

BOT_MOD_ROLE = 944286406988161046
OWNER_ROLE = 944286406988161046
SUPPORTER_ROLE = 961210631682404352
PARTNER_ROLE = 961210803489497130
STAFF_ROLE = 961209796688760842
BOOSTER_ROLE = 947931107423318056
DESIGN_HELPER_ROLE = 961209796688760842
VIP_ROLE = 953959223937630248

# EMOJIS

BADGE_EMOJIS = {
    "normie": "<:members:952237483553341470>",
    "cutevi": "<a:FN_cutekitten:961211767495725087>",
    "bot_mod": "<a:pepemod:961211900409036821>",
    "owner_of_epicness": "👑",
    "staff_member": "<a:pepestaff:961212131418710016>",
    "supporter": "<:Rudra_ka_full_sapot:960896042876940318>",
    "booster": "<a:PepeBoostt:961212491118034944>",
    "partner": "<:partners:961211114690080769>",
    "bug_hunter": "<:spy_bughunter:961212632457678908>",
    "elite_bug_hunter": "<:spy_bughunter:961212632457678908>",
    "early_supporter": "<a:spy_early:961212815148990535>",
    "Big_PP": "<:happy:961213148700999721>",
    "No_PP": "<:happy:961213148700999721>",
    "aw||oo||sh": "<a:PetAwish:819234104817877003>",
    "wendo": "<a:MH_wii_clap:857201084727689246>",
    "cat": "<a:CatRainbowJam:857201249447444530>",
    "best_streamer": "<:RamHeart:851480978668781648>",
    "voter": "<:upvote:857205463350116353>",
    "cutie": "<:mmm:834782050006466590>",
    "helper": "<:FN_HelperBadge:961213319681802250>",
    "savior": "🙏",
    "very_good_taste": "<a:petartorol:857212043375280160>",
    "samsung_girl": "<:catgirlboop:857213250512879626>",
    "love_magnet": "<:love_magnet:857215765043347527>",
    "designer": "🎨",
}
EMOJIS = {
    'heawt': '<:happy:961213148700999721> ',
    'loading': '<:happy:961213148700999721> ',
    'hacker_pepe': '<:happy:961213148700999721> ',
    # 'tick_yes': '👍 ',
    'tick_yes': '👍 ',  # '👎 ',
    # 'tick_no': '👎 ',
    'tick_no': '👎 ',
    'wave_1': '<a:kannawave:961228276477599774> ',
    'shy_uwu': '<a:uwu_bean:961228467087765574> ',
    'add': '<:happy:961213148700999721> ',
    'remove': '<:happy:961213148700999721> ',
    'pepe_jam': '<:happy:961213148700999721> ',
    'pog_stop': '<:happy:961213148700999721> ',    'pog_stop': '<:happy:961213148700999721> ',
    'catjam': '<:CH_CatBlushy:961213636506943548> ',
    'epic_coin': '<:epiccoin:837959671532748830> ',
    'bruh': '<:CH_CatBlushy:961213636506943548> ',
    'mmm': '<:CH_CatBlushy:961213636506943548> ',
    'sleepy': '<:CH_CatBlushy:961213636506943548> ',
    'muted': '<:muted:843472761342132294> ',
    'unmuted': '<:unmuted:843488852063682582> ',
    'reminder': '⏰ ',
    'cool': '<a:cool:844813588476854273> ',
    'settings': '<:settings:825008012867534928> ',
    'settings_color': '<a:settings_color:848495459882237962> ',
    'lb': '<a:leaderboard:850573823677431818> ',
    'poglep': '<:poglep:836173704249344011> ',
    'weirdchamp': '<:WeirdChamp:851062483090800640> ',
    'twitch': '<:twitch:852475334419021835> ',
    'members': '<:members:853203090001887232> ',
    'ramaziHeart': '<:RamHeart:851480978668781648> ',
    'leveling': '<a:leveling:849535096838815775> ',
    'vay': '<:vay:849994877629497365> ',
    'chat': '<:Chat:859651327391170591> ',
    'hu_peng': '<:whopingme:861230622525882378> ',
    'disboard': '<:disboard:861565998510637107> ',
    'online': '<:status_online:862599876741955584> ',
    'idle': '<:status_idle:862600144917364737> ',
    'dnd': '<:status_dnd:862600241851924480> ',
    'arrow': '<:Arrow:869101378822373417> ',
    'reaction': '<:add_reaction:873891867610210304> ',
    'cmd_arrow': '<a:GF_Little_Pretty_Star_Pink:951513061930434610> ',
    'youtube': '<:YoutubeLogo:884650525117792316> ',
    'cry_': '<a:cry_:887173073630015508>'
}
EMOJIS_FOR_COGS = {
    'actions': '<a:emoji:961658231237787688>',
    'emojis': '<:icecream_:944499781349285988>',
    'fun': '<:funny:961658476449378405>',
    'games': '<a:sapinkkawaiigamer:961229171168776192>',
    'image': '<:pepeuwuknit:952510858041372692>',
    'info': '<a:info:961657006287106059>',
    'leveling': '<:p_badge_TKG:961229361393061898>',
    'misc': '<:mister_anurag:961657334239727626>',
    'mod': '🛡️',
    'music': '<:p_badge_TKG:961229361393061898>',
    'nsfw': '🔞',
    'config': '<a:D_CAFE_SETTINGS:952237985984835704>',
    'starboard': '⭐',
    'utility': '🔧',
    'user': '<:members:952237483553341470>',
    'notifications': '🔔',
    'custom': EMOJIS['settings_color'][:-1],
}
CUTE_EMOJIS = [
    "<:shy:844039614032904222>",
    "<:shy_peek:844039614309466134>",
    "<:Shy:851665918236557312>",
    "<:shy2:851666263922966588>",
    "<a:HeartOwO:849179336041168916>",
    "<:Heawt:802801495153967154>",
    "<:UwUlove:836174204108931072>",
    "<:Pikaluv:842981646424473601>",
    "<:mmm:834782050006466590>",
    "<a:kissl:808235261708337182>",
    "<:ur_cute:845151161039716362>",
    "<:thanks:800741855805046815>",
    "<a:hugs:839739273083224104>"
]
THINKING_EMOJI_URLS = [
    'https://cdn.discordapp.com/emojis/862387505852055602.png',
    'https://cdn.discordapp.com/emojis/768302864685727755.png',
    'https://cdn.discordapp.com/emojis/854206416830988318.png',
    'https://cdn.discordapp.com/emojis/853192295277002752.png',
    'https://cdn.discordapp.com/emojis/585956493392871424.png',
    'https://cdn.discordapp.com/emojis/819207595876417546.png'
]

# CREDITS

CREDITS_CONTRIBUTORS = {
    "reef": ["reef1447", "Staff"]
}

# PP

BIG_PP_GANG = [724859002646823032, 532177714203852800, 791580073190621205, 928620885944983623]
NO_PP_GANG = [550083219136053259, 729770314388603020]

# SOME RANDOM STUFF

start_time = time.time()
EMPTY_CHARACTER = "‎"

custom_cmds_tags_lemao = """
**User:**
`{user_name}` - The name of the user.
`{user_nickname}` - The nickname of the user.
`{user_discrim}` - The discriminator of the user.
`{user_tag}` - The complete tag of the user. (Eg. Username#0000)
`{user_id}` - The ID of the user.
`{user_mention}` - The mention of the user.
`{user_avatar}` - The avatar of the user.

**Guild:**
`{guild_name}` - The name of the server.
`{guild_id}` - The ID of the server.
`{guild_membercount}` - The membercount of the server.
`{guild_icon}` - The icon URL of the server.
`{guild_owner_name}` - The name of the owner of the guild.
`{guild_owner_id}` - The ID of the owner of the guild.
`{guild_owner_mention}` - The mention of the owner of the guild.

**Invites:**
`{user_invites}` - The invites of the user.
`{inviter_name}` - The name of the inviter who invited the user.
`{inviter_discrim}` - The discriminator of the inviter.
`{inviter_tag}` - The complete tag of the inviter. (Eg. Username#0000)
`{inviter_id}` - The ID of the inviter.
`{inviter_mention}` - The mention of the inviter.
`{inviter_avatar}` - The avatar of the inviter.
`{inviter_invites}` - The invites of the inviter.
"""

ENABLE = ['enable', 'enabled', 'yes', 'true']
DISABLE = ['disable', 'disabled', 'no', 'false']

DEFAULT_WELCOME_MSG = """
{
    "title": "Welcome",
    "description": "Yay! {user_mention} has joined our server!",
    "color": "MAIN_COLOR",
    "footer": {
        "text": "Invited by {inviter_tag}",
        "icon_url": "{inviter_avatar}"
    },
    "thumbnail": "{user_avatar}"
}
"""
DEFAULT_LEAVE_MSG = """
{
    "title": "Sad!",
    "description": "Sad! **{user_tag}** has left us!",
    "color": "RED_COLOR",
    "footer": {
        "text": "Invited by {inviter_tag}",
        "icon_url": "{inviter_avatar}"
    },
    "thumbnail": "{user_avatar}"
}
"""

DEFAULT_TWITCH_MSG = """
Poggers! **{streamer}** is now live! Go check them out! {url}
"""

DEFAULT_LEVEL_UP_MSG = """
Pog! {user_mention} just leveled up to level {level}!
"""

DEFAULT_AUTOMOD_CONFIG = {
    "banned_words": {
        "enabled": False,
        "words": [],
        "removed_words": []
    },
    "all_caps": {
        "enabled": False
    },
    "duplicate_text": {
        "enabled": False
    },
    "message_spam": {
        "enabled": False
    },
    "invites": {
        "enabled": False
    },
    "links": {
        "enabled": False,
        "whitelist": []
    },
    "mass_mentions": {
        "enabled": False
    },
    "emoji_spam": {
        "enabled": False
    },
    "zalgo_text": {
        "enabled": False
    },

    "ignored_channels": [],
    "allowed_roles": []
}

DEFAULT_BANNED_WORDS = [
    'nigg', 'n1gg', 'n*gg',
    'cunt', 'bitch', 'dick',
    'pussy', 'asshole', 'b1tch',
    'b!tch', 'b*tch', 'blowjob',
    'cock', 'c0ck', 'faggot',
    'whore', 'negro', 'retard',
    'slut', 'rape', 'n i g g '
]

GLOBAL_CHAT_RULES = """
**Global chat rules:**

- No Racism, Sexism, Homophobia or anything stupid.
- No NSFW messages or pictures or emotes.
- Do not be rude to anyone.
- No spamming.
- No self promo.
- No malicious links.

**If your message has a "❌" reaction added, that means your message was not sent because you broke one of these rules.**

**If you break any of these rules, you WILL get blacklisted and won't be able to use the bot.**
If you see anyone breaking these rules please report them using the `report` command.
"""

ANTIHOIST_CHARS = "!@#$%^&*()_+-=.,/?;:[]{}`~\"'\\|<>"
