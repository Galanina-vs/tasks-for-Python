# Написать функцию которая будет возвращать float число основываясь на текущем времени
# В 00:00 возвращаем 1.01, дальше с шагом 3 минуты увеличиваем число на 0.01.
# 00:00 - 00:02 - 1.01
# 00:03 - 00:05 - 1.02
# 00:06 - 00:08 - 1.03 и т.д.

from datetime import datetime


def generate_float_number():
    current_time = datetime.now().time()
    start_time = datetime.strptime('00:00', '%H:%M').time()
    delta_minutes = (current_time.minute - start_time.minute) % 3
    step = (current_time.minute - start_time.minute) // 3
    return 1.01 + step * 0.01 + delta_minutes * 0.01


print(generate_float_number())

# Этот код сначала получает текущее время, затем вычисляет разницу во времени между текущим временем и временем
# начала (00:00). Затем он использует это разделение, чтобы определить количество шагов и количество минут в текущем
# шаге. И, наконец, он вычисляет число с учетом условий вашей задачи и возвращает его.
