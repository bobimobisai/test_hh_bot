from aiogram.types import Message, CallbackQuery
from aiogram import F
from aiogram.fsm.context import FSMContext
from base_func import go_gpt, router, Go
from keyboards.base_kb import go_back 
from bot.config import settings
from openai import AsyncOpenAI



gpt_client = AsyncOpenAI(api_key= settings.API_KEY_G)


@router.callback_query(F.data == "go_gpt_chat")
async def command_go(callback: CallbackQuery, state: FSMContext) ->  None:
    await callback.message.answer(text="Chat GPT 3 приветствует вас!👽\nВведите ваш запрос:")
    await state.set_state(Go.go_promt)


@router.message(Go.go_promt)
async def get_text_promt(message: Message, state: FSMContext) ->  None:
    response = await go_gpt(client=gpt_client, config={"role": "user"}, promt={"data": message.text}, is_sess=True, dialog=True, state=state)
    await message.answer(text=response, reply_markup=go_back(size=1))


@router.callback_query(F.data == "stop")
async def command_back(callback: CallbackQuery, state: FSMContext) ->  None:
    await callback.message.answer(text="Диалог закончен")
    await state.clear()  