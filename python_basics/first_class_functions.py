from audioop import add


def adds(*values):
    return sum(values)


def spec(func):
    return func(1,2)


print(spec(adds))  