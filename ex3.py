def fac(n):
    return fac(n - 1) * n if n > 1 else 1


print(fac(int(input())))
