def add(x : int, y : int) -> int:
    return x + y


def sub(x : int, y : int) -> int:
    return x - y


def mult(x : int, y : int) -> int:
    return x * y


def div(x : int, y : int) -> int:
    return x // y


def mod(x : int, y : int) -> int:
    return x % y


def pow(x : int, y : int) -> int:
    pass


if __name__ == '__main__':
    print(add(4, 5))
    print(sub(3, 1))
    print(mult(2, 2))
    print(div(4, 2))
    print(mod(5, 3))
    print(pow(6, 2))