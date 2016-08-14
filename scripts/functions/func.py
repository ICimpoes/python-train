def intersect(seq1, seq2):
    return [x for x in seq1 if x in seq2]

print(intersect('abc', 'act'))

print(intersect([1, 2, 3], [3, 1, 5]))

#second file should be reset using seek(0).
print(intersect(open('../../resources/test.file'), open('../../resources/app.log')))


print(intersect(('1\n', '2\n', '52'), open('../../resources/app.log')))

x = 11

def f(y):
    global x
    x = y + 5

print(f(15), x)

b, c = 1, 2

def globals():
    global a  #creates if does not exist
    a = b + c

print(globals(), a)

print(a + x)