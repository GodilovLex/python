rev = int(input('Введите выручку: '))
exp = int(input('Введите расходы: '))
fin_res = rev - exp
if fin_res >= 0:
    print('Прибыль: ', fin_res)
    ros = fin_res/rev
    print('Рентабельность: ', ros)
    staff = int(input('Введите количество сотрудников: '))
    print('Прибыль на одного сотрудника:  ', fin_res/staff)
else:
    print('Убыток:  ', fin_res * -1)

