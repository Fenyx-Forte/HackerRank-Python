import numpy


def arrays(arr: list[str]):
    return numpy.array(arr[::-1], float)


arr = input().split()
result = arrays(arr)
print(result)
