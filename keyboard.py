from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

keyboard1 = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='показать меню', callback_data='keyboard1')]
])

button1 = KeyboardButton(text='📏узнать свой размер одежды📏')
button2 = KeyboardButton(text='🛍️узнать наличие товара🛍️')
button3 = KeyboardButton(text='💌позвать bestie💌')
button4 = KeyboardButton(text='💵узнать условия оплаты💵')
button5 = KeyboardButton(text='🚂доставка🚂')


keyboard2 = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=False,
    row_width=2,
    keyboard=[
        [button1, button2],
        [button5, button4],
        [button3]
    ]
)

