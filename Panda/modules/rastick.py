import random

from .. import CMD_HANDLER as cmd
from .. import CMD_HELP
from ..misc import deEmojify, edit_or_reply, pandacute


@pandacute(pattern="rst(?: |$)(.*)")
async def rastick(animu):
    text = animu.pattern_match.group(1)
    if not text:
        if animu.is_reply:
            text = (await animu.get_reply_message()).message
            xx = await edit_or_reply(animu, "`Processing...`")
        else:
            await animu.answer("**Tidak ada teks yang diberikan.**")
            return
    animus = [
        1,
        2,
        3,
        4,
        5,
        6,
        7,
        8,
        9,
        10,
        11,
        12,
        13,
        14,
        15,
        16,
        17,
        18,
        19,
        20,
        21,
        22,
        23,
        24,
        25,
        26,
        27,
        28,
        29,
        30,
        31,
        32,
        33,
        34,
        35,
        36,
        37,
        38,
        39,
        40,
        41,
        42,
        43,
        44,
        45,
        46,
        47,
        48,
        49,
        50,
        51,
        52,
        53,
        54,
        55,
        56,
        57,
        58,
        59,
        60,
        61,
        62,
        63,
    ]
    sticcers = await bot.inline_query(
        "stickerizerbot", f"#{random.choice(animus)}{(deEmojify(text))}"
    )
    try:
        await sticcers[0].click(
            animu.chat_id,
            reply_to=animu.reply_to_msg_id,
            silent=bool(animu.is_reply),
            hide_via=True,
        )

    except Exception:
        return await edit_delete(
            xx,
            "**You cannot send inline results in this chat**"
        )
    await xx.delete()


CMD_HELP.update(
    {
        "rastick": f"**Plugin : **`rastick`\
        \n\n  ➕  **Syntax :** `{cmd}rst`\
        \n  ➕  **Function : **Untuk membuat stiker teks Anda dengan template stiker acak dari @StickerizerBot\
    "
    }
)