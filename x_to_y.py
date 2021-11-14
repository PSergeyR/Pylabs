orig_str = 'jdfhxjhjhdfxjxjhfdxlsdkkx xxx yyy'
new_str = ''
for x in orig_str:
    if x == 'x':
        new_str += 'y'
    else:
        new_str += x
print(orig_str)
print(new_str)
