L = [1, 0, 2, 0, 'spam', '', 'ham', []]

print('L =', L)

print('------------------------')
print('filter(bool, L)')
print(list(filter(bool, L)))
print()


print('------------------------')
print('[x for x in L if x]')
print([x for x in L if x])
print()

print('------------------------')
print('any(L), all(L)')
print(any(L), all(L))
