from time import sleep

from userbot import BLACKLIST_CHAT, CMD_HELP
from userbot.events import register


@register(outgoing=True, pattern=r"^\.sayang(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(3)
    await typew.edit("**Cuma Mau Bilang**")
    sleep(3)
    await typew.edit("**Aku Sayang Kamu**")
    sleep(1)
    await typew.edit("**I LOVE YOU 💞**")


@register(outgoing=True, pattern=r"^\.ceca(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1.5)
    await typew.edit("**Hy**")
    sleep(1.5)
    await typew.edit("**salken💅🏻**")
    sleep(1.5)
    await typew.edit("**princess ceca🦄**")
    sleep(1.5)
    await typew.edit("**call me ceca🐻**")


# Create by myself @localheart


@register(outgoing=True, pattern=r"^\.semangat(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(3)
    await typew.edit("**Apapun Yang Terjadi**")
    sleep(3)
    await typew.edit("**Tetaplah Bernapas**")
    sleep(1)
    await typew.edit("**Dan Selalu Bersyukur**")


# Create by myself @localheart


@register(outgoing=True, pattern=r"^\.ywc(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**Ok Sama Sama**")


@register(outgoing=True, pattern=r"^\.jamet(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**WOII**")
    sleep(1.5)
    await typew.edit("**JAMET**")
    sleep(1.5)
    await typew.edit("**CUMA MAU BILANG**")
    sleep(1.5)
    await typew.edit("**GAUSAH SO ASIK**")
    sleep(1.5)
    await typew.edit("**EMANG KENAL?**")
    sleep(1.5)
    await typew.edit("**GAUSAH REPLY**")
    sleep(1.5)
    await typew.edit("**KITA BUKAN KAWAN**")
    sleep(1.5)
    await typew.edit("**GASUKA PC ANJING**")
    sleep(1.5)
    await typew.edit("**BOCAH KAMPUNG**")
    sleep(1.5)
    await typew.edit("**MENTAL TEMPE**")
    sleep(1.5)
    await typew.edit("**LEMBEK NGENTOT🔥**")


@register(outgoing=True, pattern=r"^\.pp(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit(
        "**PASANG PP DULU GOBLOK,BIAR ORANG-ORANG PADA TAU BETAPA HINA NYA MUKA LU 😆**"
    )


@register(outgoing=True, pattern=r"^\.dp(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**MUKA LU HINA, GAUSAH SOK KERAS YA ANJENGG!!**")


@register(outgoing=True, pattern=r"^\.so(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**GAUSAH SOKAB SAMA GUA GOBLOK, LU BABU GA LEVEL!!**")


@register(outgoing=True, pattern=r"^\.nb(?: |$)(.*)")
async def typewriter(typew):
    if typew.chat_id in BLACKLIST_CHAT:
        return await typew.edit("**Perintah ini Dilarang digunakan di Group ini**")
    typew.pattern_match.group(1)
    await typew.edit("**MAEN BOT MULU ALAY NGENTOTT, KESANNYA NORAK GOBLOK!!!**")


@register(outgoing=True, pattern=r"^\.met(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**NAMANYA JUGA JAMET CAPER SANA SINI BUAT CARI NAMA**")


@register(outgoing=True, pattern=r"^\.war(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit(
        "**WAR WAR PALAK BAPAK KAU WAR, SOK KERAS BANGET GOBLOK, DI TONGKRONGAN JADI BABU, DI TELE SOK JAGOAN...**"
    )


@register(outgoing=True, pattern=r"^\.wartai(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit(
        "**WAR WAR TAI ANJING, KETRIGGER MINTA SHARELOK LU KIRA MAU COD-AN GOBLOK, BACOTAN LU AJA KGA ADA KERAS KERASNYA GOBLOK**"
    )


@register(outgoing=True, pattern=r"^\.kismin(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit(
        "**CUIHHHH, MAKAN AJA MASIH NGEMIS LO GOBLOK, JANGAN SO NINGGI YA KONTOL GA KEREN LU KEK GITU GOBLOK!!**"
    )


@register(outgoing=True, pattern=r"^\.ded(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**MATI AJA LU GOBLOK, GAGUNA LU HIDUP DI BUMI**")


@register(outgoing=True, pattern=r"^\.sokab(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit(
        "**SOKAB BET LU GOBLOK, KAGA ADA ISTILAH NYA BAWAHAN TEMENAN AMA BOS!!**"
    )


@register(outgoing=True, pattern=r"^\.gembel(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit(
        "**MUKA BAPAK LU KEK KELAPA SAWIT ANJING, GA USAH NGATAIN ORANG, MUKA LU AJA KEK GEMBEL TEXAS GOBLOK!!**"
    )


@register(outgoing=True, pattern=r"^\.cuih(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit(
        "**GAK KEREN LO KEK BEGITU GOBLOK, KELUARGA LU BAWA SINI GUA LUDAHIN SATU-SATU. CUIHH!!!**"
    )


@register(outgoing=True, pattern=r"^\.dih(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit(
        "**DIHHH NAJISS ANAK HARAM LO GOBLOK, JANGAN BELAGU DIMARI KAGA KEREN LU KEK BGITU TOLOL!**"
    )


@register(outgoing=True, pattern=r"^\.gcs(?: |$)(.*)")
async def typewriter(typew):
    if typew.chat_id in BLACKLIST_CHAT:
        return await typew.edit("**Perintah ini Dilarang digunakan di Group ini**")
    typew.pattern_match.group(1)
    await typew.edit("**GC SAMPAH KAYA GINI, BUBARIN AJA GOBLOK!!**")


@register(outgoing=True, pattern=r"^\.skb(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**EMANG KITA KENAL? KAGA GOBLOK SOKAB BANGET LU GOBLOK**")


@register(outgoing=True, pattern=r"^\.virtual(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**OOOO**")
    sleep(1.5)
    await typew.edit("**INI YANG VIRTUAL**")
    sleep(1.5)
    await typew.edit("**YANG KATANYA SAYANG BANGET**")
    sleep(1.5)
    await typew.edit("**TAPI TETEP AJA DI TINGGAL**")
    sleep(1.5)
    await typew.edit("**NI INGET**")
    sleep(1.5)
    await typew.edit("**TANGANNYA AJA GA BISA DI PEGANG**")
    sleep(1.5)
    await typew.edit("**APALAGI OMONGANNYA**")
    sleep(1.5)
    await typew.edit("**BHAHAHAHA**")
    sleep(1.5)
    await typew.edit("**KASIAN MANA MASIH MUDA**")


CMD_HELP.update(
    {
        "war": "**Plugin : **`war`\
        \n\n  •  **Syntax :** `.jamet`\
        \n  •  **Function : **Menghina Jamet telegram\
        \n\n  •  **Syntax :** `.pp`\
        \n  •  **Function : **Menghina Jamet telegram yang ga pake foto profil\
        \n\n  •  **Syntax :** `.dp`\
        \n  •  **Function : **Menghina Jamet muka hina!\
        \n\n  •  **Syntax :** `.so`\
        \n  •  **Function : **Ngeledek orang sokab\
        \n\n  •  **Syntax :** `.nb`\
        \n  •  **Function : **Ngeledek orang norak baru pake bot\
        \n\n  •  **Syntax :** `.so`\
        \n  •  **Function : **Ngeledek orang sokab\
        \n\n  •  **Syntax :** `.skb`\
        \n  •  **Function : **Ngeledek orang sokab versi 2\
        \n\n  •  **Syntax :** `.met`\
        \n  •  **Function : **Ngeledek si jamet caper\
        \n\n  •  **Syntax :** `.war`\
        \n  •  **Function : **Ngeledek orang so keras ngajak war\
        \n\n  •  **Syntax :** `.wartai`\
        \n  •  **Function : **Ngeledek orang so ketrigger ngajak cod minta sharelok\
        \n\n  •  **Syntax :** `.kismin`\
        \n  •  **Function : **Ngeledek orang kismin so jagoan di tele\
        \n\n  •  **Syntax :** `.ded`\
        \n  •  **Function : **Nyuruh orang mati aja goblok wkwk\
        \n\n  •  **Syntax :** `.sokab`\
        \n  •  **Function : **Ngeledek orang so kenal so dekat padahal kga kenal goblok\
        \n\n  •  **Syntax :** `.gembel`\
        \n  •  **Function : **Ngeledek bapaknya si jamet\
        \n\n  •  **Syntax :** `.cuih`\
        \n  •  **Function : **Ngeludahin keluarganya satu satu wkwk\
        \n\n  •  **Syntax :** `.dih`\
        \n  •  **Function : **Ngeledek anak haram\
        \n\n  •  **Syntax :** `.gcs`\
        \n  •  **Function : **Ngeledek gc sampah\
        \n\n  •  **Syntax :** `.virtual`\
        \n  •  **Function : **Ngeledek orang pacaran virtual\
        \n\n**Klo mau Req, kosa kata dari lu Bisa pake Module costum. Ketik** `.help costum`\
    "
    }
)
