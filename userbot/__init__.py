from .Session import *
from ._database import DatabaseCute
DB = DatabaseCute()




















#####
import os
SUDO_USERS = {int(x) for x in os.environ.get("SUDO_USERS", "").split()}
BL_CHAT = {int(x) for x in os.environ.get("BL_CHAT", "").split()}
CMD_HANDLER = os.environ.get("CMD_HANDLER") or "."
SUDO_HANDLER = os.environ.get("SUDO_HANDLER", r"?")

COUNT_MSG = 0
USERS = {}
COUNT_PM = {}
LASTMSG = {}
CMD_HELP = {}
CMD_LIST = {}
SUDO_LIST = {}
ZALG_LIST = {}
LOAD_PLUG = {}
INT_PLUG = ""
ISAFK = False
AFKREASON = None
ENABLE_KILLME = True


###
