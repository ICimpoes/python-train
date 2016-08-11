
def f():
    return open('../../resources/test.file')

lines = [line.rstrip().upper()
         for line in f()
         for x in ['1', '2', 'a', 'b', 'g']
         if x in line]

print(lines)

a, *b, c = f()

print(a.rstrip(), b, c)

print('a\n' in f())
print('a2\n' in f())


X = (1, 2, 'a')
Y = (3, 4, 'b')
Z = (5, 6, 'c')

print(list(zip(X, Y, Z)))


A, B, C = zip(*zip(X, Y, Z))

print(A, B, C)


print(*[1, 2, 3, 4, 5], sep=' - ')


M = map(lambda x: 2 ** x, range(3))

for i in M:
    print(i)
for i in M:
    print(i)
