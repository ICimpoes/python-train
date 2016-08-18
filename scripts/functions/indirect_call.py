def indirect(func, arg):
    func(arg)


def f(x):
    print(x)


indirect(f, 'Hi')

indirect(lambda x: print(x), 'Hello')

# unpack function to `func` and all the arguments to args
for func, *args in [(f, 'Hello!!'), (lambda x, y: print(x, y), 'Hi', 'there'),
                    (lambda x, y, z: print(x, y, z), 'Hi', 'there', '!!')]:
    func(*args)  # unpack all the args to function arguments

