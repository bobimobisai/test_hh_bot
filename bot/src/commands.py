from aiogram.types import Message, FSInputFile
from aiogram.filters import CommandStart, Command, StateFilter
from keyboards.base_kb import menu
from bot.src.handler import router


base_photo = FSInputFile("bot/images/base_img.png")
text_start = "Добро пожаловать!💻\nБот может:\n - создавать диалоги с GPT\n - создавать кастомные диалог с ChatGPT"
text_help = "/start - начало работы с ботом✅\n/menu - маню для выбора действий\n/help - базовые функции и помощь\nБыстрый доступ к командам нахоядтся в Меню↙\n\nПоддержка✉️ - https://t.me/ivan_official_py"


@router.message(Command("start"))
async def command_start(message: Message):
    await message.answer_photo(photo=base_photo, caption=text_start)


@router.message(Command("menu"))
async def command_menu(message: Message):
    await message.answer_photo(photo=base_photo, caption="Меню", reply_markup=menu())


@router.message(Command("help"))
async def command_help(message: Message):
    await message.answer_photo(photo=base_photo, caption=text_help)
