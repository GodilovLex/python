a = int(input('Введите результат 1-го дня: '))
b = int(input('Введите требуемый результат: '))
growth = 0.1
day = 1
while b >= a:
    day += 1
    a *= (1 + growth)
print(f'На {day}-й день спортсмен достиг результата - не менее {b} км')