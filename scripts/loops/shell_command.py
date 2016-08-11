import os

c = os.popen('ls -lh /')

for x in c:
    print(x.rstrip())

L = [1, 2, 4, 8, 16, 32, 64]
X = 5

for x in L:
    if x == 2 ** X:
        print('found')
        break

else:
    print('not found')
