# Ввод трёх целых чисел в переменных
print("Ввод в консоль 1 :")
first = int(input())
second = int(input())
third = int(input())

# Условная конструкция
if first == second == third:  # Все три числа равны
    print(3, 'Все три числа равны')
elif first == second or first == third or second == third:  # Два числа равны
    print(2, 'Два числа равны')
else:  # Ни одно число не равно другому
    print(0, 'Ни одно число не равно другому')

