# Copyright (C) 2020 Catuserbot <https://github.com/sandy1709/catuserbot>
# Import Panda Userbot
# Recode by Ilham Mansiz
# ••••••••••••••••••••••√•••••••••••••√√√••••••••


import sys
import Panda
from Panda import utils
LOGS = Panda.core.logger.logging.getLogger("PandaUserbot")
from .utils import P, M, V, A
from .Session.multisession_ import Pyrogram, Telethon
from pyrogram import __version__ as pyrover

## Memulai ••••••••••√√√√√•••••••

try:
    LOGS.info(Panda.__copyright__)
    LOGS.info("Licensed under the terms of the " + Panda.__license__)
except Exception as e:
    LOGS.error(f"{e}")
    sys.exit()

## Install Modules ••••••√√√√√••••••

async def memulai():
    await utils.loads(f"{P}")
    await utils.loads(f"{M}")
    await utils.buka(f"{V}")
    await utils.buka(f"{A}")
    

def start():
    if Panda.PandaBot:
        Panda.PandaBot.loop.run_until_complete(memulai())
        Panda.PandaBot.loop.run_until_complete(utils.join())
        Panda.PandaBot.loop.run_until_complete(utils.ongrup())
        LOGS.info(f"꧁༺ Panda Userbot ༻꧂\n⚙️ Version:{Panda.__version__} [TELAH DIAKTIFKAN]")

Copy = f"""
**Panda-Userbot**
**Version -** `{pyrover}`
**Berbasis Pyrogram**
Dev by Ilham Mansiz
"""

def ongruppyro():
    try:
        if Panda.pyrobot:
            if Panda.BOTLOG_CHATID != 0:
                Panda.pyrobot.send_message(
                    Panda.BOTLOG_CHATID,
                    Copy,
                )
    except BaseException:
        pass

if __name__ == "__main__":
    Telethon()
    start()
    Pyrogram()
    ongruppyro()
  
if Panda.PandaBot:
    try:
        if len(sys.argv) not in (1, 3, 4):
            Panda.PandaBot.disconnect()
        else:
            Panda.PandaBot.run_until_disconnected()
    except Exception as e:
        LOGS.info(str(e), exc_info=True)
        sys.exit(1)
