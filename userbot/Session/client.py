from ..config import *


import sys
from telethon.network.connection.tcpabridged import ConnectionTcpAbridged
import logging
from telethon import TelegramClient
from pytgcalls import PyTgCalls


try:
    if SESSION:
        session = StringSession(str(Var.SESSION))
        bot = TelegramClient(
            session=session,
            api_id=Var.API_ID,
            api_hash=Var.API_HASH,
            connection=ConnectionTcpAbridged,
            auto_reconnect=True,
            connection_retries=None,
        )
        call_py = PyTgCalls(bot)
    else:
        bot = None
        call_py = None
except Exception as e:
    print(f"STRING_SESSION - {e}")
    sys.exit()


try:
    if SESSION2:
        session2 = StringSession(str(Var.SESSION2))
        bot2 = TelegramClient(
            session=session2,
            api_id=Var.API_ID,
            api_hash=Var.API_HASH,
            connection=ConnectionTcpAbridged,
            auto_reconnect=True,
            connection_retries=None,
        )
        call_py2 = PyTgCalls(bot2)
    else:
        bot2 = None
        call_py2 = None
except Exception as e:
    print(f"STRING_SESSION2 - {e}")
    sys.exit()


try:
    if SESSION3:
        session3 = StringSession(str(Var.SESSION3))
        bot2 = TelegramClient(
            session=session3,
            api_id=Var.API_ID,
            api_hash=Var.API_HASH,
            connection=ConnectionTcpAbridged,
            auto_reconnect=True,
            connection_retries=None,
        )
        call_py3 = PyTgCalls(bot3)
    else:
        bot3 = None
        call_py3 = None
except Exception as e:
    print(f"STRING_SESSION3 - {e}")
    sys.exit()


try:
    if SESSION4:
        session4 = StringSession(str(Var.SESSION4))
        bot4 = TelegramClient(
            session=session4,
            api_id=Var.API_ID,
            api_hash=Var.API_HASH,
            connection=ConnectionTcpAbridged,
            auto_reconnect=True,
            connection_retries=None,
        )
        call_py4 = PyTgCalls(bot4)
    else:
        bot4 = None
        call_py4 = None
except Exception as e:
    print(f"STRING_SESSION4 - {e}")
    sys.exit()



try:
    if SESSION5:
        session5 = StringSession(str(Var.SESSION5))
        bot5 = TelegramClient(
            session=session5,
            api_id=Var.API_ID,
            api_hash=Var.API_HASH,
            connection=ConnectionTcpAbridged,
            auto_reconnect=True,
            connection_retries=None,
        )
        call_py5 = PyTgCalls(bot5)
    else:
        bot5 = None
        call_py5 = None
except Exception as e:
    print(f"STRING_SESSION5 - {e}")
    sys.exit()
