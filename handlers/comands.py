from aiogram import types
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.utils.markdown import hbold


async def command_start_handler(message: Message) -> None:
    kb = [
        [types.KeyboardButton(text="/start")],

    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb,
                                         resize_keyboard=True,
                                         )
    await message.answer(f"Hello, {message.from_user.full_name}!", reply_markup=keyboard)


async def help_handler(message: Message):
    await message.answer(
        f"Hello, {message.from_user.full_name}!\n\n"
        f"/start - start bot\n"
        f"/stop - stop bot\n"
        f"/reply_builder - reply builder\n"
    )


async def stop(message: types.Message):
    await message.answer(f'Goodbye {message.from_user.full_name}')
    from main import bot
    await bot.close()
