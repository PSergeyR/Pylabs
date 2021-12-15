#1
persons = [['Иванов', 'Иван', '01.01.1991', 'холост'], ['Петров', 'Петр', '02.02.1992', 'разведен'],
           ['Сидоров', 'Василий', '03.03.1993', 'женат'], ['Попов', 'Клим', '04.04.1994', 'холост']]

old = sorted(persons, key=lambda x: int(x[-2].split('.')[-1]))
print(old[0])
#2
persons1 = [{'sname': 'Иванов', 'fname': 'Иван', 'bday': '01.01.1991'}, {'sname': 'Петров', 'fname': 'Петр', 'bday': '02.02.1992'},
            {'sname': 'Сидоров', 'fname': 'Василий', 'bday': '03.03.1993'}, {'sname': 'Попов', 'fname': 'Клим', 'bday': '04.04.1994'}]

old1 = sorted(persons1, key=lambda x: int(x['bday'].split('.')[-1]))[0]
print(old1)

#3

x = input('Введите строку')

for i in persons1:
    y = list(i.values())
    for a in y:
        if a.find(x) != -1:
            print(i)
