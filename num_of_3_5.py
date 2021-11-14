nums = [1, 2, 3, 5, 7, 9, 10, 15, 16, 19, 20, 24, 25, 30]
y = 1
for x in nums:
    if x // 5 & x//3:
        y *= x
print(y)
