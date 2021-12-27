# Задача 3. Удаление части

user_string = input('Введите строку: ') #ПитоН - этО хорошО

upper = [i for i in user_string if i.isupper()]
lower = [i for i in user_string if i.islower()]

if len(upper) > len(lower):
    user_string = user_string.upper()
else:
    user_string = user_string.lower()

print('Результат:', user_string)
