# ShizuUser - UserBot
# Copyright (C) 2021 TeamShizuUser
#
# This file is a part of < https://github.com/TeamShizu/ShizuUser/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/TeamShizu/ShizuUser/blob/main/LICENSE/>.

from datetime import datetime


@asst_cmd("ping$")
@owner
async def _(event):
    start = datetime.now()
    end = datetime.now()
    ms = (end - start).microseconds / 1000
    await asst.send_message(
        event.chat_id,
        f"**Pong!!**\n `{ms} milliseconds`",
    )
