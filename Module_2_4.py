# Исходный список чисел
numbers = [1, 2, 3, 4, 5, 6, 7, 9, 10, 11, 12, 13, 14, 15]

# Пустые списки для простых и не простых чисел
primes = []  # Пустые списки для простых чисел
not_primes = []  # Пустые списки для не простых чисел

# Перебираем числа из списка numbers
for number in numbers:
    if number == 1:  # 1 не является ни простым,ни составным
        continue
    is_prime = True  # Флаг, обозначающий простоту числа
    for i in range(2, int(number ** 0.5) + 1):  # Проверка делителей до корня числа
        if number % i == 0:  # Если число делится на i, оно не простое
            is_prime = False
            break  # Прерываем проверку
    if is_prime:  # Если число простое
        primes.append(number)
    else:  # Если число не простое
        not_primes.append(number)

# Выводим результаты
print("Простые числа:", primes)
print("Не простые числа:", not_primes)
