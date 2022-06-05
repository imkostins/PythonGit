# this for python *.py это тесты для питона
# начинаем работу с файлами
# Читаю
with open('xyz.txt', 'r') as file:
    filedata = file.read()

# Меняю
filedata = filedata.replace('2', '@')

# Записываю
with open('xyz.txt', 'w') as file:
    file.write(filedata)
