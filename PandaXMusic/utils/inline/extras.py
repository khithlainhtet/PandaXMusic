from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from config import SUPPORT_CHAT


def botplaylist_markup(_):
    buttons = [
        [
            InlineKeyboardButton(text=_["S_B_9"], url=SUPPORT_CHAT),
            InlineKeyboardButton(text=_["💞Love Group💞"], url="https://t.me/myanmar_music_Bot2027"),
        ],
    ]
    return buttons


def close_markup(_):
    upl = InlineKeyboardMarkup(
        [
            [
                 InlineKeyboardButton(
                text="🥀 ꜱᴜᴘᴘᴏʀᴛ 🥀", url=f"https://t.me/myanmar_music_Bot2027"
            ),
                InlineKeyboardButton(
                    text=_["Music (panda)"],
                    url="https://t.me/PANDAMUSIC1_BOT?start=start",
                ),
            ]
        ]
    )
    return upl


def supp_markup(_):
    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text=_["S_B_9"],
                    url=SUPPORT_CHAT,
                ),
            ]
        ]
    )
    return upl
