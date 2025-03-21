import pandas as pd



# Размер датасета, типы данных и название столбцов
#1 Для чтения .csv файла
df = pd.read_csv('name')

#2 Первые 3 строки
df.head(3)

#3 Последние 2 строки
df.tail(2)

#4 Размер датафрейма (30, 15)
df.shape

#5 Список из названия столбцов
df.columns

#6 Какие есть типы данных в датафрейме
df.dtypes

#7 Показать выбранные столбцы
df[['column_name1','column_name2']].head()



# Обращение к элементам датафрейма
#1 Обращение к последней строки
df.iloc[-1]

#2 Пересечение столбца и строки
df.iloc[-1, 4]

#3 Показать датафрейм с 0 до 6 строки и с column_name1 до column_name2 столбца
df.loc[0:6, 'column_name1':'column_name2']



# Фильтрация
#1 условие
df[df['tripduration'] < 400].shape

#2 условие с оператором &
df[(df['tripduration' ] < 1000) & (df['usertype' ] == 'Subscriber' ) ].shape



# Статистика по датафрейму
#1 статистика по датафрейму (count, мин, макс и тд)
df.describe()

#2 Корреляция между всеми столбцами датасета (если они численные)
df.corr()



# Запись в csv
#1 Запись в .csv
df.to_csv('path_to_file.csv')



# Группировка данных в Pandas
#1 Группировка данных по столбцу
df.groupby(['usertype']).groups

#2 Первые строки из группировки
df.groupby(['usertype']).first()

#3 Средняя продолжительность поездок
df.groupby(['usertype' ])[['tripduration' ]].mean()

#4 Группировка по группе признаков
df.groupby(['usertype', 'start station name'])['tripduration'].mean()

#5 Агрегирование 
df.groupby(['usertype']).agg({'tripduration':[sum,min],
                              'starttime' : 'first'})

