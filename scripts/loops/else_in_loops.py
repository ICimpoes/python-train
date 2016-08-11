x = [1, 2, 3, 4, 5, 6]

# Using external flag
x1 = x.copy()
found = False
while x1 and not found:
    if x1[0] == 4:  # Value at front?
        print('Ni')
        found = True
    else:
        x1 = x1[1:]  # Slice off front and repeat
if not found:
    print('not found')

# Using loop else
x2 = x.copy()
while x2:
    if x2[0] == 7:  # Value at front?
        print('Ni')
        break
    x2 = x2[1:]
else:
    print('not found')
