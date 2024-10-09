from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram import Router, types, F, Bot
from aiogram.filters import Command
import keyboard as kb

router = Router()
bot = Bot(token="7650674022:AAG7aNieJIBj2cLEn8hW3LXsE3mKiolzMlE")

@router.message(Command('info'))
async def send_info(message: types.Message):
    await message.answer('Выберите что-то', reply_markup=kb.keyboard2)

@router.message(F.text.lower() == '💵узнать условия оплаты💵')
async def test_message(message: types.Message):
    await message.answer('Для того чтобы поменялся статус заказа, необходимо внести 100% предоплату. '
                         'Оплата производиться переводом по номеру карты (сбербанк, альфа-банк). '
                         'После оплаты необходимо прислать чек об успешном переводе менеджеру и ожидать дальнейшего ответа.')

@router.message(F.text.lower() == '📏узнать свой размер одежды📏')
async def send_massage(message: types.Message):
    photo_url = 'https://i.pinimg.com/1200x/a5/b7/94/a5b794c8d177d3e3136507b1b55801b7.jpg'
    await bot.send_photo(chat_id=message.chat.id, photo=photo_url)

@router.message(F.text.lower() == '🛍️узнать наличие товара🛍️')
async def test_message(message: types.Message):
    await message.answer('Я помогу тебе узнать наличие товара, просто пришли мне ссылку на товар или отправь скриншот товара. '
                         'Через пару минут подойдет моя подружка и все тебе расскажет')

# @router.message(F.text.lower() == '💌позвать bestie💌')
# async def test_message(message: types.Message):
#     await message.answer('Твоя подружка уже бежит к тебе, чтобы ответить на все вопросы, ожидание займет пару минут')

@router.message(F.text.lower() == '🚂доставка🚂')
async def test_message(message: types.Message):
    await message.answer('Доставка входит в стоимость товара.'
                         ' Доставка по России от 3 до 7 дней, с момента обработки заказа менеджером.'
                         ' Если вам не прислали информацию по после оплаты, пожалуйста, выберите команду "позвать bestie", и сообщите менеджеру об этом.')