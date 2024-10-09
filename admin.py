from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram import Router, types, F, Bot, types
from aiogram.filters import Command
import keyboard as kb
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

bot = Bot(token="7650674022:AAG7aNieJIBj2cLEn8hW3LXsE3mKiolzMlE")
router = Router()

ADMIN_IDS = [937832881, 852420511]

active_chats = {}


def generate_user_buttons():
    keyboard = InlineKeyboardMarkup(inline_keyboard=[])
    for user_id, status in active_chats.items():
        if status == 'waiting_for_admin':
            user_name = active_chats.get(f"{user_id}_name", "Пользователь")

            button = InlineKeyboardButton(text=user_name, callback_data=f"start_chat:{user_id}")
            keyboard.inline_keyboard.append([button])
    return keyboard




async def notify_admins():
    for admin_id in ADMIN_IDS:
        keyboard = generate_user_buttons()
        if keyboard.inline_keyboard:
            await bot.send_message(chat_id=admin_id, text="Новые заявки на чат:", reply_markup=keyboard)
        else:
            await bot.send_message(chat_id=admin_id, text="Нет активных заявок.")


@router.message(F.text.lower() == '💌позвать bestie💌')
async def call_admin(message: types.Message):
    user = message.from_user
    user_info = f'Пользователь {user.full_name} с username @{user.username} и ID {user.id} позвал администратора'

    for admin in ADMIN_IDS:
        try:
            await bot.send_message(chat_id=admin, text=user_info)
        except Exception as e:
            print(f'Ошибка отправки админу {admin}: {e}')




    await message.answer("Твоя подружка уже бежит к тебе, чтобы ответить на все вопросы, ожидание займет пару минут")



