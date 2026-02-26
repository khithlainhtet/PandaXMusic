from pyrogram.types import InlineKeyboardButton
import config
from PandaXMusic import app

def start_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_1"], url=f"https://t.me/{app.username}?startgroup=true"
            ),
            InlineKeyboardButton(text=_["S_B_2"], url=config.SUPPORT_CHAT),
        ],
        [
            InlineKeyboardButton(text="Telegram Shop🛍", url="https://t.me/HANTHAR_1999"),
        ],
    ]
    return buttons

def private_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_3"],
                url=f"https://t.me/{app.username}?startgroup=true",
            )
        ],
        [InlineKeyboardButton(text=_["S_B_4"], callback_data="settings_back_helper")],
        [
            InlineKeyboardButton(text=_["S_B_5"], user_id=config.OWNER_ID),
            InlineKeyboardButton(text=_["S_B_2"], url=config.SUPPORT_CHAT),
        ],
        [
            InlineKeyboardButton(text=_["S_B_6"], url=config.SUPPORT_CHANNEL),
            InlineKeyboardButton(text="Telegram Shop🛍", url="https://t.me/HANTHAR_1999"), 
        ],
        [
            InlineKeyboardButton(text="ဟာသကမ္ဘာ🥳", url="https://t.me/Happy_zone1999"),
            InlineKeyboardButton(text="စာတို/ကဗျာများ🤍", url="https://t.me/burmamyanmar_2"), 
        ],
    ]
    return buttons
