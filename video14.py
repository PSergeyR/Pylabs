# 2+2=5
class MyInt(int):
    def __add__(self, x): #Перекрытие метода __add__
        return super().__add__(x+1)


y = MyInt(2)
print(y + 2)

# len(list)>10
class MyList(list):
    def __init__(self, x):
        if len(x) > 10:
            raise ValueError('> 10')
        else:
            super().__init__(x)

    def append(self, x):
        if len(self) == 10:
            raise ValueError()
        else:super().append(x)


# list[i]!= list[j]
class MyList(set):
    pass

