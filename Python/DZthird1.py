# Дан список повторяющихся элементов.
# Вернуть список с дублирующимися элементами. В результирующем списке не должно быть дубликатов.

list1 = [1, 2, 3, 5, 2, 2, 1, 13, 4, 2]
list2 = []

for item in list1:
    if list1.count(item) > 1:
        list2.append(item)
print(list(set(list2)))

