# Imports the project
# ----------------------------------------------------------------
import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from decouple import config
from aiogram.filters import CommandStart
from handlers import comands

# ----------------------------------------------------------------
# Config project
# ----------------------------------------------------------------
Token = config('TOKEN')
bot = Bot(Token)
dp = Dispatcher()

# ----------------------------------------------------------------

# Register Message handlers
dp.message.register(comands.command_start_handler, CommandStart())
dp.message.register(comands.help_handler, Command("help"))


# ----------------------------------------------------------------
async def main():
    await dp.start_polling(bot)


# ----------------------------------------------------------------

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())

# ----------------------------------------------------------------
