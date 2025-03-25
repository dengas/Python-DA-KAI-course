import pandas as pd

#1 Чтение df
df = pd.read_csv('https://raw.githubusercontent.com/jorisvandenbossche/pandas-tutorial/master/data/titanic.csv')
# print(df)

#2 Создание df из словаря
# df = pd.DataFrame.from_dict({'a' : [1,2], 'b' : [3,4]})
# print(df)

#3 Записали df в папку
# df.to_csv('dataf/tmp.csv')



#1 Информация о df
# df.info()

#2 Возвращает размер
# print(df.shape)

#3 Показывает столбцы
# print(df.columns)

#4 Первые 3 строки
# print(df.head(3))

#5 Последнее 3 строки
# print(df.tail(3))



# Фильтрация данных
#1 Только одна столбец
# df = df['Name']
# print(df)

#2 
# df = df[['Name','Age']].head(3)
# print(df)

#3 Фильтрация с помощью loc: (5, 10, 15) строка, столбец Name и Age. Работает с названием столбцов и со значениями индекса
# df = df.loc[[5, 10, 15], ['Name', 'Age']]
# print(df)

#4 Фильтрация по порядку столбцов и по порядку значения индекса
# df = df.iloc[[5, 10, 15],[0,1]]
# print(df)

#5 Функция iloc() и срезы
# df = df.iloc[5:11, 0:3]
# print(df)



# Фильтрация данных по bool маске
#1 Полученние всех совершеннолетних пользователей, df['Age'] > 18 - series(True, False)
# df = df[df['Age'] > 18]
# print(df)

#2 Пользователи возрастом 15 или 50
# df[df['Age'].isin([15, 50])]
# print(df)

#3 Возраст равен либо 15 либо 50
# df[(df['Age'] == 15) | (df['Age'] == 50)]
# print(df)

# 4 Bool маска, функция проверяет есть ли значения Age в df (False если нет)
# df = df['Age'].notna()
# print(df)

# 5 .isna() антоним .notna()
# df = df['Age'].isna()

# 6 loc() и маска
# df = df.loc[df['Age'].isna(), 'Name']
# print(df)



# Сортировка данных
#1 Сортировка людей по возрасту
# df = df.sort_values('Age').head(10)
# print(df)

#2 Сортировка людей по возрасту, сначала сортитруем по колонке Age потом только по Name, ascending=[False, True] для каждой колонки False - в порядке убывания, True - возрастания
# df = df.sort_values(['Age', 'Name'], ascending=[False, True]).head(10)
# print(df)



# Объединения df
# df2 = df.copy(deep=True)
#1 Конкатенация, то есть объединение по строкам и столбцам
# cdf1 = pd.concat([df, df2])
# print(df.shape)  # (891, 12)
# print(cdf1.shape)  # (1782, 12)
#2 Конкатенация по стобцам
# cdf2 = pd.concat([df, df2], axis=1)
# print(cdf2)

#3 Создаем новый столбец с bool значением (число четное или нет) по старому столбцу
# mdf = pd.DataFrame(index=df.index)
# mdf['PassengerId'] = df['PassengerId']
# Создаем новый столбец с bool значением (число четное или нет) по старому столбцу
# mdf['evenId'] = mdf['PassengerId'].apply(lambda x: x % 2 == 0)
# print(mdf)

#4 Объединение (JOIN) с основным df
# df = pd.merge(df, mdf, how='inner')
# print(df)



# Аналитические функции
#1 Подсчет не нулевых элементов
# df = df['Age'].count()
# print(df)

#2 Среднее значение по столбцу
# df = df['Age'].mean()
# print(df)

#3 Медиана
# df = df['Age'].median()
# print(df)

#4 Сразу несколько статистик (count, mean, std, min, 25%, 50%, 75%, max)
# df = df['Age'].describe()
# print(df)

#5 Группировка данных по нескольким колонкам
# df = df.groupby('Sex')['Age'].mean()
# print(df)
# Sex
# female    27.915709
# male      30.726645

#6 Группировка выжил или нет по полу
# df = df.groupby(['Sex', 'Survived'])['Age'].agg(['mean', 'median'])
# print(df)
#                       mean  median
# Sex    Survived
# female 0         25.046875    24.5
#        1         28.847716    28.0
# male   0         31.618056    29.0
#        1         27.276022    28.0

#7 Посчитать кол-во элементов в столбце
# df = df['Sex'].value_counts()
# print(df)
# Sex
# male      577
# female    314

#8 Корреляция
# df = df.corr(numeric_only=True)
# print(df)



# Визуализация
import matplotlib.pyplot as plt
#1 Гистограмма возраста
# df['Age'].plot(kind='hist', bins=20)
# plt.show()

#2 Распределение возраста
# df['Age'].plot(kind='kde', xlim=[0, 100])
# plt.show()

#3 Распределение по полу
# df.groupby('Sex')['Age'].plot(kind='kde', xlim=[0, 100], legend=True)
# plt.show()



# Изменение данных в df
tmp_df = df.copy(deep=True)

#1 Изменения данных столбца у всего df
# tmp_df['Pclass'] = 1
# print(tmp_df)

#2 Создание новой колонки с помощью bool маски
tmp_df['isAdult'] = tmp_df['Age'] >= 18
# print(tmp_df.head(10))

#3 Создание колонки который выжил и взрослый
tmp_df['isAdultSurvived'] = tmp_df['isAdult']
tmp_df.loc[tmp_df['Survived'] == 0, 'isAdultSurvived'] = False
# print(tmp_df)

#4 Переименования колоннок
# renamed_df = tmp_df.rename(
#     columns = {'isAdultSurvived' : 'AdultSurvived'}
# ).head(1)
# print(renamed_df)

#5 Переименование с помощью функций
# renamed_df = tmp_df.rename(columns=str.lower).head(1)
# print(renamed_df)

#6 Приведение каждой строчки в lower case с помощью lambda функции
# tmp_df['lower_case_name'] = tmp_df ['Name'].apply(lambda x: x.lower())
# print(tmp_df['lower_case_name'])

#7 Решение быстрее чем #6
tmp_df['lower_case_name_2'] =tmp_df['Name'].str.lower()
print(tmp_df['lower_case_name_2'])
