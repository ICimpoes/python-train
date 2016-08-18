def f(a: 'first param', b: int, c: float) -> str:
    print(a + b + c)

f(3, 2, 3)
print(f.__annotations__)


def f(a: 'first param', b: int, c: float = 1) -> str:
    print(a + b + c)

f(3, 2)
print(f.__annotations__)