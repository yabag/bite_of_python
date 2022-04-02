n = int(input())
f1, f2, f3 = 1, 1, 1
if n < 4:
    print((1,)*n)
else:
    for _ in range(n):
        print(f1)
        f1, f2, f3 = f3, f2, f1 + f2 +f3

