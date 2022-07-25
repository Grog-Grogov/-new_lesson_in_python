#  Списковые включения
# ▫️На входе программа получает список целых чисел s. Сформируйте список, состоящий только из чётных элементов s.
a = [x for x in (1, 2, 3, 4, 5 ,8, 9, 12, 14 , 115, 21, 26, 48, 99) if x % 2 == 0]
print('Список из чётных элементов', a)

#  Генераторы-выражения
#  ️На входе программа получает список целых чисел s. Составьте генератор-выражение и вычислите все элементы,
# состоящие только из двухзначных элементов s, записанных 2 раза подряд.

list_numbers_2 = [78, 99, 66, 44, 50, 50,  30, 45, 15, 15, 25, 20, 1, 233]
element_count = ([item for item in list_numbers_2 if 10 <= item <= 99])
print(list_numbers_2[0])

print("элементы списка из двухзначных элементов:", element_count)

#  Генераторы-функции
#  ️На входе программа получает список целых чисел s. Составьте генератор-функцию и вычислите все элементы, стоящих на позициях, не кратных 3.

list_numbers_3 = [78, 99, 66, 44, 50, 50,  30, 45, 15, 15, 25, 20, 1, 233]


alphabets1 = [70, 79, 67,]
alphabets = [78, 99, 66, 44, 50, 50,  30, 45, 15, 15, 25, 20, 1, 233]
a = [x for x in alphabets]
print(a)
print(alphabets1)