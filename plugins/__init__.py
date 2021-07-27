# shizuuser - UserBot
# Copyright (C) 2021 TeamShizu
#
# This file is a part of < https://github.com/TeamShizu/shizuuser/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/TeamShizu/shizuuser/blob/main/LICENSE/>.

import asyncio
import time

from pyshizuuser import *
from pyshizuuser.dB import *
from pyshizuuser.functions.all import *
from pyshizuuser.functions.sudos import *
from pyshizuuser.version import shizuuser_version
from telethon import Button
from telethon.tl import functions, types

from strings import get_string

try:
    import glitch_me
except ModuleNotFoundError:
    os.system(
        "git clone https://github.com/1Danish-00/glitch_me.git && pip install -e ./glitch_me"
    )


start_time = time.time()

OWNER_NAME = shizuuser_bot.me.first_name
OWNER_ID = shizuuser_bot.me.id

List = []
Dict = {}
N = 0

NOSPAM_CHAT = [
    -1001387666944,  # @PyrogramChat
    -1001109500936,  # @TelethonChat
    -1001050982793,  # @Python
    -1001256902287,  # @DurovsChat
]

KANGING_STR = [
    "Using Witchery to kang this sticker...",
    "Plagiarising hehe...",
    "Inviting this sticker over to my pack...",
    "Kanging this sticker...",
    "Hey that's a nice sticker!\nMind if I kang?!..",
    "Hehe me stel ur stiker...",
    "Ay look over there (☉｡☉)!→\nWhile I kang this...",
    "Roses are red violets are blue, kanging this sticker so my pack looks cool",
    "Imprisoning this sticker...",
    "Mr.Steal-Your-Sticker is stealing this sticker... ",
]
