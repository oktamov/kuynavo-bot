from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

lang = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="UZ🇺🇿", callback_data="uz"),
            InlineKeyboardButton(text="RU🇷🇺", callback_data="ru"),
            InlineKeyboardButton(text="EN🇬🇧", callback_data="eng"),
        ]
    ]
)