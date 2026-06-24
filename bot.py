import discord
from discord.ext import commands
from datetime import datetime
import os

# ══════════════════════════════════════════════════════
#   ⚔️  AFFCONQUER WELCOME BOT  by @OPANKUSHFF007
# ══════════════════════════════════════════════════════

TOKEN               = os.getenv("DISCORD_TOKEN", "YOUR_BOT_TOKEN_HERE")
WELCOME_CHANNEL_ID  = 1518883411971014786   # #general-chat (say hi here)
SERVER_INFO_CHANNEL = 1518880166284099684   # #server-info  (MC IP)
BANNER_GIF_URL      = ""                   # optional — paste imgur gif link

# ── Bot Setup ─────────────────────────────────────────
intents = discord.Intents.default()
intents.members         = True
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

# ── Helper ────────────────────────────────────────────
def ordinal(n: int) -> str:
    suffix = ["th","st","nd","rd"] + ["th"] * 16
    return f"{n}{suffix[n % 100 if 11 <= n % 100 <= 13 else n % 10]}"

# ══════════════════════════════════════════════════════
#   ON READY
# ══════════════════════════════════════════════════════
@bot.event
async def on_ready():
    print(f"\n  ⚔️  AFFCONQUER Bot online  |  {bot.user}")
    print(f"  👑  Servers: {len(bot.guilds)}")
    print(f"  🔥  The grind never stops.\n")
    await bot.change_presence(
        activity=discord.Activity(
            type=discord.ActivityType.watching,
            name="AFFCONQUER grow 👑"
        )
    )

# ══════════════════════════════════════════════════════
#   ON MEMBER JOIN
# ══════════════════════════════════════════════════════
@bot.event
async def on_member_join(member: discord.Member):
    guild   = member.guild
    channel = guild.get_channel(WELCOME_CHANNEL_ID)
    if channel is None:
        print(f"[WARN] Welcome channel not found: {WELCOME_CHANNEL_ID}")
        return

    count = guild.member_count

    embed = discord.Embed(
        description=(
            "```ansi\n"
            "\u001b[1;35m⚔️  A F F C O N Q U E R\u001b[0m\n"
            "```\n"
            "**You are now part of something bigger.**\n"
            "This is not just a server — it's a movement.\n"
            "Prove you belong here, soldier.\n\n"
            "*— AFFCONQUER*"
        ),
        color=0x7C3AED,
        timestamp=datetime.utcnow()
    )

    embed.set_author(
        name=f"👋  Welcome, {member.display_name}!",
        icon_url=member.display_avatar.url
    )
    embed.set_thumbnail(url=member.display_avatar.url)

    embed.add_field(
        name="🎉  You Are Member",
        value=f"```yaml\n#{ordinal(count)} to join AFFCONQUER!\n```",
        inline=False
    )
    embed.add_field(
        name="💬  Introduce Yourself",
        value=f"Say hi in <#{WELCOME_CHANNEL_ID}> — don't be shy!",
        inline=True
    )
    embed.add_field(
        name="🖥️  Join MC Server",
        value=f"Get the IP from <#{SERVER_INFO_CHANNEL}>",
        inline=True
    )
    embed.add_field(name="\u200b", value="\u200b", inline=False)
    embed.add_field(
        name="📜  Rules",
        value="Break them and you're **permanently out.** No second chances.",
        inline=True
    )
    embed.add_field(
        name="⚠️  Staff is Watching",
        value="Stay legendary or stay out.",
        inline=True
    )
    embed.add_field(name="\u200b", value="\u200b", inline=False)
    embed.add_field(
        name="👑  Built By",
        value="[@OPANKUSHFF007](https://youtube.com/@OPANKUSHFF007) — respect the house.",
        inline=False
    )
    embed.set_footer(
        text="⚔️ AFFCONQUER  •  The grind never stops",
        icon_url=guild.icon.url if guild.icon else None
    )
    if BANNER_GIF_URL:
        embed.set_image(url=BANNER_GIF_URL)

    view = WelcomeView(guild.id)

    spoiler = "||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||"
    await channel.send(
        content=f"{spoiler} @everyone {member.mention} just conquered the gates! ⚔️",
        embed=embed,
        view=view
    )
    print(f"[OK] Welcome sent → {member.display_name} (#{count})")


# ══════════════════════════════════════════════════════
#   BUTTONS
# ══════════════════════════════════════════════════════
class WelcomeView(discord.ui.View):
    def __init__(self, guild_id: int):
        super().__init__(timeout=None)
        self.add_item(discord.ui.Button(
            label="💬 Say Hi",
            style=discord.ButtonStyle.link,
            url=f"https://discord.com/channels/{guild_id}/{WELCOME_CHANNEL_ID}"
        ))
        self.add_item(discord.ui.Button(
            label="🖥️ Get MC IP",
            style=discord.ButtonStyle.link,
            url=f"https://discord.com/channels/{guild_id}/{SERVER_INFO_CHANNEL}"
        ))
        self.add_item(discord.ui.Button(
            label="📺 Subscribe",
            style=discord.ButtonStyle.link,
            url="https://youtube.com/@OPANKUSHFF007"
        ))


# ══════════════════════════════════════════════════════
#   RUN
# ══════════════════════════════════════════════════════
bot.run(TOKEN)
