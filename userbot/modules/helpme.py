import re
import sys
from math import ceil

from telethon.sync import TelegramClient, custom, events

from userbot import (
    ALIVE_NAME,
    API_HASH,
    API_KEY,
    BOT_TOKEN,
    BOT_VER,
    BOTLOG_CHATID,
    CMD_HELP,
    LOGS,
    LOGSPAMMER,
    UPSTREAM_REPO_BRANCH,
    bot,
)


async def check_botlog_chatid():
    if not BOTLOG_CHATID and LOGSPAMMER:
        LOGS.info(
            "Anda harus menambahkan var BOTLOG_CHATID di config.env atau di var heroku, agar penyimpanan log error userbot pribadi berfungsi."
        )
        sys.exit(1)

    elif not BOTLOG_CHATID and BOTLOG:
        LOGS.info(
            "Anda harus menambahkan var BOTLOG_CHATID di config.env atau di var heroku, agar fitur logging userbot berfungsi."
        )
        sys.exit(1)

    elif not BOTLOG or not LOGSPAMMER:
        return

    entity = await bot.get_entity(BOTLOG_CHATID)
    if entity.default_banned_rights.send_messages:
        LOGS.info(
            "Akun Anda tidak bisa mengirim pesan ke BOTLOG_CHATID "
            "Periksa apakah Anda memasukan ID grup dengan benar."
        )
        sys.exit(1)


def paginate_help(page_number, loaded_modules, prefix):
    number_of_rows = 5
    number_of_cols = 4
    helpable_modules = [p for p in loaded_modules if not p.startswith("_")]
    helpable_modules = sorted(helpable_modules)
    modules = [
        custom.Button.inline("{} {} ✘".format("✘", x), data="ub_modul_{}".format(x))
        for x in helpable_modules
    ]
    pairs = list(
        zip(
            modules[::number_of_cols],
            modules[1::number_of_cols],
            modules[2::number_of_cols],
        )
    )
    if len(modules) % number_of_cols == 1:
        pairs.append((modules[-1],))
    max_num_pages = ceil(len(pairs) / number_of_rows)
    modulo_page = page_number % max_num_pages
    if len(pairs) > number_of_rows:
        pairs = pairs[
            modulo_page * number_of_rows : number_of_rows * (modulo_page + 1)
        ] + [
            (
                custom.Button.inline(
                    "««", data="{}_prev({})".format(prefix, modulo_page)
                ),
                custom.Button.inline("Tutup", b"close"),
                custom.Button.inline(
                    "»»", data="{}_next({})".format(prefix, modulo_page)
                ),
            )
        ]
    return pairs


with bot:
    try:
        tgbot = TelegramClient("TG_BOT_TOKEN", api_id=API_KEY, api_hash=API_HASH).start(
            bot_token=BOT_TOKEN
        )

        dugmeler = CMD_HELP
        me = bot.get_me()
        uid = me.id
        logo = ALIVE_LOGO

        @tgbot.on(events.NewMessage(pattern="/start"))
        async def handler(event):
            await event.message.get_sender()
            text = (
                f"**Hey**, __I am using__ 🔥 **Man-Userbot** 🔥\n\n"
                f"       __Thanks For Using me__\n\n"
                f"✣ **Userbot Version :** `{BOT_VER}@{UPSTREAM_REPO_BRANCH}`\n"
                f"✣ **Group Support :** [Sharing Userbot](t.me/sharinguserbot)\n"
                f"✣ **Owner Repo :** [Risman](t.me/mrismanaziz)\n"
                f"✣ **Repo :** [Man-Userbot](https://github.com/mrismanaziz/Man-Userbot)\n"
            )
            await tgbot.send_file(
                event.chat_id,
                logo,
                caption=text,
                buttons=[
                    [
                        custom.Button.url(
                            text="⛑ Group Support ⛑", url="https://t.me/SharingUserbot"
                        )
                    ]
                ],
            )

        @tgbot.on(events.InlineQuery)
        async def inline_handler(event):
            builder = event.builder
            result = None
            query = event.text
            if event.query.user_id == uid and query.startswith("@UserButt"):
                buttons = paginate_help(0, dugmeler, "helpme")
                result = builder.article(
                    "Harap Gunakan .help Untuk Perintah",
                    text="{}\n\n**✥ Jumlah Module Yang Tersedia :** `{}` **Module**\n               \n**✥ Daftar Modul Man-Userbot :** \n".format(
                        "**✗ Man-Userbot Main Menu ✗**",
                        len(dugmeler),
                    ),
                    buttons=buttons,
                    link_preview=False,
                )
            elif query.startswith("repo"):
                result = builder.article(
                    title="Repository",
                    description="Repository Man - Userbot",
                    url="https://t.me/SharingUserbot",
                    text="**Man - UserBot**\n➖➖➖➖➖➖➖➖➖➖\n✣ **Owner Repo :** [Risman](https://t.me/mrismanaziz)\n✣ **Grup Support :** @SharingUserbot\n✣ **Repository :** [Man-Userbot](https://github.com/mrismanaziz/Man-Userbot)\n➖➖➖➖➖➖➖➖➖➖",
                    buttons=[
                        [
                            custom.Button.url("Support", "https://t.me/SharingUserbot"),
                            custom.Button.url(
                                "Repo", "https://github.com/mrismanaziz/Man-Userbot"
                            ),
                        ],
                    ],
                    link_preview=False,
                )
            else:
                result = builder.article(
                    title="✗ Man-Userbot ✗",
                    description="Man - UserBot | Telethon",
                    url="https://t.me/SharingUserbot",
                    text="**Man - UserBot**\n➖➖➖➖➖➖➖➖➖➖\n✣ **Owner Repo :** [Risman](https://t.me/mrismanaziz)\n✣ **Grup Support :** @SharingUserbot\n✣ **Repository :** [Man-Userbot](https://github.com/mrismanaziz/Man-Userbot)\n➖➖➖➖➖➖➖➖➖➖",
                    buttons=[
                        [
                            custom.Button.url("Support", "https://t.me/SharingUserbot"),
                            custom.Button.url(
                                "Repo", "https://github.com/mrismanaziz/Man-Userbot"
                            ),
                        ],
                    ],
                    link_preview=False,
                )
            await event.answer([result] if result else None)

        @tgbot.on(
            events.callbackquery.CallbackQuery(
                data=re.compile(rb"helpme_next\((.+?)\)")
            )
        )
        async def on_plug_in_callback_query_handler(event):
            if event.query.user_id == uid:
                current_page_number = int(event.data_match.group(1).decode("UTF-8"))
                buttons = paginate_help(current_page_number + 1, dugmeler, "helpme")
                # https://t.me/TelethonChat/115200
                await event.edit(buttons=buttons)
            else:
                reply_pop_up_alert = (
                    f"Kamu Tidak diizinkan, ini Userbot Milik {ALIVE_NAME}"
                )
                await event.answer(reply_pop_up_alert, cache_time=0, alert=True)

        @tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"close")))
        async def on_plug_in_callback_query_handler(event):
            if event.query.user_id == uid:
                await event.edit("**Help Mode Button Ditutup!**")
            else:
                reply_pop_up_alert = (
                    f"Kamu Tidak diizinkan, ini Userbot Milik {ALIVE_NAME}"
                )
                await event.answer(reply_pop_up_alert, cache_time=0, alert=True)

        @tgbot.on(
            events.callbackquery.CallbackQuery(
                data=re.compile(rb"helpme_prev\((.+?)\)")
            )
        )
        async def on_plug_in_callback_query_handler(event):
            if event.query.user_id == uid:
                current_page_number = int(event.data_match.group(1).decode("UTF-8"))
                buttons = paginate_help(current_page_number - 1, dugmeler, "helpme")
                # https://t.me/TelethonChat/115200
                await event.edit(buttons=buttons)
            else:
                reply_pop_up_alert = (
                    f"Kamu Tidak diizinkan, ini Userbot Milik {ALIVE_NAME}"
                )
                await event.answer(reply_pop_up_alert, cache_time=0, alert=True)

        @tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"ub_modul_(.*)")))
        async def on_plug_in_callback_query_handler(event):
            if event.query.user_id == uid:
                modul_name = event.data_match.group(1).decode("UTF-8")

                cmdhel = str(CMD_HELP[modul_name])
                if len(cmdhel) > 150:
                    help_string = (
                        str(CMD_HELP[modul_name]).replace("`", "")[:150]
                        + "..."
                        + "\n\nBaca Teks Berikutnya Ketik .help "
                        + modul_name
                        + " "
                    )
                else:
                    help_string = str(CMD_HELP[modul_name]).replace("`", "")

                reply_pop_up_alert = (
                    help_string
                    if help_string is not None
                    else "{} Tidak ada dokumen yang telah ditulis untuk modul.".format(
                        modul_name
                    )
                )
            else:
                reply_pop_up_alert = (
                    f"Kamu Tidak diizinkan, ini Userbot Milik {ALIVE_NAME}"
                )

            await event.answer(reply_pop_up_alert, cache_time=0, alert=True)

    except BaseException:
        LOGS.info(
            "Help Mode Inline Bot Mu Tidak aktif. Tidak di aktifkan juga tidak apa-apa. "
            "Untuk Mengaktifkannya Buat bot di @BotFather Lalu Tambahkan var BOT_TOKEN dan BOT_USERNAME. "
            "Pergi Ke @BotFather lalu settings bot » Pilih mode inline » Turn On. "
        )
    try:
        bot.loop.run_until_complete(check_botlog_chatid())
    except BaseException:
        LOGS.info(
            "var BOTLOG_CHATID kamu belum di isi. "
            "Buatlah grup telegram dan masukan bot @MissRose_bot lalu ketik /id "
            "Masukan id grup nya di var BOTLOG_CHATID"
        )
        sys.exit(1)
