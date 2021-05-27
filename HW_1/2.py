time_in_secs = int(input('Введите количество секунд для преобразования :'))
seconds = time_in_secs % 60
hours = time_in_secs // (60 * 60)
minutes = time_in_secs // 60 % 60
print(f'{str(time_in_secs)} секунд равно {hours}h {minutes}m {seconds}s')