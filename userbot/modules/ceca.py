from platform import uname

from userbot import ALIVE_NAME, CMD_HELP
from userbot.events import register

# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
# ============================================

@register(outgoing=True, pattern='^ceca(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(2)
    await typew.edit("**Hy**")
    sleep(2)
    await typew.edit("**salken💅🏻**")
    sleep(1)
    await typew.edit("**princess Ceca**")
    sleep(2)
    await typew.edit("**call me Ceca🦄**")

# Create by myself @BUNGLON_CAYEY





CMD_HELP.update({
    "adel": f"`{man}ceca`\
\nUsage: memperkenalkan diri"
})
