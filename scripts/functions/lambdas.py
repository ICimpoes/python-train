
m = {1: (lambda: print('hi' * 1)),
 2: (lambda: print('bye' * 2)),
 3: (lambda: print('HI bye' * 3)),
 4: (lambda: print('bye Hi' * 4))}

for f in m.values():
    f()

# nested scopes (LEGB works as well)

print((lambda x: (lambda y: x + y))(1)(4))
