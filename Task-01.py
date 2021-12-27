# Задача 1. Шифр Цезаря 2

user_text = input('Введите текст: ').lower()
k = int(input('Введите смещение: '))
dict_user = 'абвгдеёжзиклмнопрстуфхцчшщъыбьэюя'
new_text = ''
for i in user_text:
    new_text += dict_user[dict_user.index(i) + k]

print('Кодированный текст:', new_text)
