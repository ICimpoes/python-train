s, h = 'SSSS', 'HHHH'
print('s: {}; h: {}'.format(s, h))

[s, h] = ['SSSS', 'HHHH']
print('s: {}; h: {}'.format(s, h))

[s, *h] = ['SSSS', 'HHHH', 'HHH2']
print('s: {}; h: {}'.format(s, h))

a, b, c, d = 'abcd'
print('a: {}; b: {}; c: {}; d: {}'.format(a, b, c, d))

a, b, c, d = 'abcd'
print('a: {}; b: {};` c: {}; d: {}'.format(a, b, c, d))

a, *b = 'abcdefg'
print('a: {}; b: {}'.format(a, b))

a, *b = 'a'
print('a: {}; b: {}'.format(a, b))

for ((a, b), c) in [((1, 2), 3), ((4, 5), 6)]:
    print('a: {}; b: {}; c: {}'.format(a, b, c))


L = [1, 2, 3, 4]
while L:
    front, L = L[0], L[1:]
    print(front, L)

a, *b, c = range(4)
print('a: {}; b: {}; c: {}'.format(a, b, c))

a, *b, c = range(2)
print('a: {}; b: {}; c: {}'.format(a, b, c))


def f():
    return open('../../resources/test.file')

a, *b, c = open('../../resources/test.file')

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