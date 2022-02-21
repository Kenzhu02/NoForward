import os
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import time 

Bot = Client(
    "Forward remove bot",
    bot_token=os.environ.get("BOT_TOKEN"),
    api_id=int(os.environ.get("API_ID")),
    api_hash=os.environ.get("API_HASH")
)

START_TXT = """Hello {},
Saya adalah bot penghapus pesan Terusan Otomatis sederhana
➣ Tambahkan saya ke grup Anda dan jadikan saya sebagai admin.
➣ Saya hanya akan menghapus pesan dengan terusan.

**Dibuat Oleh @TripleNineee**
"""

START_BUTTONS = InlineKeyboardMarkup(
    [[
        InlineKeyboardButton("Tambahkan saya kegroup", url="https://t.me/ZhuXAntichannelBot?startgroup=true")
    ]]
)

@Bot.on_message(filters.command("start"))
async def start(bot, message):
    m=await message.reply_text("▰▱▱")
    n=await m.edit("▰▰▱")
    o=await n.edit("▰▰▰")
    await o.edit(
        text=START_TXT.format(message.from_user.mention),
        reply_markup=START_BUTTONS,
    )

@Bot.on_message(filters.forwarded)
async def forward(bot, message):
    await message.delete("⛔ Pesan terusan telah dihapus")
    await message.delete()

Bot.run()
