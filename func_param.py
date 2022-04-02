def print_Max(a, b):
    if a > b:
        print(a, 'максимально')
    elif a == b:
        print(a, 'равно', b)
    else:
        print(b, 'максимально')


print_Max(3, 4)  # прямая передача значений

x = 5
y = 7

print_Max(x, y)  # передача переменных в качастве аргументов
