def f(n):
    result = 0
    for t in range(0, n + 1, 1):
        result += t
    return result


print(f(10))
