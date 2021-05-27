n = int(input('Введите число: '))
max_digit = 9
cur_max = 0
if n < 10:
    cur_max = n
while (n % 10) != n:
    cur_digit = n % 10
    if max_digit == cur_digit:
        cur_max = cur_digit
        break
    n = n // 10
    if cur_max < cur_digit:
        cur_max = cur_digit

print('Максимальная цифра в числе равна ', cur_max)