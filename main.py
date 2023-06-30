import logging

from aiogram import Bot, Dispatcher, executor, types
from button import *

API_TOKEN = '6216979043:AAE94uiANnJvzvuKwzCZIPCTxQIh9tGAkAc'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("""Assalomu alaykum! 

Botdan foydalanish uchun ushbu kanalga a'zo bo‘ling:
👉 t.me/audiokitoblar_uz

Используйте /off чтобы приостановить подписку.""")
    await message.reply("""Хотите создать своего бота?
Вам сюда: @Manybot""", reply_markup=bosh_menu)




@dp.message_handler(text = "💿 O‘zbek adabiyoti 💿")
async def echo(message: types.Message):
    await message.answer("🔘 Tanlang", reply_markup=uzb_menu)


@dp.message_handler(text = "O‘tkan kunlar")
async def echo(message: types.Message):
    await message.answer("""Bu yerdan yuklab oling:

https://t.me/audiokitoblar_uz/933""", reply_markup=uzb_menu)



@dp.message_handler(text = "Mehrobdan chayon")
async def echo(message: types.Message):
    await message.answer("""Bu yerdan yuklab oling:

https://t.me/audiokitoblar_uz/700""")



@dp.message_handler(text = "Ufq")
async def echo(message: types.Message):
    await message.answer("""Bu yerdan yuklab oling:

https://t.me/audiokitoblar_uz/406""")



@dp.message_handler(text = "Kecha va kunduz")
async def echo(message: types.Message):
    await message.answer("""Bu yerdan yuklab oling:

https://t.me/audiokitoblar_uz/275""")



@dp.message_handler(text = "Avlodlar dovoni")
async def echo(message: types.Message):
    await message.answer("""Bu yerdan yuklab oling:

https://t.me/audiokitoblar_uz/1014""")



@dp.message_handler(text = "Yulduzli tunlar")
async def echo(message: types.Message):
    await message.answer("""Bu yerdan yuklab oling:

https://t.me/audiokitoblar_uz/890""")



@dp.message_handler(text = "Navoiy")
async def echo(message: types.Message):
    await message.answer("""Bu yerdan yuklab oling:

https://t.me/audiokitoblar_uz/1346""")



@dp.message_handler(text = "Ulug‘bek xazinasi")
async def echo(message: types.Message):
    await message.answer("""Bu yerdan yuklab oling:

https://t.me/audiokitoblar_uz/971""")



@dp.message_handler(text = "Oltin zanglamas")
async def echo(message: types.Message):
    await message.answer("""Bu yerdan yuklab oling:

https://t.me/audiokitoblar_uz/2193""")



@dp.message_handler(text = "Jannati odamlar")
async def echo(message: types.Message):
    await message.answer("""Bu yerdan yuklab oling:

https://t.me/audiokitoblar_uz/1422""")



@dp.message_handler(text = "Bu dunyoda o‘lib bo‘lmaydi")
async def echo(message: types.Message):
    await message.answer("""Bu yerdan yuklab oling:

https://t.me/audiokitoblar_uz/264""")



@dp.message_handler(text = "Yulduzlar mangu yonadi")
async def echo(message: types.Message):
    await message.answer("""Bu yerdan yuklab oling:

https://t.me/audiokitoblar_uz/1095""")
    


@dp.message_handler(text = "Ot kishnagan oqshom")
async def echo(message: types.Message):
    await message.answer("""Bu yerdan yuklab oling:

https://t.me/audiokitoblar_uz/622""")
    


@dp.message_handler(text = "Ikki eshik orasi")
async def echo(message: types.Message):
    await message.answer("""Bu yerdan yuklab oling:

https://t.me/audiokitoblar_uz/1680""")



@dp.message_handler(text = "Dunyoning ishlari")
async def echo(message: types.Message):
    await message.answer("""Bu yerdan yuklab oling:

https://t.me/audiokitoblar_uz/306""")
    


@dp.message_handler(text = "Daftar hoshiyasidagi bitiklar")
async def echo(message: types.Message):
    await message.answer("""Bu yerdan yuklab oling:

https://t.me/audiokitoblar_uz/1903""")



@dp.message_handler(text = "Bahor qaytmaydi")
async def echo(message: types.Message):
    await message.answer("""Bu yerdan yuklab oling:

https://t.me/audiokitoblar_uz/14""")



@dp.message_handler(text = "Tushda kechgan umrlar")
async def echo(message: types.Message):
    await message.answer("""Bu yerdan yuklab oling:

https://t.me/audiokitoblar_uz/183""")



@dp.message_handler(text = "Nur borki soya bor")
async def echo(message: types.Message):
    await message.answer("""Bu yerdan yuklab oling:

https://t.me/audiokitoblar_uz/1618""")



@dp.message_handler(text = "Shum bola")
async def echo(message: types.Message):
    await message.answer("""Bu yerdan yuklab oling:

https://t.me/audiokitoblar_uz/2359""")



@dp.message_handler(text = "Bolalik")
async def echo(message: types.Message):
    await message.answer("""Bu yerdan yuklab oling:

https://t.me/audiokitoblar_uz/1432""")



@dp.message_handler(text = "Go Back")
async def echo(message: types.Message):
    await message.answer("Главное меню", reply_markup=bosh_menu)



@dp.message_handler(text = "💿 Jahon adabiyoti 💿")
async def echo(message: types.Message):
    await message.answer("🔘 Tanlang", reply_markup=jahon_menu)



@dp.message_handler(text = "Choliqushi")
async def echo(message: types.Message):
    await message.answer("""Bu yerdan yuklab oling:

https://t.me/audiokitoblar_uz/1873""")



@dp.message_handler(text = "Qon da'vosi")
async def echo(message: types.Message):
    await message.answer("""Bu yerdan yuklab oling:

https://t.me/audiokitoblar_uz/1664""")



@dp.message_handler(text = "Martin Iden")
async def echo(message: types.Message):
    await message.answer("""Bu yerdan yuklab oling:

https://t.me/audiokitoblar_uz/2156""")



@dp.message_handler(text = "Hikoyalar (Jek London)")
async def echo(message: types.Message):
    await message.answer("""Bu yerdan yuklab oling:

https://t.me/audiokitoblar_uz/587""")



@dp.message_handler(text = "🔘 Audio darsliklar 🔘")
async def echo(message: types.Message):
    await message.answer("Audio darsliklar bu yerda: @audio_darsliklar")



@dp.message_handler(text = "🔘 Yangi audio kitoblar 🔘")
async def echo(message: types.Message):
    await message.answer("""Yangi audio kitoblarni o‘tkazib yubormaslik uchun kanalimizga obuna bo‘lishni unutmang: 

t.me/audiokitoblar_uz""")



@dp.message_handler(text = "📨 Murojaat uchun 📨")
async def echo(message: types.Message):
    await message.answer("""Murojaat uchun: 

@audiokitoblar_uzbot""")






@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
