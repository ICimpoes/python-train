def make(x):

    def f(y):
        return x ** y
    return f


def make2(x):
    return lambda y: 2 * x ** y


print(make(2)(3))

F = make(3)

print(type(F))

print({'3^' + str(x): F(x) for x in [1, 2, 3, 4, 5, 6, 7, 8] if x % 2 == 0})

print(make2(2)(3))

F = make2(3)

print(type(F))

print({'2 * 3^' + str(x): F(x) for x in [1, 2, 3, 4, 5, 6, 7, 8] if x % 2 == 0})


def make_all():
    return [lambda x: i ** x for i in range(5)]  # `i` is evaluated when lambda is called.

print(make_all()[0](2))  # same result (remembers the last `i`)
print(make_all()[1](2))  # same result
print(make_all()[2](2))  # same result
print(make_all()[3](2))  # same result


def make_all2():
    return [lambda x, i = i: i ** x for i in range(5)]  # `i` is evaluated when lambda is created

print(make_all2()[0](2))  # 0
print(make_all2()[1](2))  # 1
print(make_all2()[2](2))  # 4
print(make_all2()[3](2))  # 9
print(make_all2()[4](2))  # 16

