#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (C) PR0FESSOR-99

import os
from config import Config
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

USERNAME=Config.BOT_USERNAME


# start_Msg, help_msg, about_msg
# Team Mo Tect
MT = "@Mo_Tech_YT"


@Client.on_message(filters.private & filters.command("start"))
async def start_meg(client, update):
    text = f"""<b> 👋Hello {update.from_user.mention}\n\nAn AutoCaption bot\n\nAll you have to do is to,add me to your channel and I will show you a miracle 😮\n\nFor more info check help \n\n {Help}</b>"""
    reply_markup =  InlineKeyboardMarkup( [[
        InlineKeyboardButton("help↗️", callback_data="heroku"),
        InlineKeyboardButton("🗣️Group", url="t.me/thewarriorsreal"),
        InlineKeyboardButton("Channel📢", url="t.me/defenderofthemultiverse")
        ]]
    )
    await update.reply_text(
        text=text,
        disable_web_page_preview=True,
        reply_markup=reply_markup
  )

@Client.on_callback_query(filters.regex(r"^(heroku|about|motech)$"))
async def callback_data(client, update: CallbackQuery):

    query_data = update.data

    if query_data == "heroku":
        buttons = [[
            InlineKeyboardButton("ꪮ᭙ꪀꫀ𝘳", url="https://t.me/ANKIT3690"),
            Inlinekeyboardbutton ("ꪮ᭙ꪀꫀ𝘳", url="https://t.me/Saurav3BV6SA9LLElon7Musk")
            ],[
            InlineKeyboardButton("🏠Home", url=f"https://t.me/{USERNAME}?start=start"),
            InlineKeyboardButton("❌️Close", callback_data="motech"),
            InlineKeyboardButton("About↗️", callback_data="about")
            ]]
    
        reply_markup = InlineKeyboardMarkup(buttons)

        await update.message.edit_text(
            f"""<b>🔻AutoCaption Bot🔻\n\nTake a look at the channel\nOnly Hollywood Movies Get Uploaded \n\nOne of the best channel/group\n\nHeroku 👉 https://dashboard.heroku.com/\n\n {MT}</b>""",
            reply_markup=reply_markup,
            parse_mode="html"
        )

    if query_data == "about":
        buttons = [[
            InlineKeyboardButton("🗣️Group", url="t.me/thewarriorsreal"),
            InlineKeyboardButton("Channel📢", url="t.me/defenderofthemultiverse"),
            InlineKeyboardButton("Owner", url="https://t.me/ANKIT3690")
            ],[
            InlineKeyboardButton("🏠Home", url=f"https://t.me/{USERNAME}?start=start"),
            InlineKeyboardButton("🔙Back", callback_data="heroku"),
            InlineKeyboardButton("❌️Close", callback_data="close")
            ]]
    
        reply_markup = InlineKeyboardMarkup(buttons)

        await update.message.edit_text(
            """<b>➪ Bot Name</b> AutoCaptionBot\n\n😎<b> ꪮ᭙ꪀꫀ𝘳: <a href="https://t.me/Saurav3BV6SA9LLElon7Musk">𝐒𝐀𝐔𝐑𝐀𝐕</a>\n\n😎 Owner : <a href="https://t.me/ANKIT3690">𝐀𝐍𝐊𝐈𝐓</a></b>""",
            reply_markup=reply_markup,
            parse_mode="html"
        )

    elif query_data == "motech":
        await update.message.delete()
