import requests
from aiogram import F,Router
from aiogram.types import Message
from aiogram.filters import CommandStart, Command
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv('api_key')


def get_weather(city, key):
    try:
        req = requests.get(
            f"http://api.weatherapi.com/v1/current.json?key={key}&q={city}&lang=ru"
        )
        data = req.json()
        city = data['location']['name']
        temp = data['current']['temp_c']
        description = data['current']['condition']['text']
        humidity = data['current']['humidity']
        return f'<b>Город</b>: {city}\n<b>Температура</b>: {temp}\n<b>Влажность</b>: {humidity}\n<b>Погода</b>: {description}'
    except:
        return f'Попробуйте ввести название города заново'


router = Router()

@router.message(CommandStart())
async def start_command(message: Message):
    await message.answer('Привет!\nЭтот бот поможет тебе узнать погоду в интересующем тебя городе, просто назови город')

@router.message()
async def get_city(message: Message):
    answer_text = get_weather(message.text, api_key)
    await message.answer(answer_text, parse_mode='HTML')
    pass