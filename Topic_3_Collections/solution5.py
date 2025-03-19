# Создайте два списка, в каждом из которых лежит 10 случайных букв алфавита (могут повторяться). 
# Затем для каждого списка создайте словарь из пар «индекс — значение» и выведите оба словаря на экран.
# Для генерации случайных букв можно использовать модуль random.

# Пример: 
# Первый список: ['й', 'р', 'с', 'г', 'а', 'а', 'т', 'ж', 'е', 'к']
# Второй список: ['д', 'а', 'а', 'в', 'т', 'ж', 'р', 'б', 'й', 'р']
# Первый словарь: {0: 'й', 1: 'р', 2: 'с', 3: 'г', 4: 'а', 5: 'а', 6: 'т', 7: 'ж', 8: 'е', 9: 'к'}
# Второй словарь: {0: 'д', 1: 'а', 2: 'а', 3: 'в', 4: 'т', 5: 'ж', 6: 'р', 7: 'б', 8: 'й', 9: 'р'}

import random

russian_alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"  
my_list1 = []
my_list2 = []
i = 0

while i < 10:
    letter1 = random.choice(russian_alphabet)
    letter2 = random.choice(russian_alphabet)
    my_list1.append(letter1)
    my_list2.append(letter2)
    i += 1
    
# print(my_list1)
# print(my_list2)

my_dict1 = {n : my_list1[n] for n in range(len(my_list1))}
my_dict2 = {n : my_list2[n] for n in range(len(my_list2))}

print(my_dict1)
print(my_dict2)