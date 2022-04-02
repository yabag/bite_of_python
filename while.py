number = 23
running = True
while running:
    guess = int(input('Введите целое число : '))

    if guess == number:
        print('Поздравляю, вы угадали.')
        running = False  # это останавливает цикл while
    elif guess < number:
        print('Нет, загаданное число больше этого.')
    else:
        print('Нет, загаданное число меньше этого.')
else:
    print('Цикл while закончен.')
    # Здесь мможете выполнить всё что вам ещё угодно

print('Завершение.')
