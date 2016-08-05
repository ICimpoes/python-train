x = 1
if x:
    y = 2
    if y:
        print('block2')
    print('block1')
print('block0')


x = 'SPAM'
if 'rubbery' in 'shrubbery':
    print(x * 8) # Prints 8 "SPAM"
    x += 'NI'
    if x.endswith('NI'):
        x *= 2
        print(x) # Prints "SPAMNISPAMNI"

