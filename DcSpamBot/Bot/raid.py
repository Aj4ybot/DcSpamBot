
#
# Copyright (C) 2022-2023 by DeCode@Github, < https://github.com/TeamDeCode >.
#
# This file is part of < https://github.com/TeamDeCode/DcSpamBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/TeamDeCode/DcSpamBot/blob/main/LICENSE >
#
# All rights reserved.

import asyncio
import random
import asyncio
import time
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.types import Message
from pyrogram.errors import FloodWait
from pyrogram import filters, Client
from DcSpamBot import SUDO_USER as sudo_user
from DcSpamBot.Data.Cache import RAID, PROGROUPS, PORN, PORNS
from traceback import format_exc
from typing import Tuple

def get_user(message: Message, text: str) -> [int, str, None]:
    """Get User From Message"""
    if text is None:
        asplit = None
    else:
        asplit = text.split(" ", 1)
    user_s = None
    reason_ = None
    if message.reply_to_message:
        user_s = message.reply_to_message.from_user.id
        reason_ = text if text else None
    elif asplit is None:
        return None, None
    elif len(asplit[0]) > 0:
        if message.entities:
            if len(message.entities) == 1:
                required_entity = message.entities[0]
                if required_entity.type == "text_mention":
                    user_s = int(required_entity.user.id)
                else:
                    user_s = int(asplit[0]) if asplit[0].isdigit() else asplit[0]
        else:
            user_s = int(asplit[0]) if asplit[0].isdigit() else asplit[0]
        if len(asplit) == 2:
            reason_ = asplit[1]
    return user_s, reason_


async def edit_or_send_as_file(
    text: str,
    message: Message,
    client: Client,
    caption: str = "`Result!`",
    file_name: str = "result",
    parse_mode="md",
):
    """Send As File If Len Of Text Exceeds Tg Limit Else Edit Message"""
    if not text:
        await message.edit("`Wait, What?`")
        return
    if len(text) > 1024:
        await message.edit("`OutPut is Too Large, Sending As File!`")
        file_names = f"{file_name}.text"
        open(file_names, "w").write(text)
        await client.send_document(message.chat.id, file_names, caption=caption)
        await message.delete()
        if os.path.exists(file_names):
            os.remove(file_names)
        return
    else:
        return await message.edit(text, parse_mode=parse_mode)

def get_text(message: Message) -> [None, str]:
    """Extract Text From Commands"""
    text_to_return = message.text
    if message.text is None:
        return None
    if " " in text_to_return:
        try:
            return message.text.split(None, 1)[1]
        except IndexError:
            return None
    else:
        return None

@Client.on_message(filters.user(sudo_user) & filters.command(["raid"], [".", "!", "/"]))
async def raid(client: Client, message: Message):       
    sex = await message.reply_text("`Processing..`")
    quantity = message.command[1]
    text_ = get_text(message)
    spam_text = ' '.join(message.command[2:])
    user, reason = get_user(message, spam_text)
    failed = 0 
    try:
        userz = await client.get_users(user)
    except:
        await sex.edit(f"`404 : User Doesn't Exists In This Chat !`")
        return            
    if not text_:
        await sex.edit("`Who Should I Raid? You?`")
        return
    raid = random.choice(RAID) 
    blaze = f"[{userz.first_name}](tg://user?id={userz.id}) {raid}"
    quantity = int(quantity)

    if int(message.chat.id) in PROGROUPS:
        await sex.edit("`Baap Ke Group Me Spam Nahi!`")
        return    
    for _ in range(quantity):
        await asyncio.sleep(2)
        try:
            await client.send_message(message.chat.id, blaze)            
        except FloodWait as e:
            await asyncio.sleep(e.x)

@Client.on_message(filters.user(sudo_user) & filters.command(["pornspam"], [".", "!", "/"]))
async def raid(client: Client, message: Message):       
    sex = await message.reply_text("`Processing..`")
    quantity = message.command[1]
    text_ = get_text(message)
    failed = 0 
    quantity = int(quantity)

    if int(message.chat.id) in PROGROUPS:
        await sex.edit("`Baap Ke Group Me Spam Nahi!`")
        return    
    for _ in range(quantity):
        await asyncio.sleep(2)
        try:
            await message.reply_photo(photo=f"{random.choice(PORN)}")          
        except FloodWait as e:
            await asyncio.sleep(e.x)

