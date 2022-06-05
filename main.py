# this for python *.py это тесты для питона
# начинаем работу с файлами
# Читаю
import re

with open('xyz.txt', 'r') as file:
    filedata = file.read()

# Меняю
fd = re.sub(r'1{3,}', '@', filedata)

# Записываю
with open('xyz.txt', 'w') as file:
    file.write(fd)
