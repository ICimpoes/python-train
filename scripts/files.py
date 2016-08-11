f = open('../resources/data.txt', 'w+')

lines = ['Hello', 'world']

for l in lines:
    f.write(l + '\n')

f.seek(0)


for l in f:
    print(l, end='')
