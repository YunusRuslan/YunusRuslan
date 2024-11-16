"""
tuple_ = 1,2,3,True, "String"
list_ = [1,2,3, True, "String"]
print(tuple_.__sizeof__())
print(list_.__sizeof__())
"""
# Задайте переменные разных типов данных:
immutable_var = (1, 2, 'a', 'b')
print("Кортеж Immutable tuple:", immutable_var)
# Попытка изменения значения кортежа
print("immutable_var[0] = 100 # Попытка изменить кортеж (неизменяем), при проверки следующая строка вызовет ошибку")
print("Ошибка при попытке изменить кортеж: TypeError: 'tuple' object does not support item assignment")
print("Объяснение: Кортежи являются неизменяемыми объектами, поэтому нельзя изменить их элементы напрямую.")
# Создание изменяемого списка
mutable_list = [1, 2, 'a', 'b']
print("Cписок mutable list:", mutable_list)
# Изменение значений списка
mutable_list[0] = 100  # Изменение первого элемента
mutable_list.append("Modified")  # Добавление нового элемента
print("Изменённый список Mutable list:", mutable_list)
