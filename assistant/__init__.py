# ShizuUser - UserBot
# Copyright (C) 2021 TeamShizuUser
#
# This file is a part of < https://github.com/TeamShizu/ShizuUser/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/TeamShizu/ShizuUser/blob/main/LICENSE/>.

from pyShizuUser import *
from pyShizuUser.dB.database import Var
from pyShizuUser.functions.all import *
from telethon import Button, custom

from strings import get_languages, get_string

OWNER_NAME = ShizuUser_bot.me.first_name
OWNER_ID = ShizuUser_bot.me.id


async def setit(event, name, value):
    try:
        udB.set(name, value)
    except BaseException:
        return await event.edit("`Something Went Wrong`")


def get_back_button(name):
    button = [Button.inline("« Bᴀᴄᴋ", data=f"{name}")]
    return button
