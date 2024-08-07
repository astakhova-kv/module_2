def poisk_parolya(left_ch):
    parol = ''
    for slg1 in range(1, left_ch):
        for slg2 in range(slg1 + 1, left_ch):
            if left_ch % (slg1 + slg2) == 0:
                parol += str(slg1)
                parol += str(slg2)
    return parol


result = poisk_parolya(int(input('Введите число от 3 до 20: ')))
print(result)
