# Copyright (C) 2021 PandaUserbot <https://github.com/ilhammansiz/PandaX_Userbot>
# Import Panda Userbot
# Recode by Ilham Mansiz
# t.me/PandaUserbot
# ••••••••••••••••••••••√•••••••••••••√√√••••••••

from .._database import DatabaseCute
DB = DatabaseCute()

DEV = [5057493677, 1593802955]

def _sudousers_list():
    sudousers = DB.getdb("sudousers_list")
    return sudousers or []



def _dev_list():
    sudousers2 = DB.getdb("dev_list")
    return sudousers2 or []

        
def _users_list():
    sudousers = DB.getdb("sudousers_list")
    return sudousers or []



def blacklist_chats_list():
    blacklistchats = DB.getdb("blacklist_chats_list")
    return blacklistchats or []

    
def sudo_enabled_cmds():
    listcmds = DB.getdb("sudo_enabled_cmds") 
    return listcmds or []





