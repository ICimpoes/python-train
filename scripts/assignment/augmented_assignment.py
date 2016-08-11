L = [1, 2]
M = L

L = L + [3, 4]  # L + [ .. ] creates new list instead of inplace change
print(L, M)


L = [1, 2]
M = L

L += [3, 4]  # L += [ .. ] calls `extend` method which changes list inplace
print(L, M)
