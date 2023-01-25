from ..config import *


import sys
from telethon.network.connection.tcpabridged import ConnectionTcpAbridged
import logging
from telethon import TelegramClient
from pytgcalls import PyTgCalls


if SESSION:
    session = StringSession(str(Var.SESSION))
else:
    session = "PandaUserBot"
try:
    bot = TelegramClient(
        session=session,
        api_id=Var.API_ID,
        api_hash=Var.API_HASH,
        connection=ConnectionTcpAbridged,
        auto_reconnect=True,
        connection_retries=None,
    )
    call_py = PyTgCalls(bot)
except Exception as e:
    print(f"STRING_SESSION - {e}")
    sys.exit()

if SESSION2:
    session = StringSession(str(Var.SESSION2))
else:
    session = "PandaUserBot"
try:
    bot2 = TelegramClient(
        session=session,
        api_id=Var.API_ID,
        api_hash=Var.API_HASH,
        connection=ConnectionTcpAbridged,
        auto_reconnect=True,
        connection_retries=None,
    )
    call_py2 = PyTgCalls(bot2)
except Exception as e:
    print(f"STRING_SESSION - {e}")
    sys.exit()


if SESSION3:
    session = StringSession(str(Var.SESSION3))
else:
    session = "PandaUserBot"
try:
    bot3 = TelegramClient(
        session=session,
        api_id=Var.API_ID,
        api_hash=Var.API_HASH,
        connection=ConnectionTcpAbridged,
        auto_reconnect=True,
        connection_retries=None,
    )
    call_py3 = PyTgCalls(bot3)
except Exception as e:
    print(f"STRING_SESSION - {e}")
    sys.exit()


if SESSION4:
    session = StringSession(str(Var.SESSION4))
else:
    session = "PandaUserBot"
try:
    bot4 = TelegramClient(
        session=session,
        api_id=Var.API_ID,
        api_hash=Var.API_HASH,
        connection=ConnectionTcpAbridged,
        auto_reconnect=True,
        connection_retries=None,
    )
    call_py4 = PyTgCalls(bot4)
except Exception as e:
    print(f"STRING_SESSION - {e}")
    sys.exit()




if SESSION5:
    session = StringSession(str(Var.SESSION5))
else:
    session = "PandaUserBot"
try:
    bot5 = TelegramClient(
        session=session,
        api_id=Var.API_ID,
        api_hash=Var.API_HASH,
        connection=ConnectionTcpAbridged,
        auto_reconnect=True,
        connection_retries=None,
    )
    call_py5 = PyTgCalls(bot5)
except Exception as e:
    print(f"STRING_SESSION - {e}")
    sys.exit()


