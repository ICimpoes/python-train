import sys

temp = sys.stdout

sys.stdout = open('../../resources/app.log', 'a')

lines = [1, 2, 3, 4, 'line1', 'line2']

for line in lines:
    print(line)


sys.stdout = temp

for line in lines:
    print(line)


lines = [12, 22, 32, 42, 'line12', 'line22']
log = open('../../resources/app.log', 'a')

for line in lines:
    print(line, file=log)


for line in lines:
    print(line)

log.close()

log = open('../../resources/app.log')
print('---------------------------------------------------')
print('from app.log')
print('---------------------------------------------------')
print(log.read())
print('---------------------------------------------------')
