from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from aiogram import F, Router
from aiogram import  html
from weather import get_weather

router = Router()

@router.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(f"Здравствуйте, {html.bold(message.from_user.full_name)}!")


@router.message(Command('help'))
async def command_help_handler(message: Message):
    await message.answer("Вы нажали на кнопку помощи!")

@router.message(F.text == 'изо')
async def command_image_handler(message: Message):
    await message.answer("Пока в доработке")

@router.message(F.text == 'погода')
async def command_weather_handler(message: Message, country="Трубчевск"):
    result = get_weather(country)
    await message.answer(result)