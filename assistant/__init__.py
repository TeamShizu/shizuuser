# shizuuser - UserBot
# Copyright (C) 2021 TeamShizu
#
# This file is a part of < https://github.com/TeamShizu/shizuuser/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/TeamShizu/shizuuser/blob/main/LICENSE/>.

from pyshizuuser import *
from pyshizuuser.dB.database import Var
from pyshizuuser.functions.all import *
from telethon import Button, custom

from strings import get_languages, get_string

OWNER_NAME = shizuuser_bot.me.first_name
OWNER_ID = shizuuser_bot.me.id


async def setit(event, name, value):
    try:
        udB.set(name, value)
    except BaseException:
        return await event.edit("`Something Went Wrong`")


def get_back_button(name):
    button = [Button.inline("« Bᴀᴄᴋ", data=f"{name}")]
    return button
