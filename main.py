# программа ищет в аудио файле(в данном случае текстовом) тишину
# и заменяет ее на другой звук
# Читаю
import re

with open('xyz.txt', 'r') as file:
    filedata = file.read()

# Меняю
# 1 - тишина
# @ - на что заменяется тишина
fd = re.sub(r'1{3,}', '@', filedata)

# Записываю
with open('xyz.txt', 'w') as file:
    file.write(fd)
