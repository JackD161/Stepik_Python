# заведем пустой список
d=[]

# заполним список с помощью list comprehension
#d=[int(i) for i in input().split()]
d=[4,8,0,3,4,2,0,3,8]
#print ("Введено","\t",d)

# отсортируем список методом sort
d.sort()
#print ("Отсортировано","\t",d)

# зададим цикл который пройдет по всмему введенному списку
for i in d:
# посчитаем количество одинаковых значений итерируемого списка
    g=d.count(i)-1
# посчитаем индекс первого найденного итерируемого значения
    ind=d.index(i)
# удалим одиночно введенные данные
    if g == 0:
        del d[ind]
    # удилим элемент

    print (d[ind],ind)

# вывод результата
#print ("Результат","\t",d)