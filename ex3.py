def calculation_of_total(R, T, C):
    if -129 > R > 128 and -1 > T > 8 and -1 > C > 8:
        return 'error'

    if T == 0:
        if R != 0:
            return 3
        else:
            return C
    elif T == 1:
        return C
    elif T == 4:
        if R != 0:
            return 3
        else:
            return 4
    elif T == 6:
        return 0
    elif T == 7:
        return 1
    else:
        return T


R, T, C = int(input()), int(input()), int(input())
print(calculation_of_total(R, T, C))
