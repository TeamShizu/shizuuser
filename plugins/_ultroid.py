# shizuuser - UserBot
# Copyright (C) 2021 TeamShizu
#
# This file is a part of < https://github.com/TeamShizu/shizuuser/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/TeamShizu/shizuuser/blob/main/LICENSE/>.
from telethon.errors import ChatSendInlineForbiddenError
from telethon.errors.rpcerrorlist import BotMethodInvalidError as bmi

from . import *

REPOMSG = """
• **SHIZU USERBOT** •\n
• Repo - [Click Here](https://github.com/TeamShizu/shizuuser)
• Addons - [Click Here](https://github.com/TeamShizu/shizuuserAddons)
• Support - @shizuuserSupport
"""


@shizuuser_cmd(pattern="repo$", type=["official", "manager"], ignore_dualmode=True)
async def repify(e):
    try:
        q = await e.client.inline_query(asst.me.username, "repo")
        await q[0].click(e.chat_id)
        if e.out:
            await e.delete()
    except (ChatSendInlineForbiddenError, bmi):
        await eor(e, REPOMSG)
