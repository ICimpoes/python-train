#CONTINUE
x = 10
while x:
    x -= 1
    if x % 2 != 0: continue # Odd? -- skip print
    print(x, end=' ')

#BREAK
while True:
    name = input('\nEnter name: ')
    if name == 'stop': break
    age = input('Enter age: ')
    print('Hello', name, '=>', int(age) ** 2)

y = int(input('\nEnter number: '))
x = y // 2 # For some y > 1
while x > 1:
    if y % x == 0: # Remainder
        print(y, 'has factor', x)
        break # Skip else
    x -= 1
else:
    print(y, 'is prime')
