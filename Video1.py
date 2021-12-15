#задание 1
orig_str = 'jdfhxjhjhdfxjxjhfdxlsdkkx xxx yyy'
new_str = ''
for x in orig_str:
    if x == 'x':
        new_str += 'y'
    else:
        new_str += x
print(orig_str)
print(new_str)
#задание 2
nums = [1, 2, 3, 5, 7, 9, 10, 15, 16, 19, 20, 24, 25, 30]
y = 1
for x in nums:
    if x // 5 or x // 3:
        y *= x
print(y)
#задание 3
orig_str = 'jdfhxjhjhdfxjxjhfdxlsdkkx xxx yyy'
a = orig_str.replace('x', 'y')
print(a)
