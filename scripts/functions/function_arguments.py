def f(*args):
    print(type(args), args)


f()
f(1)
f(1, 2)


def f(**args):
    print(type(args), args)

f()
f(a=1)
f(a=1, b=2)
f(a=1, b=2, c='3')


# *args -> tuple, **kwargs -> dict
def f(a, *args, **kwargs):
    print(a, args, kwargs)

f(1)
f(1, 2)
f(1, 2, 3, 4, 5)
f(1, 2, 3, 4, 5, b=1, c=2, key=3)

f((1, 2, 3, 4, 5), b=1, c=2, key=3)

f(*(1, 2, 3, 4, 5), **{'b': 1, 'c': 2, 'key': 3})

print(list(zip(*zip((1, 2), (3, 4)))))


# key word only arguments
def konly(a, *b, c):
    print(a, b, c)

# konly(1, 2, 3, 4)
konly(1, c=2)


def konly(a, *, b, c):
    print(a, b, c)

konly(1, b=2, c='asdasd')

# konly(a, **, c) - invalid

# ordering rules
def f(a, *b, c, **d):
    print(a, b, c, d)

f(1, 2, 3, aa=1, b=3, c='c')