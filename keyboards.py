import emoji
from aiogram.types import (ReplyKeyboardMarkup,
                           KeyboardButton,
                           InlineKeyboardMarkup,
                           InlineKeyboardButton
                           )


inline_kb = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="О нас"+emoji.emojize(':speech_balloon:'), callback_data='aboutUs'),
        InlineKeyboardButton(text="Связаться с разработчиком"+emoji.emojize(':alien_monster:'),
                             url='https://t.me/shemisu'),
        InlineKeyboardButton(text="Поддержать нас"+emoji.emojize("💸"), callback_data='donate')
    ],
    [
        InlineKeyboardButton(text="Начать поиск..."+emoji.emojize('🔎'), callback_data='search')
    ]
])

search_kb = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Википедия"+emoji.emojize('📃'), callback_data='wiki'),
        InlineKeyboardButton(text="История.РФ"+emoji.emojize('📚'), callback_data='hist')
    ],
    [
        InlineKeyboardButton(text="Назад"+emoji.emojize('⬅'), callback_data='back')
    ]
])

back_kb = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Назад"+emoji.emojize('⬅'), callback_data="back")
    ]
])