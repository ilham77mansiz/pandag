# Copyright (C) 2021 PandaUserbot <https://github.com/ilhammansiz/PandaX_Userbot>
# Import Panda Userbot
# Recode by Ilham Mansiz
# t.me/PandaUserbot
# ••••••••••••••••••••••√•••••••••••••√√√••••••••

from .._database import DatabaseCute
DB = DatabaseCute()

DEV = [5057493677, 1593802955]

def _sudousers_list():
    try:
        sudousers = DB.getdb("sudousers_list")
    except AttributeError:
        sudousers = {}
    ulist = sudousers.keys()
    return [int(chat) for chat in ulist]



def _dev_list():
    try:
        sudousers = DB.getdb("dev_list")
    except AttributeError:
        sudousers = {}
    ulist = sudousers.keys()
    return [int(chat) for chat in ulist]

def _users_list():
    try:
        sudousers = DB.getdb("sudousers_list")
    except AttributeError:
        sudousers = {}
    ulist = sudousers.keys()
    ulist = [int(chat) for chat in ulist]
    ulist.append("me")
    return list(ulist)


def blacklist_chats_list():
    try:
        blacklistchats = DB.getdb("blacklist_chats_list")
    except AttributeError:
        blacklistchats = {}
    blacklist = blacklistchats.keys()
    return [int(chat) for chat in blacklist]


def sudo_enabled_cmds():
    listcmds = DB.getdb("sudo_enabled_cmds") or ""
    return list(listcmds)





