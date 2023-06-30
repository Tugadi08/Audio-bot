from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


bosh_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="💿 O‘zbek adabiyoti 💿"),
            KeyboardButton(text="💿 Jahon adabiyoti 💿")
        ],
        [
            KeyboardButton(text="🔘 Audio darsliklar 🔘")
        ],
        [
            KeyboardButton(text="🔘 Yangi audio kitoblar 🔘")
        ],
        [
            KeyboardButton(text="📨 Murojaat uchun 📨")
        ],
    ],
    resize_keyboard=True
)


uzb_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="O‘tkan kunlar"),
            KeyboardButton(text="Mehrobdan chayon")
        ],
        [
            KeyboardButton(text="Ufq"),
            KeyboardButton(text="Kecha va Kunduz")
        ],
        [
            KeyboardButton(text="Avlodlar dovoni"),
            KeyboardButton(text="Yulduzli tunlar")
        ],
        [
            KeyboardButton(text="Navoiy"),
            KeyboardButton(text="Ulug'bek xazinasi")
        ],
        [
            KeyboardButton(text="Oltin zanglamas"),
            KeyboardButton(text="Jannati odamlar")
        ],
        [
            KeyboardButton(text="Otamdan qolgan dalalar"),
            KeyboardButton(text="Bu dinyoda o'lib bo'lmaydi")
        ],
        [
            KeyboardButton(text="Yulduzlar mangu yonadi"),
            KeyboardButton(text="Ot kishnagan oqshom")
        ],
        [
            KeyboardButton(text="Ikki eshik orasi"),
            KeyboardButton(text="Dunyoning ishlari")
        ],
        [
            KeyboardButton(text="Daftar hoshiyasidagi bitiklar"),
            KeyboardButton(text="Bahor qaytmaydi")
        ],
        [
            KeyboardButton(text="Tushda kechgan umrlar"),
            KeyboardButton(text="Nur borki soya bor")
        ],
        [
            KeyboardButton(text="Shum bola"),
            KeyboardButton(text="Bolalik")
        ],
        [
            KeyboardButton(text="Go Back")
        ]
    ],
    resize_keyboard=True
)



jahon_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Choliqushi"),
            KeyboardButton(text="Qon da'vosi")
        ],
        [
            KeyboardButton(text="Martin Iden"),
            KeyboardButton(text="Hikoyalar (Jek London)")
        ],
    ],
    resize_keyboard=True
)