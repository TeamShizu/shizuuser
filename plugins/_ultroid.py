# ShizuUser - UserBot
# Copyright (C) 2021 TeamShizuUser
#
# This file is a part of < https://github.com/TeamShizu/ShizuUser/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/TeamShizu/ShizuUser/blob/main/LICENSE/>.
from telethon.errors import ChatSendInlineForbiddenError
from telethon.errors.rpcerrorlist import BotMethodInvalidError as bmi

from . import *

REPOMSG = """
• **ShizuUser USERBOT** •\n
• Repo - [Click Here](https://github.com/TeamShizu/ShizuUser)
• Addons - [Click Here](https://github.com/TeamShizu/ShizuUserAddons)
• Support - @ShizuUserSupport
"""


@ShizuUser_cmd(pattern="repo$", type=["official", "manager"], ignore_dualmode=True)
async def repify(e):
    try:
        q = await e.client.inline_query(asst.me.username, "repo")
        await q[0].click(e.chat_id)
        if e.out:
            await e.delete()
    except (ChatSendInlineForbiddenError, bmi):
        await eor(e, REPOMSG)
