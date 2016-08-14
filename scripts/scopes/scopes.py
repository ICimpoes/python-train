def mem_state(start):
    state = start

    def nested(label):
        nonlocal state
        print(label, state)
        state += 1
    return nested


F = mem_state(0)

F('F - xxx')

F('F - xxx2')


H = mem_state(44)


H('H - xxx')

F('F - xxx3')

H('H - xxx1')

H('H - xxx2')

F('F - xxx1')

H('H - xxx3')


a = 9


def f1():
    a = 8  # Enclosing scope

    def f2():
        print('enclosing', a)

    def f3():
        global a
        print('global', a)

    f2()
    f3()

f1()


def f11():
    x = 1

    def f2():
        print(x)  # remember x
    return f2


action = f11()

action()
