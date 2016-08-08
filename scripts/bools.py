def f1():
    print('called "f1"')
    return ''

def f2():
    print('called "f2"') #None is returned which is `false` 

def f3():
    print('called "f3"')
    return 'non empty'

def f4():
    print('called "f4"')

#f4 is not called because f3 retrns non empty string which is `true`. Same works with number, lists, dicts objects ....
res = f1() or f2() or f3() or f4()

print(res)
