import numpy as np

# 1
x = np.array(range(100))
summ = 0
for i in x:
    summ += x[i]
print(summ)
# 2
inp = int(input('Введите число, до которого посчитать сумму:'))
inpArr = np.array(range(0, inp))
summ1 = np.sum(inpArr)
print(summ1)
# 3
rnd = np.random.sample(100)
print('Среднее арифметическое среди 100 случайных:', np.mean(rnd))



