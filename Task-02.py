# Задача 2. Путь к файлу

path_file = input('Путь к файлу: ') # C:/user/docs/folder/new_file.txt

ask_disk = input('На каком диске должен лежать файл: ').upper()     # C
ask_file = input('Требуемое расширение файла: ').lower()            # .txt

if not path_file.startswith(ask_disk):
    print('Диск не корректен')
elif not path_file.endswith(ask_file):
    print('Файл не корректен')
else:
    print('Путь корректен!')
