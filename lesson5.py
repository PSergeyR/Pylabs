persons = [['Иванов', 'Иван', 1991, 'холост'], ['Петров', 'Петр', 1992, 'разведен'],
           ['Сидоров', 'Василий', 1996, 'женат'], ['Попов', 'Клим', 1994, 'холост']]
persons1 = {'Иванов' :{ 'fname': 'Иван', 'bday': '01.01.1991'}, 'Петров': { 'fname': 'Петр', 'bday': '02.02.1992'},
             'Сидоров':{ 'fname': 'Василий', 'bday': '03.03.1993'},'Попов':{'fname': 'Клим', 'bday': '04.04.1994'}}
def old():
    oldest = persons[0][2]
    for x in range(1, len(persons)):
        if persons[x][2] < oldest:
            oldest = persons[x][2]
            name = persons[x][0]

    print('Самый старший:', name, 'год рождения:', oldest)

def old_dic():
    oldestDic = persons1['Иванов']['bday']
    for key in persons1:
        if persons1[key]['bday'] < oldestDic:
            oldestDic = persons1[key]['bday']
    print('Самый старший в словаре:', key, 'год рождения:', oldestDic)

old()
old_dic()

def compare (s1,s2):
    ngrams = [s1[i:i+3] for i in range(len(s1))]
    count = 0
    for ngram in ngrams:
        count += s2.count(ngram)
    return count/max(len(s1), len(s2))

def main():
    s1 = input("Введите первую строку:")
    s2 = input("Введите вторую строку:")
    print(compare(s1, s2))


if __name__ == '__main__':
    main()







