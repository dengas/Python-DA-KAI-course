# Дан словарь beatles_map, в котором ключ - это имя музыканта, а значение - это инструмент, на котором играет музыкант
# beatles_map = {'Paul': 'Bass', 'John': 'Guitar', 'George': 'Guitar'}
# Напишите код, который выполняет действия со словарём в следующем порядке:
# 1. Добавить в словарь музыканта Ringo, который играет на барабанах (“Drums”)
# 2. В отдельную переменную записать инструмент, на котором играет John и удалить этого музыканта из словаря
# 3. Вывести на экран значения словаря и новой переменной

# Результат должен получиться такой:
# {'Paul': 'Bass', 'George': 'Guitar', 'Ringo': 'Drums'}
# 'Guitar'

beatles_map = {'Paul': 'Bass', 'John': 'Guitar', 'George': 'Guitar'}

beatles_map['Ringo'] = 'Drums'

delete_key = beatles_map.pop('John')

print(beatles_map)
print(delete_key)