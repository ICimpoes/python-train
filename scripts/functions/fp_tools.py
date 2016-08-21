# [1*4, 2*5, 4*6]
print(list(map(lambda x, y: x*y, [1, 2, 3], [4, 5, 6])))

print(list(map(lambda x, y, z: x*y*z, [1, 2, 3], [4, 5, 6], [3])))
print(list(map(lambda x, y, z: x*y*z, [1, 2, 3], [4, 5, 6], [3, 4, 5])))

from functools import reduce

print(reduce((lambda x, y: x*y), ['HI_ªª', 2, 3, 4]))
print(reduce((lambda x, y: x*y), [1]))

# print(reduce((lambda x, y: x*y), []))
