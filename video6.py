class Person:
    def __init__(self, name, age, height, city, bornDate ):
        self.name = name
        self.age = age
        self.height = height
        self.city = city
        self.bornDate = bornDate

    def __repr__(self):
        return "Person('%s', %s, %s, '%s, %s)" % (self.name, self.age, self.height, self.city, self.bornDate)

petr = Person('Петр Петрович', 33, 180, 'Пермь', 1988)
ivan = Person('Иван Иванович', 32, 160, 'Москва', 1989)
dima = Person('Дмитрий Дмитриевич', 30, 175, 'Воронеж', 1991)
sasha = Person('Александр Александрович', 34, 155, 'Тамбов', 1987)

peoples = {
    petr.name: petr, ivan.name: ivan, dima.name: dima, sasha.name: sasha
}

def compare (s1,s2):
    ngrams = [s1[i:i+3] for i in range(len(s1))]
    count = 0
    for ngram in ngrams:
        count += s2.count(ngram)
    return count/max(len(s1), len(s2))

def nameFinder(name):
    for i in peoples.values():
        if compare(str(name), str(i.name)) > 0.8:
            return i
    return 'Нет совпадений'

def heightFinder(heigh):
    for i in peoples.values():
        if 0.97 * heigh  <= i.height <= 1.03 * heigh:
            return (i.height, i.name)
        return 'Нет совпадений'


print(nameFinder('Петр Петрович'))
print(nameFinder('Сидор'))
print(heightFinder(179))