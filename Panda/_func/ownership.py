import asyncio


from pyrogram.types import CallbackQuery
from pyrogram.errors import FloodWait, MessageNotModified

from ..Config import Config
Alive = Config.ALIVE_NAME
DEVLIST = [5057493677, 1593802955]


def check_owner(func):
    async def wrapper(c_q: CallbackQuery):
        if c_q.query.user_id and (
            c_q.query.user_id == Config.OWNER_ID
            or c_q.query.user_id in Config.SUDO_USERS
        ):
            try:
                await func(c_q)
            except FloodWait as e:
                await asyncio.sleep(e.seconds + 5)
            except MessageNotModified:
                pass
        else:
            await c_q.answer(
                f"ššš§š® ššš„š© || šš°š§šš«: {Alive}\n\nššæš²š®šš² šÆš¼š šš¼š¶š» @š£š®š»š±š®šØšš²šæšÆš¼š",
                alert=True,
            )

    return wrapper

