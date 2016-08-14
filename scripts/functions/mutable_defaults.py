def f(a=[]):
    try:
        x = a[-1]
    except:
        x = 0
    a.append(x + 1)
    return a

print(f())
print(f())
print(f())
print(f())
print(f())