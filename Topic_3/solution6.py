# Мы снова работаем с базой данных магазина одежды, но в этот раз структуру немного изменили. Здесь информация делится на два словаря: первый отвечает за коды (id) товаров, второй — за списки количества разнообразных товаров, которые есть в наличии в магазине
# Каждая запись второго словаря отображает, сколько и по какой цене лежит товар  (quantity - количество, price - цена за одну штуку)
# Напишите программу, которая рассчитывает, на какую сумму лежит каждого товара и выводит эту информацию на экран.

# Результат работы программы.
# t-shirt - 120 pieces, worth 106500 rub.
# sneakers - 36 pieces, worth 183000 rub.
# trousers - 72 pieces, worth 83900 rub.
# cap - 5 pieces, worth 3000 rub.
# jacket - 11 pieces, worth 165000 rub.

ids = {
    't-shirt': '10',
    'sneakers': '20',
    'trousers': '30',
    'cap': '40',
    'jacket': '50'
}

store = {
    '10': [
        {'quantity': 50, 'price': 800},
        {'quantity': 70, 'price': 950},
    ],

    '20': [
        {'quantity': 6, 'price': 5000},
        {'quantity': 12, 'price': 6000},
        {'quantity': 18, 'price': 4500},
    ],

    '30': [
        {'quantity': 22, 'price': 1200},
        {'quantity': 50, 'price': 1150},
    ],

    '40': [
        {'quantity': 5, 'price': 600},
    ],
    '50': [
        {'quantity': 11, 'price': 15000},
    ]
}

for ids_name, ids_id in ids.items():
    for store_id, store_dict in store.items():
        if ids_id == store_id:
            # print(f"{ids_name} {store_dict}")
            cost = 0
            pices = 0
            for values in store_dict:
                pices = pices + values['quantity']
                cost = cost + values['quantity']*values['price']
                # print("Pices = ", pices)
                # print("Cost = ", cost)
                # for key, value in values.items():
                #     print(value)
                    
    print(f"{ids_name} - {pices} pieces, worth {cost} rub.")