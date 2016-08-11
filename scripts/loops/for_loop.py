D = {'a': 1, 'b': 2, 'c': 3}

print('first')
for (k, v) in D.items():
    print(k, '=>', v)

print('second')
for ((a, b), c) in [((1, 2), 3), ((4, 5), 6)]:
    print(a, b, c)

print('third')
for ((a, b), c) in [([1, 2], 3), ['XY', 6]]:
    print(a, b, c)

print('forth')
for (a, *b, c) in [(1, 2, 3, 4), (5, 6, 7, 8)]:
    print(a, b, c)

print('-----------------------------')
print('search')

items = ['aaa', 111, (4, 5), 2.01]  # A set of objects
tests = [(4, 5), 3.14]  # Keys to search for

for key in tests:  # For all keys
    for item in items:  # For all items
        if item == key:  # Check for match
            print(key, 'was found')
            break
    else:
        print(key, 'not found!')

for key in tests:
    if key in items:
        print(key, 'was found')
    else:
        print(key, 'not found')

print('-----------------------------')
seq1 = 'pram'
seq2 = 'bram'

print([x for x in seq1 if x in seq2])

S = 'abcde'
for i in range(len(S)):
    print(S[i:] + S[:i], end=' ')

print()

S = 'abcdefghijk'
for i in range(0, len(S), 2):
    print(S[i], end=' ')

print()

for c in S[::2]:
    print(c, end=' ')

print()

L1 = [1, 2, 3]
L2 = [4, 5]

for x1, x2 in zip(L1, L2):
    print(x1, '+', x2, '=', x1 + x2)

print(dict(zip(L1, L2)))

print(dict(enumerate('abcddefghijklmnopqrstuvwxyz')))

