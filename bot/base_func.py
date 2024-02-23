from openai import AsyncOpenAI
from aiogram.fsm.state import State, StatesGroup
from bot.config import settings
from aiogram import Router
from aiogram.fsm.context import FSMContext

router = Router()

gpt_client = AsyncOpenAI(api_key= settings.API_KEY_G)

class Go(StatesGroup):
    go_promt = State()
    dialog = State()


premission = {'PREMISSION': 'Некоректный вопрос'}
response_gpt = {'data': 'ТВОЙ ОВТЕТ'}
config_promt = "сноуборд, доски для сноуборда"
link_from_promt = "https://www.sportmaster.ru/catalog/vidy_sporta_/snoubording/snoubordy/?utm_referrer=https%3A%2F%2Fwww.google.com%2F"

base_pre = f"ТЫ - ЧАТ БОТ ПОМОШНИК, ТЫ РАЗБИРАЕШЬСЯ В {config_promt}, ОТВЕЧАЙ ТОЛЬКО НА СООБЩЕНИЯ ПО ТЕМЕ {config_promt} И СВЯЗАННЫЕ С {config_promt}, НА ОСТАЛЬНЫЕ ВОПРОСЫ НЕ ПО ТЕМЕ ОТВЕЧАЙ {premission}.НА ВПОПРОСЫ ПО ТЕМЕ ОТВЕЧАЙ В ФОРМАТЕ {response_gpt}, ЕСЛИ СЛЕДУЮЩИЙ ПУНКТ НЕ ПУСТОЙ, ДОБАВЛЯЙ ССЛЫКУ ЕСЛИ ПОЛЬЗОВАТЕЛЬ ЗАХОЧЕТ УЗНАТЬ О ТОВАРЕ {link_from_promt}"


async def go_gpt(client: AsyncOpenAI, config: dict, promt: dict, is_sess: bool, dialog: bool, state: FSMContext):

    p_promt = {"role": "system", "content": base_pre}
    if is_sess is True:
        response = await client.chat.completions.create(
            model="gpt-3.5-turbo-0125", 
            messages=[p_promt, {"role": config["role"], "content": promt["data"]}], 
            temperature=0.9, 
            max_tokens=256)
    else:
        response = await client.chat.completions.create(
            model="gpt-3.5-turbo-0125", 
            messages=[{"role": config["role"], "content": promt["data"]}], 
            temperature=0.9, 
            max_tokens=256)
        
    return response.choices[0].message.content
