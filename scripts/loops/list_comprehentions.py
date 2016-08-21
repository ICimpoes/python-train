
lines = [line.rstrip().upper()
         for line in open('../../resources/test.file')
         for x in ['1', '2', 'a', 'b', 'g']
         if x in line]

print(lines)

M = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

for x in [[col * 2 for col in row] for row in M]:
    print(x)

print([M[i][i] for i in range(len(M))])

print([M[i][len(M) - i - 1] for i in range(len(M))])

print([M[i][k] * M[k][j] for i in range(3)
       for j in range(3)
       for k in range(3)])

print([sum(x) for x in [[M[i][k] * M[k][j] for k in range(3)]
       for i in range(3)
       for j in range(3)]])
