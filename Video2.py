me1 = ['Иванов Иван Иванович', 1987, 34, 185, 'Пермь', 'Попова', 43, 56, +79123453676]
me2 = {'ФИО': 'Иванов Иван Иванович', 'Год рождения': 1987, 'Возраст': 34, 'Город': 'Пермь', 'Улица': 'Попова',
       'Дом': 43, 'Квартира': 56, 'Телефон': +79123453676}
for x in me1:
    print(x)
for x in me2:
    print(x, me2[x])
#Список занимает меньше памяти, но для понятия информации нужно обладать сведениями, какой ячейке что соответствует
#Словарь занимает больше памяти но в связке ключ: значение легче ориентироваться