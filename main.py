# this for python *.py это тесты для питона
st = input()
first = st.find('h')
last = st.rfind('h')
st = st[:first] + st[(last + 1):]
print(st)
print('well done')
