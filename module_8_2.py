def personal_sum(numbers):
    # присвоила переменным значения 0 перед вычислением
    result = 0
    incorrect_data = 0
    # цикл перебора значений numbers
    for i in numbers:
        # блок проверки на ошибки
        try:
            # вычисление суммы чисел в numbers
            result += i
        # блок подсчета ошибок типа данных
        except TypeError:
            # подсчет количества выявленых ошибок типов данных
            print(f'Некорректный тип данных для подсчёта суммы — {i}')
            incorrect_data += 1
    # возврат полученных результатов в виде кортежа
    return (result, incorrect_data)


def calculate_average(numbers):
    try:
        # обращение за данными к функции personal_sum()(кортеж)
        per_sum = personal_sum(numbers)
        # подсчет среднего арифметического через индексы кортежа per_sum
        avg = per_sum[0] / (len(numbers) - per_sum[1])
        return avg
    # блок обработки ошиибок деления на 0
    except ZeroDivisionError:
        return 0
    # блок обработки ошибок типа данных
    except TypeError:
        print(f'В numbers записан некорректный тип данных')
        return None



print(f'Результат 1: {calculate_average("1, 2, 3")}') # Строка перебирается, но каждый символ - строковый тип
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}') # Учитываются только 1 и 3
print(f'Результат 3: {calculate_average(567)}') # Передана не коллекция
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}') # Всё должно работать