import os
import re
from platform import python_version as kontol
from telethon import events, Button
from telegram import __version__ as telever
from telethon import __version__ as tlhver
from pyrogram import __version__ as pyrover
from PrimeMega.events import register
from PrimeMega import telethn as tbot


PHOTO = "https://telegra.ph/file/c3a27b7cefdf304e9e672.jpg"

@register(pattern=("/alive"))
async def awake(event):
  PRIME = f"**Hi [{event.sender.first_name}](tg://user?id={event.sender.id}), I'm 𝐬𝐲𝐚𝐬𝐚𝐗𝐫𝐨𝐛𝐨𝐭.** \n\n"
  PRIME += "⚪ **I'm Working Properly** \n\n"
  PRIME += f"⚪ **My Master : [muk](https://t.me/muk_aja)** \n\n"
  PRIME += f"⚪ **Library Version :** `{telever}` \n\n"
  PRIME += f"⚪ **Telethon Version :** `{tlhver}` \n\n"
  PRIME += f"⚪ **Pyrogram Version :** `{pyrover}` \n\n"
  PRIME += "**Thanks For Adding Me Here ❤️**"
  BUTTON = [[Button.url("ʜᴇʟᴘ​", "https://t.me/syasaaXrobot?start=help"), Button.url("sᴜᴘᴘᴏʀᴛ​", "https://t.me/PrimeSupportGroup")]]
  await tbot.send_file(event.chat_id, PHOTO, caption=PRIME,  buttons=BUTTON)
