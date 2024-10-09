from aiogram import Router, types, F
import keyboard as kb
from aiogram.filters import Command
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import BotCommand

router = Router()


@router.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer('Привет! На связи твоя лучшая подружка и я очень рада тебя видеть. 💌'
                         'Я как фея крестная помогу тебе во всем и отправлю в свет самой красивой! Я помогу тебе с размером, узнаю наличие товара и '
                         'смогу ответить на любой твой вопрос. Для еще большего удобства ниже есть панель, которая поможет тебе быстрее найти ответы.'
                         ' Обязательно не забудь представиться, чтобы нам было комфортнее общаться!✨')
    await message.answer("Теперь давай разберемся, что тебя интересует 🔍", reply_markup=kb.keyboard1)

@router.callback_query(F.data == "keyboard1")
async def send_random_value(callback: types.CallbackQuery):
    await callback.message.answer('Выберите что хотите узнать:', reply_markup=kb.keyboard2)



    