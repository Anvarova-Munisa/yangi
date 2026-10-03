from aiogram.utils.keyboard import ReplyKeyboardBuilder

b_type = ReplyKeyboardBuilder()
types_list = ["oddiy", "elektro", "inamarka"]
for t in types_list:
    b_type.button(text=t)
b_type.adjust(3)

b_oddiy = ReplyKeyboardBuilder()
cars = ["tiko", "matiz", "jiguli", "nexia", "cobalt", "jentra", "damas"]
for car in cars:
    b_oddiy.button(text=car)
b_oddiy.adjust(3)

b_inamarka = ReplyKeyboardBuilder()
cars = ["malibu", "tracker", "onix", "bmw", "bugatti"]
for car in cars:
    b_inamarka.button(text=car)
b_inamarka.adjust(3)

b_elektro = ReplyKeyboardBuilder()
cars = ["byd", "tesla", "kia", "tesla2", "tesla3"]
for car in cars:
    b_elektro.button(text=car)
b_elektro.adjust(3)



b_rang = ReplyKeyboardBuilder()
ranglar = ["oq", "qora", "qizil", "kok", "yashil"]
for rang in ranglar:
    b_rang.button(text=rang)
b_rang.adjust(3)

narxlar = {
    "tiko": "5 000$", "matiz": "6 000$", "jiguli": "4 000$", "nexia": "10 000$",
    "cobalt": "12 000$", "jentra": "14 000$", "damas": "9 000$",
    "malibu": "28 000$", "tracker": "21 000$", "onix": "17 000$",
    "bmw": "45 000$", "bugatti": "3 000 000$",
    "byd": "30 000$", "tesla": "40 000$", "kia": "35 000$",
    "tesla2": "50 000$", "tesla3": "60 000$",
}