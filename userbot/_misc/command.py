
# Credits: @mrconfused

import asyncio
import inspect
import re
from pathlib import Path

from telethon import events
from telethon.errors import (
    AlreadyInConversationError,
    BotInlineDisabledError,
    BotResponseTimeoutError,
    ChatSendInlineForbiddenError,
    ChatSendMediaForbiddenError,
    ChatSendStickersForbiddenError,
    FloodWaitError,
    MessageIdInvalidError,
    MessageNotModifiedError,
)

from .. import (
    BL_CHAT,
    CMD_HANDLER,
    CMD_LIST,
    LOAD_PLUG,
    LOGS,
    bot2,
    bot3,
    bot4,
    bot5,
    SUDO_HANDLER,
    SUDO_USERS,
    bot,
)

from .event import eod

edit_delete = eod

def mansiz_cmd(
    pattern: str = None,
    allow_sudo: bool = True,
    group_only: bool = False,
    admins_only: bool = False,
    private_only: bool = False,
    disable_edited: bool = False,
    forword=False,
    command: str = None,
    **args,
):
    args["func"] = lambda e: e.via_bot_id is None
    stack = inspect.stack()
    previous_stack_frame = stack[1]
    file_test = Path(previous_stack_frame.filename)
    file_test = file_test.stem.replace(".py", "")

    if "disable_edited" in args:
        del args["disable_edited"]

    args["blacklist_chats"] = True
    black_list_chats = list(BL_CHAT)
    if len(black_list_chats) > 0:
        args["chats"] = black_list_chats

    if pattern is not None:
        global _reg
        global sudo_reg
        if (
            pattern.startswith(r"\#")
            or not pattern.startswith(r"\#")
            and pattern.startswith(r"^")
        ):
            _reg = sudo_reg = re.compile(pattern)
        else:
            _ = "\\" + CMD_HANDLER
            sudo_ = "\\" + SUDO_HANDLER
            _reg = re.compile(_ + pattern)
            sudo_reg = re.compile(sudo_ + pattern)
            if command is not None:
                cmd1 = _ + command
                cmd2 = sudo_ + command
            else:
                cmd1 = (
                    (_ + pattern).replace("$", "").replace("\\", "").replace("^", "")
                )
                cmd2 = (
                    (sudo_ + pattern)
                    .replace("$", "")
                    .replace("\\", "")
                    .replace("^", "")
                )
            try:
                CMD_LIST[file_test].append(cmd1)
            except BaseException:
                CMD_LIST.update({file_test: [cmd1]})

    def decorator(func):
        async def wrapper(event):
            chat = event.chat
            if admins_only:
                if event.is_private:
                    return await edit_delete(
                        event, "**Perintah ini hanya bisa digunakan di grup.**", 10
                    )
                if not (chat.admin_rights or chat.creator):
                    return await edit_delete(
                        event, f"**Maaf anda bukan admin di {chat.title}**", 10
                    )
            if group_only and not event.is_group:
                return await edit_delete(
                    event, "**Perintah ini hanya bisa digunakan di grup.**", 10
                )
            if private_only and not event.is_private:
                return await edit_delete(
                    event, "**Perintah ini hanya bisa digunakan di private chat.**", 10
                )
            try:
                await func(event)
            except MessageNotModifiedError as er:
                LOGS.error(er)
            except MessageIdInvalidError as er:
                LOGS.error(er)
            except BotInlineDisabledError:
                await edit_delete(
                    event, "**Silahkan aktifkan mode Inline untuk bot**", 10
                )
            except ChatSendStickersForbiddenError:
                await edit_delete(
                    event, "**Tidak dapat mengirim stiker di obrolan ini**", 10
                )
            except BotResponseTimeoutError:
                await edit_delete(
                    event, "**The bot didnt answer to your query in time**"
                )
            except ChatSendMediaForbiddenError:
                await edit_delete(
                    event, "**Tidak dapat mengirim media dalam obrolan ini**", 10
                )
            except AlreadyInConversationError:
                await edit_delete(
                    event,
                    "**Percakapan sudah terjadi dengan obrolan yang diberikan. coba lagi setelah beberapa waktu.**",
                )
            except ChatSendInlineForbiddenError:
                await edit_delete(
                    event,
                    "**Tidak dapat mengirim pesan inline dalam obrolan ini.**",
                    10,
                )
            except FloodWaitError as e:
                LOGS.error(
                    f"Telah Terjadi flood wait error tunggu {e.seconds} detik dan coba lagi"
                )
                await event.delete()
                await asyncio.sleep(e.seconds + 5)
            except events.StopPropagation:
                raise events.StopPropagation
            except KeyboardInterrupt:
                pass
            except BaseException as e:
                LOGS.exception(e)

        if bot:
            if not disable_edited:
                bot.add_event_handler(
                    wrapper,
                    events.MessageEdited(**args, outgoing=True, pattern=_reg),
                )
            bot.add_event_handler(
                wrapper, events.NewMessage(**args, outgoing=True, pattern=_reg)
            )
        if bot:
            if allow_sudo:
                if not disable_edited:
                    bot.add_event_handler(
                        wrapper,
                        events.MessageEdited(
                            **args, from_users=list(SUDO_USERS), pattern=sudo_reg
                        ),
                    )
                bot.add_event_handler(
                    wrapper,
                    events.NewMessage(
                        **args, from_users=list(SUDO_USERS), pattern=sudo_reg
                    ),
                )
        if bot2:
            if not disable_edited:
                bot2.add_event_handler(
                    wrapper,
                    events.MessageEdited(**args, outgoing=True, pattern=_reg),
                )
            bot2.add_event_handler(
                wrapper, events.NewMessage(**args, outgoing=True, pattern=_reg)
            )
        if bot3:
            if not disable_edited:
                bot3.add_event_handler(
                    wrapper,
                    events.MessageEdited(**args, outgoing=True, pattern=_reg),
                )
            bot3.add_event_handler(
                wrapper, events.NewMessage(**args, outgoing=True, pattern=_reg)
            )
        if bot4:
            if not disable_edited:
                bot4.add_event_handler(
                    wrapper,
                    events.MessageEdited(**args, outgoing=True, pattern=_reg),
                )
            bot4.add_event_handler(
                wrapper, events.NewMessage(**args, outgoing=True, pattern=_reg)
            )
        if bot5:
            if not disable_edited:
                bot5.add_event_handler(
                    wrapper,
                    events.MessageEdited(**args, outgoing=True, pattern=_reg),
                )
            bot5.add_event_handler(
                wrapper, events.NewMessage(**args, outgoing=True, pattern=_reg)
            )
        try:
            LOAD_PLUG[file_test].append(wrapper)
        except Exception:
            LOAD_PLUG.update({file_test: [wrapper]})
        return wrapper

    return decorator


def man_handler(
    **args,
):
    def decorator(func):
        if bot:
            bot.add_event_handler(func, events.NewMessage(**args))
        if bot2:
            bot2.add_event_handler(func, events.NewMessage(**args))
        if bot3:
            bot3.add_event_handler(func, events.NewMessage(**args))
        if bot4:
            bot.add_event_handler(func, events.NewMessage(**args))
        if bot5:
            bot5.add_event_handler(func, events.NewMessage(**args))
        return func

    return decorator




def chataction(**args):
    def decorator(func):
        if bot:
            bot.add_event_handler(func, events.ChatAction(**args))
        if bot2:
            bot2.add_event_handler(func, events.ChatAction(**args))
        if bot3:
            bot3.add_event_handler(func, events.ChatAction(**args))
        if bot4:
            bot4.add_event_handler(func, events.ChatAction(**args))
        if bot5:
            bot5.add_event_handler(func, events.ChatAction(**args))
        return func

    return decorator


