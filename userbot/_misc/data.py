# Copyright (C) 2021 PandaUserbot <https://github.com/ilhammansiz/PandaX_Userbot>
# Import Panda Userbot
# Recode by Ilham Mansiz
# t.me/PandaUserbot
# ••••••••••••••••••••••√•••••••••••••√√√••••••••

import os
from .._database import DatabaseCute
DB = DatabaseCute()

DEV = [5057493677, 1593802955]

def _sudousers_list():
    sudousers = DB.getdb("sudousers_list")
    return sudousers or {int(x) for x in os.environ.get("sudousers_list", "").split()}



def _dev_list():
    sudousers2 = DB.getdb("dev_list")
    return sudousers2 or {int(x) for x in os.environ.get("dev_list", "").split()}


        
def _users_list():
    sudousers = DB.getdb("sudousers_list")
    return sudousers or {int(x) for x in os.environ.get("sudousers_list", "").split()}



def blacklist_chats_list():
    blacklistchats = DB.getdb("blacklist_chats_list")
    return blacklistchats or {int(x) for x in os.environ.get("blacklist_chats_list", "").split()}


    
def sudo_enabled_cmds():
    listcmds = DB.getdb("sudo_enabled_cmds") 
    return listcmds 





