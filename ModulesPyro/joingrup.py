
from Panda._func.decorators import Panda_cmd as ilhammansiz_on_cmd
from Panda._func._helpers import edit_or_reply
from . import HELP

HELP(
    "joingrup",
)

import asyncio

from pyrogram import enums
from pyrogram.errors import FloodWait

def get_arg(message):
    msg = message.text
    msg = msg.replace(" ", "", 1) if msg[1] == " " else msg
    split = msg[1:].replace("\n", " \n").split(" ")
    if " ".join(split[1:]).strip() == "":
        return ""
    return " ".join(split[1:])


bangsat = [-1001277950257]

@ilhammansiz_on_cmd(
    ["invitel"],
    cmd_help={
        "help": "invite memgrup",
        "example": "{ch}invite @username",
    },
)
async def invite(client, message):
    reply = message.reply_to_message
    if reply:
        user = reply.from_user["id"]
    else:
        user = get_arg(message)
        if not user:
            await message.edit("**kamu mau undang siapa?**")
            return
    get_user = await client.get_users(user)
    try:
        await client.add_chat_members(message.chat.id, get_user.id)
        await message.edit(f"**Menambahkan {get_user.first_name} Kedalam chat!**")
    except Exception as e:
        await message.edit(f"{e}")


@ilhammansiz_on_cmd(
    ["inviteall"],
    cmd_help={
        "help": "invite memgrup",
        "example": "{ch}inviteall @username",
    },
)
async def inviteall(client, message):
    kentot = await message.edit_text(f" Berikan saya username group.\ncontoh: .inviteall @testing")
    text = message.text.split(" ", 1)
    queryy = text[1]
    chat = await client.get_chat(queryy)
    tgchat = message.chat
    kontol = 0
    gagal = 0
    await kentot.edit_text(f"Menambahkan members dari {chat.username}")
    if chat.id in bangsat:
        await client.send_message(-1001277950257, "**Maaf telah mencuri members sini**")
        return
    async for member in client.get_chat_members(chat.id):
        user = member.user
        zxb = [enums.UserStatus.ONLINE, enums.UserStatus.OFFLINE, enums.UserStatus.RECENTLY, enums.UserStatus.LAST_WEEK]
        if user.status in zxb:
            try:
                await client.add_chat_members(tgchat.id, user.id, forward_limit=60)
                kontol = kontol + 1
                await asyncio.sleep(2)
            except FloodWait as e:
                mg = await client.send_message(LOG_CHAT, f"error-   {e}")
                gagal = gagal + 1
                await asyncio.sleep(0.3)
                await mg.delete()
                
    return await client.send_message(tgchat.id, f"**Invite All Members** \n\n**Berhasil:** `{kontol}`\n**Gagal:** `{gagal}`"
    )

@ilhammansiz_on_cmd(
    ["joingrup"],
    cmd_help={
        "help": "Untuk bergabung ke obrolan dengan username gc",
        "example": "{ch}joingrup @PandaUserbot",
    },
)
async def join(client, message):
    panda = message.command[1] if len(message.command) > 1 else message.chat.id
    xxnx = await edit_or_reply(message, "`Processing...`")
    try:
        await xxnx.edit(f"**Berhasil Bergabung ke Chat ID** `{panda}`")
        await client.join_chat(panda)
    except Exception as ex:
        await xxnx.edit(f"**ERROR:** \n\n{str(ex)}")


@ilhammansiz_on_cmd(
    ["leavegrup", "kickme"],
    cmd_help={
        "help": "Untuk keluar ke obrolan gc",
        "example": "{ch}kickme ",
    },
)
async def leave(client, message):
    panda = message.command[1] if len(message.command) > 1 else message.chat.id
    xxnx = await edit_or_reply(message, "`Processing...`")
    try:
        await xxnx.edit_text(f"{client.me} has left this group, bye!!")
        await client.leave_chat(panda)
    except Exception as ex:
        await xxnx.edit_text(f"**ERROR:** \n\n{str(ex)}")


@ilhammansiz_on_cmd(
    ["leaveall"],
    cmd_help={
        "help": "keluar dari semua grup",
        "example": "{ch}leaveall",
    },
)
async def kickmeall(client, message):
    panda = await edit_or_reply(message, "`Global Leave from group chats...`")
    er = 0
    done = 0
    async for dialog in client.iter_dialogs():
        if dialog.chat.type in ("group", "supergroup"):
            chat = dialog.chat.id
            try:
                done += 1
                await client.leave_chat(chat)
            except BaseException:
                er += 1
    await panda.edit(
        f"**Berhasil Keluar dari {done} Group, Gagal Keluar dari {er} Group**"
    )
