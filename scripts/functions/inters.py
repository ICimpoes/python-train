def intersect(first, *args):
    res = []
    for x in first:
        if x in res: continue
        for y in args:
            if x not in y: break
        else: res.append(x)
    return res


def union(*args):
    return list({y for x in args for y in x})

print(intersect(('a', 'b'), ['b', 1], 'bAm'))
print(union(('a', 'b'), ['b', 1], 'bAm'))
