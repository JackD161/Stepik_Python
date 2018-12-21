# заведем пустой список
d=[]

# заполним список с помощью list comprehension
#d=[int(i) for i in input().split()]
d=[4,0,8,8,3,4,2,0,9,3]
print ("Введено","\t",d)

# отсортируем список методом sort
d.sort()
print ("Отсортировано","\t",d)

# зададим цикл который пройдет по всмему введенному списку
for i in d:
# посчитаем количество одинаковых значений итерируемого списка
    cnt=d.count(i)
    ind=d.index(i)
    print(i, d[ind], ind)
    #if cnt==1:
    #    del d[ind]
    #if cnt > 1:
     #   del d[ind:ind+cnt-1]
    #print(d[ind], ind)
print ("Вывод",d)